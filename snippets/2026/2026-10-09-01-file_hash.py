"""计算文件哈希

记录于 2026-10-09。可直接复制使用，无需第三方依赖。
"""

import hashlib
from pathlib import Path


def file_hash(path: str | Path, algo: str = "sha256") -> str:
    """分块读取文件算哈希，大文件也不会把内存吃满。"""
    h = hashlib.new(algo)
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

