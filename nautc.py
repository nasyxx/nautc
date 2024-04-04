#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

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
update   : Apr 03, 2024
email    : Nasy <nasyxx+python@gmail.com>
filename : nautc.py
project  : nautc

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""

__version__ = "1.1.1"
__all__ = ["convert"]

# Standard Library
import gzip
from importlib import resources
from string import ascii_letters, digits

from tyro import cli

# Types
from collections.abc import Iterator


def convert(text: str) -> Iterator[tuple[str, str]]:
  """Convert plain `text` to obscure characters from Unicode."""
  with gzip.open(str(resources.files("nautc") / "txt.gz"), "rt") as txt:
    return (
      lambda idxs: map(
        lambda kv: (
          kv[0],
          "".join(
            map(
              lambda char: char in idxs and kv[1][idxs[char]] or char,
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


def nautc(
  text: str,
  /,
  no_label: bool = False,
  labels: bool = False,
  dash_length: int = 20,
) -> None:
  """Convert and print out `text` to obscure but coooool characters.

  For example:
      # It will only print out funny nautc.
      $> nautc nautc --no_label --dash_length=0
      # It will only print labels.
      $> nautc xx --labels
      # It will return errors.
      $> nautc --labels
  """
  if text:
    for label, ctxt in convert(text):
      print("-" * dash_length)
      ((not no_label) or labels) and print(label) # type: ignore
      not labels and print(ctxt) # type: ignore
    print("-" * dash_length)


def main() -> None:
  """Main function."""
  cli(nautc)


if __name__ == "__main__":
  main()
