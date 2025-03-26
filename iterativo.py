def factorial(n):
    if n < 0:
        return ValueError("El número debe ser no negativo.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(int(input('Dime un marica numero: '))))