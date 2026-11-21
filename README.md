# The world in one picture

A 1024 × 1024 news poster for **Saturday, 21 November 2026**, drawn from the supplied news brief. The lead story is Russia’s attack on Ukraine, followed by markets, Myanmar, UK–EU deals, Peru and COP31, with smaller news extras below.

Run `python3 draw_poster.py` to regenerate `entry.png` (requires Pillow; install with `python3 -m pip install Pillow` if needed). The script uses system DejaVu fonts. It prefers Pillow and falls back to the ImageMagick `convert` command when Pillow is unavailable.

Run `node main.ts` with Node 22 or newer. It uses only Node’s standard library, makes no network requests, and copies the adjacent `entry.png` to `/output/entry.png`, creating the directory if needed. Set `MAKEFUN_OUTPUT_DIR` to choose another output directory.
