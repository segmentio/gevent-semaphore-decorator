from functools import wraps

from gevent.coros import BoundedSemaphore


def semaphore(size):
    sem = BoundedSemaphore(size)

    def decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            try:
                sem.acquire()
                result = func(*args, **kwargs)
            finally:
                sem.release()

            return result

        return func_wrapper

    return decorator
