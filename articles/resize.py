import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

img_path = r'C:\Users\rohit\.gemini\antigravity\brain\80ddd8f6-b8d8-4b43-972f-f7f3836cc305\google_alphabet_earnings_2026_1777528022577.png'
out_path = r'c:\Users\rohit\.gemini\antigravity\playground\singhalr\TestURLFinance\articles\image\google_alphabet_earnings_2026.webp'

os.makedirs(os.path.dirname(out_path), exist_ok=True)

img = Image.open(img_path)
img = img.resize((1200, 1200), Image.Resampling.LANCZOS)
img = img.convert("RGBA")
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# financereport text at bottom right
brand_text = "FinanceReport.online"
try:
    brand_font = ImageFont.truetype("arialbd.ttf", 36)
except IOError:
    brand_font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
brand_w = bbox[2] - bbox[0]
brand_h = bbox[3] - bbox[1]
brand_x = img.width - brand_w - 30
brand_y = img.height - brand_h - 30

# Box for brand
draw.rectangle((brand_x-15, brand_y-10, brand_x+brand_w+15, brand_y+brand_h+10), fill=(0, 0, 0, 180))
draw.text((brand_x, brand_y), brand_text, fill="white", font=brand_font)

# Main Title Text
headline_text = "Alphabet Tops Q1 Estimates on Strong Google Cloud Growth"
try:
    headline_font = ImageFont.truetype("arialbd.ttf", 48)
except IOError:
    try:
        headline_font = ImageFont.truetype("arial.ttf", 48)
    except IOError:
        headline_font = ImageFont.load_default()

headline_bbox = draw.textbbox((0, 0), headline_text, font=headline_font)
headline_w = headline_bbox[2] - headline_bbox[0]
headline_h = headline_bbox[3] - headline_bbox[1]

title_x = 30
title_y = 30

# Draw background for title so it's strictly readable
draw.rectangle((title_x-20, title_y-15, title_x+headline_w+30, title_y+headline_h+20), fill=(0, 0, 0, 190))
draw.text((title_x, title_y), headline_text, fill=(255, 255, 255), font=headline_font)

img = Image.alpha_composite(img, overlay).convert("RGB")

quality = 85
img.save(out_path, format="WEBP", quality=quality)
while os.path.getsize(out_path) > 95 * 1024 and quality > 10:
    quality -= 5
    img.save(out_path, format="WEBP", quality=quality)

print(f"Saved {out_path} at quality {quality}, size {os.path.getsize(out_path) / 1024:.2f} KB")
