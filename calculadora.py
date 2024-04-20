import math

dic_operaciones = {nombre: getattr(math, nombre) for nombre in dir(math) if nombre[0] != "_" and callable(getattr(math, nombre))}
dic_mathNums = {nombre: getattr(math, nombre) for nombre in dir(math) if nombre == "pi" or nombre == "e" or nombre == "tau" }
dic_operaciones.update(dic_mathNums)

def algebra(expresion, variables):
  try:
    if any(len(k) > 1 or k == "e" for k in variables):
      raise Exception(f"{variables} invalido")
    dic_operaciones.update(variables)
    return eval(expresion, dic_operaciones)
  except Exception as error:
    print(error)

dic_operaciones.update({"fn":algebra})

print("\n\nComandos:\noperacion\nalgebra\nfunciones\nconstantes\nexit\n\n")

def calculadora():
  try:
    operacion = input(">> ")
    if operacion == "exit":
      return print("Fin del programa")
    if operacion == "operacion":
      print("\n\nInstrucciones:\n\n>>Escribe la operacion en una linea. Puedes anidar operaciones utilizando parenstesis (). \n\n\tEjemplo:\n\t>> ((pi*3)**2)/2. \n\n>>Para obtener el resultado presiona Enter. \n\n>>Para obtener el input anterior presiona flecha arriba\n\n")
      return calculadora()
    if operacion == "algebra":
      print("\n\nInstrucciones:\n\n>>Las operaciones algebraicas deben estar escritas de la siguiente manera fn('', {'x':1}). \n\n\tEjemplo:\n\t>> fn('x**2', {'x':5}).\n\n>>Puedes introducir mas de una variable. \n\n\tEjemplo:\n\t>> fx('x**2+y', {'x':5, 'y':3}).\n\n>>Puedes declarar valores de variables y posteriormente usarlos en una operacion sin necesidad de escribir fn() y utilizar comillas. \n\n\tEjemplo:\n\tDeclaras el valor de x \n\t>> fn('x', {'x':5})\n\tluego utilizar x en una operacion \n\t>> x*5\n\tEl valor de x se conserva hasta que se cierre la aplicacion o hasta que se le reasigne valor.\n\n>>Para casos donde se multilpica la variable es necesario indicar el *.\n\n\tEjemplo:\n\t'5x' es invalido '5*x es correcto'\n\n>>Cuando utilizas fn(), es importante escribir la expresión entre comillas 'x+3' y las variables entre llaves y con comillas {'x':5, 'y':3, 'z':7}\n\n")
      return calculadora()
    if operacion == "funciones":
      print("\nFunciones validas:", *dic_operaciones.keys())
      print("\n\nInstrucciones:\n\n>>Al usar una funcion valida debes utilizar parentesis para escribir la variable. \n\n\tEjemplo:\n\t>> sin(5), log(3), sqrt(9).\n\n>>Hay algunas funciones validas que requieren dos variables. \n\n\tEjemplo:\n\tpow(2,2).\n\n>>La calculadora utiliza la libreria matematica de python, si quieres mas detalles sobre una funcion los puedes encontrar aqui: https://docs.python.org/3/library/math.html \n\n")
      return calculadora()
    if operacion == "constantes":
      print("\nConstantes:", *dic_mathNums.keys())
      print("\n\nInstrucciones:\n\n>>Se utilizan como cualquier otro numero, no requieren parentesis. \n\n\tEjemplo:\n\t>> pi*3/e\n\n")
      return calculadora()
    resultado = eval(operacion, dic_operaciones)
    print(f"Resultado: {resultado}\n\n")
    return calculadora()
  except Exception as error:
    print("Error:",error)
    return calculadora()

calculadora()

