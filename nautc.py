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
email    : Nasy <nasyxx+python@gmail.com>
filename : nautc.py
project  : nautc

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
__version__ = "0.1.0"
# Standard Library
import re
import sys
import html
from typing import Tuple, Iterator
from urllib.parse import quote

# Web Packages
import requests as req

URL = "http://qaz.wtf/u/convert.cgi?text={}"
UTC = re.compile(
    r"<tr><td><span .+?>(.*?)</span>(.*?)</td><td>(.*?)</td></tr>", re.S
)


def nautc(text: str) -> Iterator[Tuple[str, str]]:
    """Convert plain text to obscure characters from Unicode."""
    return map(
        lambda x: (x[0] + x[1], html.unescape(x[2])),
        UTC.findall(req.get(URL.format(quote(text))).text),
    )


__all__ = ["nautc"]


def main() -> None:
    """Main function."""
    for n, s in nautc(
        not sys.stdin.isatty() and sys.stdin.read() or "".join(sys.argv[1:])
    ):
        print(n + s + ("-" * 20))


if __name__ == "__main__":
    main()
