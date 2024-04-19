import math



def calculadoraCientifica():

  dic_math = {nombre: getattr(math, nombre) for nombre in dir(math) if nombre[0] != "_"}
  dic_operaciones = {nombre: getattr(math, nombre) for nombre in dir(math) if nombre[0] != "_" and callable(getattr(math, nombre))}
  dic_mathNums = {nombre: getattr(math, nombre) for nombre in dir(math) if nombre == "pi" or nombre == "e" or nombre == "tau" }


  print("")
  print("Comandos:")
  print("help")
  print("exit")
  print("")

  try:
    operacion = input("Input: ")
    if operacion == "exit":
      return print("Fin del programa")
    if operacion == "help":
      print("")
      print("Funciones validas:", *dic_operaciones.keys())
      print("")
      print("Numeros matematicos:", *dic_mathNums.keys())
      print("")
      print("Escribe la operacion en una linea. Puedes anidar operaciones utilizando parenstesis (). e.g. Input: ((pi*3)**2)/2")
      print("Al usar una funcion valida debes utilizar parentesis para escribir la variable. e.g. Input: sin(5), log(3), sqrt(9).")
      print("Los numeros matematicos no requieren parentesis. e.g. Input: pi*3")
      print("Hay algunas funciones validas que requieren dos variables. e.g. pow(2,2).")
      print("Precionando la flecha hacia arriba en tu teclado, puedes recuperar el input anterior")
      print("La calculadora utiliza la libreria matematica de python, si quieres mas detalles sobre una funcion los puedes encontrar aqui: https://docs.python.org/3/library/math.html")
      print("")
      return calculadoraCientifica()
    resultado = eval(operacion, dic_math)
    print(f"Resultado: {resultado}")
    print("")
    return calculadoraCientifica()
  except Exception as error:
    print("Error:",error)
    return calculadoraCientifica()

calculadoraCientifica()