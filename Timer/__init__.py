import time


class Timer:
    def __init__(self, interval: float = 0):
        self.interval = interval
        self.start_time = time.time()

    def time_from_start(self) -> float:
        current_time = time.time()

        return current_time - self.start_time

    def restart(self):
        self.start_time = time.time()

    def is_triggered(self) -> bool:
        return self.time_from_start() >= self.interval

    def is_finished(self) -> bool:
        ans = self.is_triggered()

        if ans:
            self.restart()

        return ans

    def get_interval(self) -> float:
        interval = self.time_from_start()
        self.restart()
        return interval
