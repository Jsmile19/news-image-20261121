#!/usr/bin/env python3
"""Draw the 21 November 2026 news poster using supplied editorial facts."""
from pathlib import Path
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    # Offline fallback: the environment may have neither Pillow nor pip.
    # ImageMagick supplies the same raster drawing operations here.
    import json
    import subprocess
    import tempfile

    class ImageFont:
        @staticmethod
        def truetype(path, size):
            return (path, size)

    class Image:
        @staticmethod
        def new(mode, size, color):
            return Image(size, color)

        def __init__(self, size, color):
            self.size = size
            self.commands = [f"fill '{color}' rectangle 0,0,{size[0]},{size[1]}"]

        def save(self, path, optimize=True):
            with tempfile.NamedTemporaryFile(mode='w', suffix='.mvg') as f:
                f.write('\n'.join(self.commands))
                f.flush()
                subprocess.run(['convert', '-size', f'{self.size[0]}x{self.size[1]}',
                                'xc:white', '-draw', '\n'.join(self.commands), '-strip',
                                'PNG24:'+str(path)], check=True)

    class ImageDraw:
        @staticmethod
        def Draw(image):
            return ImageDraw(image)

        def __init__(self, image):
            self.commands = image.commands

        def rectangle(self, box, fill=None, outline=None, width=1):
            x1, y1, x2, y2 = box
            self.commands.append(f"fill '{fill or 'none'}' stroke '{outline or 'none'}' "
                                 f'stroke-width {width} rectangle {x1},{y1},{x2},{y2}')

        def textbbox(self, xy, value, font):
            path, size = font
            width = int(subprocess.check_output([
                'convert', '-font', path, '-pointsize', str(size),
                'label:'+value, '-format', '%w', 'info:']))
            return (xy[0], xy[1], xy[0]+width, xy[1]+size)

        def text(self, xy, value, font, fill):
            path, size = font
            x, y = xy
            self.commands.append(f"font '{path}' font-size {size} fill '{fill}' stroke none "
                                 f'text {x},{y+size} '+json.dumps(value, ensure_ascii=False))

ROOT = Path(__file__).resolve().parent
FONT = Path('/usr/share/fonts/truetype/dejavu')
PAPER, INK, RED, MUTED = '#F5F0E5', '#14262D', '#BD3528', '#45565A'
im = Image.new('RGB', (1024, 1024), PAPER)
d = ImageDraw.Draw(im)

def font(size, bold=False):
    return ImageFont.truetype(str(FONT / ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')), size)

def text(x, y, value, size, color=INK, bold=False):
    f = font(size, bold)
    box = d.textbbox((x, y), value, font=f)
    assert box[2] <= 1000, (value, box)
    d.text((x, y), value, font=f, fill=color)

def panel(x, y, w, h, label, title, lines):
    d.rectangle((x, y, x+w, y+h), outline=INK, width=2)
    text(x+15, y+9, label, 17, RED, True)
    text(x+15, y+34, title, 30, INK, True)
    for i, line in enumerate(lines):
        text(x+15, y+69+i*26, line, 23)

# Masthead: the date is the anchor of the image.
d.rectangle((0, 0, 1024, 130), fill=INK)
text(30, 15, 'THE WORLD IN ONE PICTURE', 24, PAPER, True)
text(30, 53, 'SATURDAY 21 NOVEMBER 2026', 51, PAPER, True)

# Lead story.
text(30, 146, 'UKRAINE / POLAND', 23, RED, True)
text(30, 180, "RUSSIA’S BIGGEST", 66, INK, True)
text(30, 252, 'ATTACK ON UKRAINE', 66, INK, True)
text(30, 336, '400+ drones, 110 missiles overnight; 8+ killed in Kyiv.', 30)
text(30, 378, 'Poland: 2 missiles + suspected drone; Tusk: “deliberate provocation”.', 25)

# Markets occupy the widest secondary panel.
panel(30, 435, 964, 126, 'MARKETS / AI', 'AI STOCKS ROUT', [
    'S&P 500 + Dow in correction; Nasdaq loses all 2026 gains.',
    'Anthropic falls after IPO; Nvidia faces SEC accounting probe.'
])
panel(30, 577, 474, 130, 'WORLD COURT', 'MYANMAR: GENOCIDE', [
    'ICJ finds Myanmar responsible',
    'for genocide against Rohingya.'
])
panel(520, 577, 474, 130, 'BRUSSELS / BIGGEST SINCE BREXIT', 'UK–EU DEALS SIGNED', [
    'Food, carbon; youth mobility',
    'for 100,000 young Britons.'
])
panel(30, 723, 474, 130, 'CENTRAL PERU', 'MAGNITUDE 6.8 QUAKE', [
    'Earthquake felt in Lima.'
])
panel(520, 723, 474, 130, 'ANTALYA, TURKEY', 'COP31 IN OVERTIME', [
    'Nearly 200 nations deadlocked',
    'on fossil fuels; deadline passes.'
])

# Each extra remains a single line; dots separate the ticker items.
d.rectangle((0, 873, 1024, 1024), fill=INK)
extras = [
    'Pancreatic cancer pill trial: tumours undetectable in 1 in 12',
    'GTA VI: $3.8bn first-day sales record',
    'Gen Z protests spread across 25 European countries',
    'FBI criminal database reportedly hacked',
    'Israeli strikes kill Palestinians in Gaza',
]
for i, line in enumerate(extras):
    text(30, 881+i*27, '•  '+line, 23, PAPER)

im.save(ROOT / 'entry.png', optimize=True)
print(f'Saved {ROOT / "entry.png"}')
