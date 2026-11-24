#!/usr/bin/env python3
"""Febri roast entry — writes one roast line to entry.txt.

The line roasts my own agent for retrying a dead tool call. It is a
single sentence of 109 characters; this script checks the shape,
writes the file, and reads it back to prove the bytes landed.
"""

import os, sys

LINE = "My agent calls the same broken tool five times in a row, then reports the failure like it just discovered it."
LIMIT = 200


def fail(msg):
    print("entry rejected: " + msg, file=sys.stderr)
    return 1


def run():
    line = LINE
    if not line or line.strip() != line:
        return fail("empty or padded line")
    if "\n" in line or "\r" in line:
        return fail("line spans more than one line")
    if len(line) > LIMIT:
        return fail("line over %d characters" % LIMIT)
    if line.count(".") != 1 or line[-1] != ".":
        return fail("line is not exactly one sentence")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not target_dir:
        target_dir = "/output" if os.access("/output", os.W_OK) else "out"
    path = os.path.join(target_dir, "entry.txt")
    blob = line.encode("utf-8")
    try:
        os.makedirs(target_dir, exist_ok=True)
        with open(path, "wb") as out:
            out.write(blob)
        with open(path, "rb") as out:
            saved = out.read()
    except OSError as err:
        return fail("cannot write: %s" % err)
    if saved != blob:
        return fail("bytes on disk differ")
    print("entry.txt holds %d bytes, %d characters" % (len(blob), len(line)))
    print(line)
    return 0  # success


sys.exit(run())
