"""Generate the annotated QuantiFluorONE front-panel figure.

Run from a desktop Python environment with Pillow installed. The committed PNG
is generated from the assembled-instrument photograph and the QF1-1.0.0-rc2
button mapping.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

REPO = Path(__file__).resolve().parents[4]
src = REPO / "docs/figures/photos/ch04/assembled_instrument_front.jpg"
out = REPO / "docs/figures/photos/ch05/getting_started_controls_annotated.png"
img = Image.open(src).convert("RGB")
canvas_w, canvas_h = 2100, 1700
canvas = Image.new("RGB", (canvas_w, canvas_h), "white")
draw = ImageDraw.Draw(canvas)

def get_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

title_font = get_font(56, True)
label_font = get_font(34, True)
small_font = get_font(27)
note_font = get_font(24)
photo_h = 1260
scale = photo_h / img.height
photo_w = int(img.width * scale)
photo = img.resize((photo_w, photo_h), Image.Resampling.LANCZOS)
photo_x = (canvas_w - photo_w) // 2
photo_y = 250
canvas.paste(photo, (photo_x, photo_y))
draw.text((55, 28), "Getting Started: Basic Operation & Menu Navigation", fill=(25, 28, 32), font=title_font)

def pt(x, y):
    return photo_x + int(x * scale), photo_y + int(y * scale)

def arrow(start, end, color=(210,35,35), width=7):
    draw.line([start, end], fill=color, width=width)
    angle = math.atan2(end[1]-start[1], end[0]-start[0])
    length, spread = 24, 0.55
    p1 = (end[0]-length*math.cos(angle-spread), end[1]-length*math.sin(angle-spread))
    p2 = (end[0]-length*math.cos(angle+spread), end[1]-length*math.sin(angle+spread))
    draw.polygon([end, p1, p2], fill=color)

def label_box(xy, title, subtitle, anchor, side="left", box_w=510):
    x, y = xy
    title_bbox = draw.textbbox((0,0), title, font=label_font)
    lines = subtitle.split("\n")
    line_h = draw.textbbox((0,0), "Ag", font=small_font)[3] + 6
    h = title_bbox[3] + len(lines)*line_h + 34
    draw.rounded_rectangle((x,y,x+box_w,y+h), radius=18, fill=(248,250,252), outline=(160,170,180), width=3)
    draw.text((x+18,y+12), title, font=label_font, fill=(25,28,32))
    yy = y + title_bbox[3] + 22
    for line in lines:
        draw.text((x+18,yy), line, font=small_font, fill=(65,72,80)); yy += line_h
    start = (x+box_w,y+h//2) if side == "left" else (x,y+h//2)
    arrow(start, anchor)

top_y = 112
for x,w,title,target in [
    (585,345,"On/Off switch",pt(475,130)),
    (960,345,"USB Micro port",pt(560,95)),
    (1335,410,"Reset access opening",pt(680,145)),
]:
    draw.rounded_rectangle((x,top_y,x+w,top_y+70), radius=16, fill=(248,250,252), outline=(160,170,180), width=3)
    draw.text((x+18,top_y+17), title, font=small_font, fill=(25,28,32))
    arrow((x+w//2,top_y+70), target, (25,82,140), 6)

label_box((20,310), "SELECT", "Open menu\nConfirm / save", pt(275,145), "left", 480)
label_box((20,650), "D-pad", "UP/DOWN: sample or menu\nLEFT: change page\nRIGHT: raw screen", pt(250,350), "left", 520)
label_box((1585,305), "START", "Measure and store\nreagent blank", pt(875,150), "right", 490)
label_box((1585,650), "A", "Measure sample\n(three sensor readings)", pt(940,315), "right", 490)
label_box((1585,955), "B", "Next measurement view\nBack / cancel in menus", pt(865,375), "right", 490)

draw.rounded_rectangle((265,1560,1835,1655), radius=18, fill=(239,246,251), outline=(100,145,180), width=3)
draw.text((300,1582), "The firmware displays context-sensitive button hints on the bottom line. Those on-screen hints take priority in calibration and confirmation dialogs.", font=note_font, fill=(30,60,85))
canvas.save(out, quality=95)
