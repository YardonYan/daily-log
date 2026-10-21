"""计时上下文管理器

记录于 2026-10-22。可直接复制使用，无需第三方依赖。
"""

import time
from contextlib import contextmanager


@contextmanager
def timer(label="block"):
    """统计一段代码的耗时，异常时同样会打印，方便定位慢调用。"""
    start = time.perf_counter()
    try:
        yield
    finally:
        cost = (time.perf_counter() - start) * 1000
        print(f"[{label}] {cost:.2f} ms")

