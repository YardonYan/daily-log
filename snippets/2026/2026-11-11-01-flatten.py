"""展平嵌套列表

记录于 2026-11-11。可直接复制使用，无需第三方依赖。
"""

from collections.abc import Iterable
from typing import Any, Iterator


def flatten(items: Iterable[Any]) -> Iterator[Any]:
    """递归展平任意深度的嵌套列表，返回迭代器，不额外构造中间列表。"""
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item

