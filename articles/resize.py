import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

img_path = r'C:\Users\rohit\.gemini\antigravity\brain\fcc9557c-2ec4-484f-8096-f3039ec63d96\base_top_7_no_fee_cards_1776593911662.png'
out_path = r'c:\Users\rohit\.gemini\antigravity\playground\singhalr\TestURLFinance\articles\image\top_7_no_fee_cards.webp'

os.makedirs(os.path.dirname(out_path), exist_ok=True)

img = Image.open(img_path)
img = img.resize((800, 450), Image.Resampling.LANCZOS)
img = img.convert("RGBA")
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# financereport text at bottom right
brand_text = "financereport.online"
try:
    brand_font = ImageFont.truetype("arialbd.ttf", 22)
except IOError:
    brand_font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
brand_w = bbox[2] - bbox[0]
brand_h = bbox[3] - bbox[1]
brand_x = img.width - brand_w - 20
brand_y = img.height - brand_h - 20

# Box for brand
draw.rectangle((brand_x-8, brand_y-5, brand_x+brand_w+8, brand_y+brand_h+5), fill=(0, 0, 0, 180))
draw.text((brand_x, brand_y), brand_text, fill="white", font=brand_font)

# Main Title Text
headline_text = "Top 7 No Annual Fee Credit Cards\nHidden Rewards You're Missing"
try:
    headline_font = ImageFont.truetype("arialbd.ttf", 36)
except IOError:
    try:
        headline_font = ImageFont.truetype("arial.ttf", 32)
    except IOError:
        headline_font = ImageFont.load_default()

headline_bbox = draw.textbbox((0, 0), headline_text, font=headline_font)
headline_w = headline_bbox[2] - headline_bbox[0]
headline_h = headline_bbox[3] - headline_bbox[1]

title_x = 20
title_y = 20

# Draw background for title so it's strictly readable
draw.rectangle((title_x-10, title_y-10, title_x+headline_w+20, title_y+headline_h+15), fill=(0, 0, 0, 190))
draw.text((title_x, title_y), headline_text, fill=(255, 255, 255), font=headline_font)

img = Image.alpha_composite(img, overlay).convert("RGB")

quality = 85
img.save(out_path, format="WEBP", quality=quality)
while os.path.getsize(out_path) > 200 * 1024 and quality > 30:
    quality -= 10
    img.save(out_path, format="WEBP", quality=quality)

print(f"Saved {out_path} at quality {quality}, size {os.path.getsize(out_path) / 1024:.2f} KB")
