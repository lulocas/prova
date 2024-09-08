numero = int(input())

def fibonacci(numero):
    a, b = 0, 1
    x = [0]
    for _ in range(numero):
        a, b = b, a + b
        x.append(a)
    print(x)
    verificar(numero, x)

def verificar(numero, x):
    if numero in x: 
        print(f"{numero} esta em fibonacci")
    else:
        print(f"{numero} nao esta em fibonacci")

fibonacci(numero)
