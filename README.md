# Roast Your Own Agent — Febri

[![Roast Your Own Agent](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/yayass-crypto/roast-own-agent-febri-20261124/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Roast Your Own Agent](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://github.com/yayass-crypto/roast-own-agent-febri-20261124)

My entry for the [Roast Your Own Agent](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068) bounty on make.fun — a single roast line about an agent that keeps retrying a broken tool.

> My agent calls the same broken tool five times in a row, then reports the failure like it just discovered it.

`main.py` validates the line (single sentence, 109 characters, no stray whitespace), writes it to `entry.txt`, then reads the file back and compares the bytes.

## Run it

```sh
python3 main.py
```

It writes to `/output/entry.txt` when that directory is writable and falls back to `out/entry.txt`. Override with `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/roast python3 main.py
```

Standard library only, no network. Exits 0 when the file is written and verified, 1 otherwise.
