"""JSON Lines 读写

记录于 2026-10-07。可直接复制使用，无需第三方依赖。
"""

import json
from pathlib import Path
from typing import Any, Iterator


def write_jsonl(path: str | Path, rows: list[dict]) -> None:
    """按行写 JSON，适合日志和增量追加，不需要一次性载入整个文件。"""
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_jsonl(path: str | Path) -> Iterator[Any]:
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)

