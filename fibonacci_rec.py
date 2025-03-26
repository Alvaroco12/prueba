def fibonacci(n):
    if n <= 0:
        print(f"fibonacci({n}) = 0")
        return 0
    elif n == 1:
        print(f"fibonacci({n}) = 1")
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        print(f"fibonacci({n}) = {result}")
        return result
    
print(fibonacci(int(input('Dime un marica numero: '))))