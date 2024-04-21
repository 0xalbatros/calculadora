import math
import re

diccionario = math.__dict__
funciones = list({n for n in diccionario.keys() if n[0] != "_" and any(callable(n) for n in diccionario.values())})

def algebra(expresion, variables):
  try:
    for k in variables.keys():
      if len(k) > 1 or k == "e":
        print(f"Error: {k} no se puede modificar")
        return calculadora()
    diccionario.update(variables)
    return eval(expresion, diccionario)
  except Exception as error:
    print(error)

diccionario.update({"fn":algebra})

def validar(input):
  regex = r'([\+\-\*\/\^\s]|acos|acosh|asin|asinh|atan|atan2|atanh|cbrt|ceil|comb|copysign|cos|cosh|degrees|dist|erf|erfc|exp|exp2|expm1|fabs|factorial|floor|fmod|frexp|fsum|gamma|gcd|hypot|isclose|isfinite|isinf|isnan|isqrt|lcm|ldexp|lgamma|log|log10|log1p|log2|modf|nextafter|perm|pow|prod|radians|remainder|sin|sinh|sqrt|sumprod|tan|tanh|trunc|ulp|fn)+\('
  funciones = re.findall(regex, input)
  parentesis = re.findall(r'\(', input)
  if len(parentesis) > 0 and len(funciones) == 0:
    print("Error: solo se permiten funciones de la libreria math de python")
    return calculadora()
  resultado = eval(input, diccionario)
  try:
    float(resultado)
    int(resultado)
    complex(resultado)
  except Exception:
    print("Input invalido")
    return calculadora()

print("\n\nComandos:\noperación\nalgebra\nfunciones\nconstantes\nexit\n\n")

def calculadora():
  try:
    inp = input(">> ")
    if inp == "exit":
      print("Fin del programa")
      return exit()
    if inp == "operacion":
      print("\n\nInstrucciones:\n\n>> Escribe la operación en una linea. Puedes anidar operaciones utilizando paréntesis (). \n\n\tEjemplo:\n\t>> ((pi*3)**2)/2. \n\n>> Para obtener el resultado presiona Enter. \n\n>> Para obtener el input anterior presiona flecha arriba\n\n")
      return calculadora()
    if inp == "algebra":
      print("\n\nInstrucciones:\n\n>> Las operaciones algebraicas deben estar escritas de la siguiente manera fn('', {'x':1}). \n\n\tEjemplo:\n\t>> fn('x**2', {'x':5}).\n\n>> Puedes introducir mas de una variable. \n\n\tEjemplo:\n\t>> fn('x**2+y', {'x':5, 'y':3}).\n\n>> Puedes declarar valores de variables y posteriormente usarlos en una operación sin necesidad de escribir fn() y utilizar comillas. \n\n\tEjemplo:\n\tDeclaras el valor de x \n\t>> fn('x', {'x':5})\n\tluego utilizar x en una operación \n\t>> x*5\n\tEl valor de x se conserva hasta que se cierre la aplicación o hasta que se le reasigne valor.\n\n>> Para casos donde se multiplica la variable es necesario indicar el *.\n\n\tEjemplo:\n\t'5x' es invalido '5*x es correcto'\n\n>> Cuando utilizas fn(), es importante escribir la expresión entre comillas 'x+3' y las variables entre llaves y con comillas {'x':5, 'y':3, 'z':7}\n\n")
      return calculadora()
    if inp == "funciones":
      print("\nFunciones válidas:", *funciones)
      print("\n\nInstrucciones:\n\n>> Al usar una función valida debes utilizar paréntesis para escribir la variable. \n\n\tEjemplo:\n\t>> sin(5), log(3), sqrt(9).\n\n>> Hay algunas funciones validas que requieren dos variables. \n\n\tEjemplo:\n\tpow(2,2).\n\n>> La calculadora utiliza la librería matemática de python, si quieres mas detalles sobre una función los puedes encontrar aquí: https://docs.python.org/3/library/math.html \n\n")
      return calculadora()
    if inp == "constantes":
      print("\nConstantes: pi e tau")
      print("\n\nInstrucciones:\n\n>> Se utilizan como cualquier otro numero, no requieren paréntesis. \n\n\tEjemplo:\n\t>> pi*3/e\n\n")
      return calculadora()
    validar(inp)
    resultado = eval(inp, diccionario)
    print("r =", resultado)
    return calculadora()
  except Exception as error:
    print("Error:", error)
    return calculadora()

calculadora()