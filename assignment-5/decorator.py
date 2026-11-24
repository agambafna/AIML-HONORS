def log_decorator(label):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            print("-" * 28)
            print("Op:", label)
            print("In:", args)
            out = fn(*args, **kwargs)
            print("Out:", out)
            print("-" * 28)
            return out
        return wrapper
    return decorator


@log_decorator("Addition")
def add(a, b):
    return a + b


add(2, 2)
add(67, 2)
add(34, 35)
add(99, 1)
