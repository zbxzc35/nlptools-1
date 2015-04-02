#!/usr/bin/python3

import sys
import unicodedata

# char codes that generates whitespace U+20 while normalization
IGNORE_CHARS = [
    0x00a8, 0x00af, 0x00b4, 0x00b8, 0x02d8, 0x02d9, 0x02da, 0x02db,
    0x02dc, 0x02dd, 0x037a, 0x0384, 0x0385, 0x1fbd, 0x1fbf, 0x1fc0,
    0x1fc1, 0x1fcd, 0x1fce, 0x1fcf, 0x1fdd, 0x1fde, 0x1fdf, 0x1fed,
    0x1fee, 0x1ffd, 0x1ffe, 0x2017, 0x203e, 0x309b, 0x309c, 0xfc5e,
    0xfc5f, 0xfc60, 0xfc61, 0xfc62, 0xfc63, 0xfdfa, 0xfdfb, 0xfe49,
    0xfe4a, 0xfe4b, 0xfe4c, 0xfe70, 0xfe72, 0xfe74, 0xfe76, 0xfe78,
    0xfe7a, 0xfe7c, 0xfe7e, 0xffe3
]

# normalize chars except IGNORE_CHARS
def my_normalize(c):
    return unicodedata.normalize('NFKD', c) if ord(c) not in IGNORE_CHARS else c

def main():
    for l in sys.stdin:
        ll = ''.join(my_normalize(c) for c in l.strip())
        print(unicodedata.normalize('NFC', ll))

if __name__ == '__main__':
    main()

