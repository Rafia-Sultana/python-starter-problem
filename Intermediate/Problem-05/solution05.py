from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n:int) ->int:
    if n<=1:
        return n
    return fibonacci(n-1)+ fibonacci(n-2)

number = 50
print(f"Fibonacci of {number} : {fibonacci(50)}")