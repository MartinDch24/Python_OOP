def logged(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return (f"you called {func.__name__}{args}{kwargs if kwargs else ''}\n"
                f"it returned {result}")

    return wrapper
