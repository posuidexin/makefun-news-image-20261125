#!/usr/bin/env python3
"""make.fun bounty entry: news-image-20261125.

Sums up the world's news of Wednesday 25 November 2026 in one image.
Deterministic, no network: copies the bundled entry.png to /output/entry.png.
Runs twice -> identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
