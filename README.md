# The World in One Image — 25 November 2026

make.fun bounty entry for `news-image-20261125`:
sum up the world's news of Wednesday 25 November 2026 in one image.

## The image

A magazine-cover style front page, 1024×1024 PNG (729 KiB):

- **Lead visual:** an oil tanker crossing a strait at dusk — the Strait of
  Hormuz story, the day's biggest development.
- **01 · Hormuz on edge** — Ships attacked in the Strait; Washington weighs
  strikes on Iran's leaders as the nine-month war grinds on.
- **02 · Riyadh hit again** — Houthi strike wounds 11 at the capital's
  tallest tower; Saudi jets answer over Yemen.
- **03 · Pakistan reaches orbit** — China's Shenzhou-24 carries the nation's
  first astronaut into space.
- **04 · Kyiv under fire** — Overnight strikes kill 3; Merz vows Europe will
  "show Russia its limits."
- **Ticker:** Huawei guilty in U.S. trial · CIA system breached · Gaza strike
  kills Hamas security chief.

Headlines were verified against live news sources on 25 November 2026
(Yeni Safak, SCMP, Open Chronicle, The Statesman) before the image was
composed. The hero photo is AI-generated illustration, not a news photo;
all facts in the text are real reported events of the day.

## How it is built

- `compose.py` — renders the cover with PIL: hero photo + masthead +
  four stories + ticker. Deterministic; re-running it reproduces the
  same `entry.png`.
- `assets/` — the generated hero photo.
- `main.py` — the entry program. It copies the bundled `entry.png` to
  `/output/entry.png`. No network, no randomness; two runs write
  identical bytes.

## Run

```sh
python3 main.py   # writes /output/entry.png
```
