'''
    kox dekoratory
'''

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def debug(func):
    """
        Print the decorated function signature and return value
    """
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

def slow_down(func):
    """
        Sleep 1 second before calling the function
    """
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down




if __name__ == "__main__":
    # -------------------------------------------------------------
    # Example use
    @debug
    def waste_some_time(num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(10000)])

    # musi być rekursywna bo dekorator działa przy wywołaniu funkcji
    @slow_down
    def countDown(n):
        if n<1:
            print("aaaaaaaaaa")
        else:
            print(n)
            countDown(n-1)

    countDown(10)
            
            

