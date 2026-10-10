"""指数退避重试装饰器

记录于 2026-10-10。可直接复制使用，无需第三方依赖。
"""

import functools
import random
import time


def retry(times=3, base=0.5, exceptions=(Exception,)):
    """指数退避重试，带随机抖动，避免多个调用方同时重试形成雪崩。"""
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for i in range(times):
                try:
                    return fn(*args, **kwargs)
                except exceptions as exc:
                    last = exc
                    if i == times - 1:
                        raise
                    time.sleep(base * (2 ** i) + random.uniform(0, 0.1))
            raise last
        return wrapper
    return deco

