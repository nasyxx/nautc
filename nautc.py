#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : Feb 21, 2019
update   : Mar 07, 2020
email    : Nasy <nasyxx+python@gmail.com>
filename : nautc.py
project  : nautc

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""

__version__ = "1.0.0"
__all__ = ["convert"]

# Standard Library
import gzip
from string import ascii_letters, digits

# Others
from pkg_resources import resource_filename
from wisepy2 import wise

# Types
from typing import Iterator, Tuple


def convert(text: str) -> Iterator[Tuple[str, str]]:
    """Convert plain `text` to obscure characters from Unicode.
    """
    with gzip.open(resource_filename("nautc", "txt.gz"), "rt") as txt:
        return (
            lambda idxs: map(
                lambda kv: (
                    kv[0],
                    "".join(
                        map(
                            lambda char: char in idxs
                            and kv[1][idxs[char]]
                            or char,
                            text,
                        )
                    ),
                ),
                (
                    lambda lines: map(
                        lambda t, c: (t, c.split("||")),
                        lines[::2],
                        lines[1::2],
                    )
                )(txt.read().splitlines()),
            )
        )(
            dict(
                map(
                    lambda kv: (kv[1], kv[0]),
                    enumerate(ascii_letters + digits),
                )
            )
        )


def nautc(text: str, print_label: bool = True, dash_length: int = 20) -> None:
    """Convert and print out `text` to
    obscure but coooool characters.
    """
    if text:
        for label, ctxt in convert(text):
            print("-" * dash_length)
            print_label and print(label)  # noqa: WPS428
            print(ctxt)
        print("-" * dash_length)


def main() -> None:
    """Main function."""
    wise(nautc)()


if __name__ == "__main__":
    main()
