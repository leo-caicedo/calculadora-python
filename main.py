# Calculadora
import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def porcentaje(a, b):
    return (a * b) / 100

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(a)