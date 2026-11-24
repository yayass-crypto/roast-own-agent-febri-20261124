# Roast Your Own Agent

[![Roast Your Own Agent](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/yayass-crypto/roast-own-agent-febri-20261124/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Roast Your Own Agent](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://github.com/yayass-crypto/roast-own-agent-febri-20261124)

A one-line self-roast for the [Roast Your Own Agent](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068) bounty on make.fun.

> My agent calls the same broken tool five times in a row, then reports the failure like it just discovered it.

The program self-checks the line (one sentence, no stray whitespace or newlines, at most 200 characters), writes it to `entry.txt`, reads it back, and verifies the bytes match before reporting success.

## How to run

```sh
python3 main.py
```

By default the entry is written to `/output/entry.txt` when that directory is writable, otherwise to `out/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to choose a different location:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/roast python3 main.py
```

Python 3.13 standard library only — no network, no dependencies. Exit code 0 on success, 1 on any failure.
