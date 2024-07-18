from datetime import datetime, timedelta
import time
import functools
from typing import Callable, Any

def time_counter(unix_time: bool = False) -> Callable[[Callable[..., Any]], Callable[..., None]]:
    """
    A decorator that measures the execution time of a function.

    Parameters:
    unix_time (bool): If True, the execution time will be returned in seconds.
                      If False, the execution time will be returned as a timedelta object.
    """
    def decorator(func: Callable[..., None]) -> Callable[..., None]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> None:
            start: datetime = datetime.now()
            func(*args, **kwargs)
            delta: timedelta = datetime.now() - start
            if unix_time:
                delta = delta.total_seconds()
            print(f"delta {delta}")
        return wrapper
    return decorator

@time_counter(unix_time=True)
def sleeping(sleep_time: int) -> None:
    """A function that sleeps for a given number of seconds."""
    time.sleep(sleep_time)

@time_counter(unix_time=False)
def sleeping_non_unix(sleep_time: int) -> None:
    """A function that sleeps for a given number of seconds."""
    time.sleep(sleep_time)

# Test functions
if __name__ == "__main__":
    sleeping(2)
    sleeping_non_unix(2)
