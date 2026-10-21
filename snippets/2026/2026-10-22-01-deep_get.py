"""安全取嵌套字典值

记录于 2026-10-22。可直接复制使用，无需第三方依赖。
"""

from typing import Any, Mapping


def deep_get(data: Mapping, path: str, default: Any = None, sep: str = ".") -> Any:
    """按 a.b.c 路径取嵌套字典，任一层缺失就返回默认值，避免一串 if 判断。"""
    cur: Any = data
    for key in path.split(sep):
        if not isinstance(cur, Mapping) or key not in cur:
            return default
        cur = cur[key]
    return cur

