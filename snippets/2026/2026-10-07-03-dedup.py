"""保持顺序去重

记录于 2026-10-07。可直接复制使用，无需第三方依赖。
"""

from typing import Iterable, List, TypeVar

T = TypeVar("T")


def dedup(items: Iterable[T]) -> List[T]:
    """去重但保留原有顺序，比 list(set(...)) 更适合对顺序有要求的场景。"""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out

