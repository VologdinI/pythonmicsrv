import time


def time_decorator(func):
    def wrapper(*args, **kwargs): ##https://ru.stackoverflow.com/questions/594651/Что-значит-звёздочка-и-двойная-звёздочка-в-параметрах-функций
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.6f} seconds to execute.")
        return result
    return wrapper

@time_decorator
def sum_and_write():
    with open('input.txt', 'r') as f:
        a = float(f.readline())
        b = float(f.readline())

    result = a + b

    with open('output.txt', 'w') as f:
        f.write(str(result))


@time_decorator
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
sum_and_write()