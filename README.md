# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Jsmile19/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Jsmile19/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A 1024 × 1024 news poster for **Saturday, 21 November 2026**, drawn from the supplied news brief. The lead story is Russia's attack on Ukraine, followed by markets, Myanmar, UK–EU deals, Peru and COP31, with smaller news extras below.

## Run it

```sh
python3 draw_poster.py
node main.ts
```

Run `python3 draw_poster.py` to regenerate `entry.png` (requires Pillow; install with `python3 -m pip install Pillow` if needed). The script uses system DejaVu fonts. It prefers Pillow and falls back to the ImageMagick `convert` command when Pillow is unavailable.

Run `node main.ts` with Node 22 or newer. It uses only Node's standard library, makes no network requests, and copies the adjacent `entry.png` to `/output/entry.png`, creating the directory if needed. Set `MAKEFUN_OUTPUT_DIR` to choose another output directory.

---

<sub>Entered on [make.fun](https://make.fun/?ref=q3bse5cn&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
