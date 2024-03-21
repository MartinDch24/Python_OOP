from time import time


def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()

        return end - start

    return wrapper()
