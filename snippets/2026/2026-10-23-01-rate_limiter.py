"""简易令牌桶限流

记录于 2026-10-23。可直接复制使用，无需第三方依赖。
"""

import threading
import time


class TokenBucket:
    """令牌桶限流：允许一定程度的突发，长期速率受 rate 约束。"""

    def __init__(self, rate: float, capacity: float):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.updated = time.monotonic()
        self.lock = threading.Lock()

    def acquire(self, amount: float = 1.0) -> bool:
        with self.lock:
            now = time.monotonic()
            self.tokens = min(self.capacity, self.tokens + (now - self.updated) * self.rate)
            self.updated = now
            if self.tokens >= amount:
                self.tokens -= amount
                return True
            return False

