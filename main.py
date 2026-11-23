#!/usr/bin/env python3
"""One Emoji, One Smile — the emoji most likely to make a stranger smile.

"🤗" (hugging face): open arms, warm and friendly at first glance,
universal across ages and backgrounds, and clearly chosen rather than
the default smiley. Writes the emoji to /output/entry.txt.
"""
import os

EMOJI = "🤗"

def main():
    # One emoji only: exactly one code point, 1-8 UTF-8 chars per the gate.
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    assert 1 <= len(EMOJI.encode("utf-8")) <= 8, "entry must be 1-8 UTF-8 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)

if __name__ == "__main__":
    main()
