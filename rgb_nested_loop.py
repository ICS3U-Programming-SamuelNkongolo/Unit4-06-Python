#!/usr/bin/env python3
# Created by: Samuel Nkongolo
# Created on: Dec 1
# This program uses ASCI characters to RGB color code numbers in a range 0-255.


def main():
    for r in range(0, 255, 5):
        for g in range(0, 255, 5):
            for b in range(0, 255, 5):
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        r, g, b, "RBG({}, {}, {})".format(r, g, b)
                    )
                )


if __name__ == "__main":
    main()
