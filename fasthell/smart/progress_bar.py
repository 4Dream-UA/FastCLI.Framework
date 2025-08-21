import sys
import time
from contextlib import contextmanager

class ProgressBar:

    total = 100
    length = 50
    desc = "Progress"
    current = 0
    start_time = time.time()


    def update(self, step=1):
        self.current = min(self.current + step, self.total)
        self._render()

    def _render(self):
        percent = self.current / self.total
        filled = int(self.length * percent)
        bar = "█" * filled + "-" * (self.length - filled)
        elapsed = time.time() - self.start_time
        sys.stdout.write(f"\r{self.desc}: [{bar}] {percent:.1%} | Time: {elapsed:.1f}s")
        sys.stdout.flush()

    def __enter__(self):
        self._render()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.current = self.total
        self._render()
        print()
