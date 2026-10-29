"""列表分块迭代

记录于 2026-10-30。可直接复制使用，无需第三方依赖。
"""

from itertools import islice
from typing import Iterable, Iterator, List, TypeVar

T = TypeVar("T")


def chunked(items: Iterable[T], size: int) -> Iterator[List[T]]:
    """把可迭代对象按固定大小切块，适合批量入库或批量请求。"""
    it = iter(items)
    while block := list(islice(it, size)):
        yield block

