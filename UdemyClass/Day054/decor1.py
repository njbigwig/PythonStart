def log_decorator(func):
    def wrapper():
        print(f"Calling {func.__name__}...")
        func()
        print(f"Finished {func.__name__}!")
    return wrapper

@log_decorator
def say_hello():
    print("Hello, world!")

say_hello()