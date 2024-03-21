def store_results(func):
    _FILE_NAME = "files/log.txt"

    def wrapper(*args, **kwargs):
        with open(_FILE_NAME, "a") as log_file:
            log_file.write(f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}")

    return wrapper
