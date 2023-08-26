def calcular_factorial(numero):
    factorial = 1
    # Completa el bucle for para calcular el factorial
    for i in range(1, numero + 1):
        factorial = factorial * i
       #completar el codigo que me calcule el factorial en esta funcion 
    return factorial


def main():
    try:
        numero = int(input("Ingresa un número entero positivo: "))
        
        if numero < 0:
            print("El número debe ser positivo.")
        else:
            resultado = calcular_factorial(numero)
            print(f"El factorial de {numero} es {resultado}")
    except ValueError:
        print("Debes ingresar un número válido.")

if __name__ == "__main__":
    main()