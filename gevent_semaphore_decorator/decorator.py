from functools import wraps
import logging

from gevent.lock import BoundedSemaphore


def semaphore(size, timeout=30):
    sem = BoundedSemaphore(size)

    def decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            tries = 0
            while True:
                acquired = sem.acquire(timeout=timeout)
                if acquired:
                    try:
                        logging.info("acquired semaphore: %s, attempts: %s",
                            func, tries)
                        result = func(*args, **kwargs)
                    finally:
                        sem.release()
                    return result
                tries += 1
                logging.info("retrying semaphore: %s, attempts: %s",
                    func, tries)

        return func_wrapper

    return decorator
