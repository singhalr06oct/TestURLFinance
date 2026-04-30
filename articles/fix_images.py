import os
from PIL import Image, ImageDraw, ImageFont

images = [
    {
        "in": r"C:\Users\rohit\.gemini\antigravity\brain\80ddd8f6-b8d8-4b43-972f-f7f3836cc305\google_alphabet_earnings_2026_clean_1777530822278.png",
        "out": r"c:\Users\rohit\.gemini\antigravity\playground\singhalr\TestURLFinance\articles\image\google_alphabet_earnings_2026.webp",
        "title": "Alphabet Tops Q1 Estimates on\nStrong Google Cloud Growth"
    },
    {
        "in": r"C:\Users\rohit\.gemini\antigravity\brain\80ddd8f6-b8d8-4b43-972f-f7f3836cc305\ai_printing_money_tech_earnings_2026_clean_1777530838087.png",
        "out": r"c:\Users\rohit\.gemini\antigravity\playground\singhalr\TestURLFinance\articles\image\ai_printing_money_tech_earnings_2026.webp",
        "title": "AI Is Printing Money:\nTech Earnings 2026"
    },
    {
        "in": r"C:\Users\rohit\.gemini\antigravity\brain\80ddd8f6-b8d8-4b43-972f-f7f3836cc305\ai_driven_revenue_models_2026_clean_1777530854792.png",
        "out": r"c:\Users\rohit\.gemini\antigravity\playground\singhalr\TestURLFinance\articles\image\ai_driven_revenue_models_2026.webp",
        "title": "AI-Driven Revenue Models:\nThe Next Evolution"
    }
]

for item in images:
    img_path = item["in"]
    out_path = item["out"]
    title = item["title"]

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
    try:
        headline_font = ImageFont.truetype("arialbd.ttf", 48)
    except IOError:
        headline_font = ImageFont.load_default()

    title_lines = title.split("\n")
    title_x = 30
    title_y = 30
    line_spacing = 15

    # Calculate overall bounding box for title
    max_w = 0
    total_h = 0
    line_heights = []
    
    for line in title_lines:
        bbox = draw.textbbox((0, 0), line, font=headline_font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        max_w = max(max_w, w)
        line_heights.append(h)
        total_h += h
    
    total_h += line_spacing * (len(title_lines) - 1)

    # Draw background for title
    draw.rectangle((title_x-20, title_y-15, title_x+max_w+30, title_y+total_h+20), fill=(0, 0, 0, 190))

    # Draw text line by line
    current_y = title_y
    for i, line in enumerate(title_lines):
        draw.text((title_x, current_y), line, fill=(255, 255, 255), font=headline_font)
        current_y += line_heights[i] + line_spacing

    img = Image.alpha_composite(img, overlay).convert("RGB")

    quality = 85
    img.save(out_path, format="WEBP", quality=quality)
    while os.path.getsize(out_path) > 95 * 1024 and quality > 10:
        quality -= 5
        img.save(out_path, format="WEBP", quality=quality)

    print(f"Saved {out_path} at quality {quality}, size {os.path.getsize(out_path) / 1024:.2f} KB")
