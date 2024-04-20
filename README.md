# Calculadora

Una simple calculadora para utilizar en la consola. Puede realizar todas las operaciones de la libreria math the python y resolver funciones algebraicas.

## Requerimientos

1. Git: Necesitas tener Git instalado en tu sistema para poder clonar el repositorio desde GitHub. Puedes descargar e instalar Git desde el sitio web oficial: https://git-scm.com/.

2. Python: Debes tener Python instalado en tu sistema para poder ejecutar el archivo de Python. Puedes descargar e instalar Python desde el sitio web oficial: https://www.python.org/. Asegúrate de configurar correctamente la variable de entorno PATH durante la instalación para que puedas ejecutar el comando python desde cualquier ubicación en tu terminal.

## Clonar el repositorio

1. Abre tu terminal y utiliza el comando git clone seguido de la URL del repositorio de GitHub para clonar el repositorio en tu máquina local. Por ejemplo:

```bash
git clone https://github.com/0xalbatros/calculadora.git
```

2. Navegar al directorio del repositorio: Utiliza el comando cd para cambiar al directorio del repositorio que acabas de clonar. Por ejemplo:

```bash
cd calculadora
```

3.Ejecutar el archivo de Python: Una vez en el directorio del repositorio, ejecuta el archivo de Python utilizando el intérprete de Python. Por ejemplo, si el archivo se llama script.py, puedes ejecutarlo con el siguiente comando:

```bash
python calculadora.py
```

## Uso

1. Abre la consola y navega hasta la ubicación del archivo `calculadora.py`.
2. Ejecuta el siguiente comando para iniciar la calculadora:

```bash
python calculadora.py
```

Asegurate de escribir el comando desde la ubicacion del archivo.

Si se ejecuto correctamente te aparecera algo asi:

```bash
Comandos:
operacion
algebra
funciones
constantes
exit


Input:
```

Ahora solo tienes que ingresar las operaciones que desees y presionar enter para obtener el resultado.

Ejemplo:

```bash
Input: (pi*3)*cos(4)/sin(2)
Resultado: -6.774951528916912
```

La calculadora tiene una lista de comandos que puedes utilizar para obtener mayor informacion de como utilizar cada funcion.

Puedes realizar operaciones algebraicas y asignarle valores a variables

Ejemplo:

```bash
Input: fn('x**2+2*y+5', {'x':3, 'y':5})
Resultado: 24
```
Reutilizar los valores de 'x' y 'y'

```bash
Input: 8*x + y**2
Resultado: 49
```
Donde conservaran los valores asignados en el input anterior

Puedes ver mas detalles de uso con con el menu de comandos, solo escribe lo que te interese ver.

Ejemplo:

```bash
Comandos:
operacion
algebra
funciones
constantes
exit


Input:funciones

Funciones validas: acos acosh asin asinh atan atan2 atanh cbrt ceil comb copysign cos cosh degrees dist erf erfc exp exp2 expm1 fabs factorial floor fmod frexp fsum gamma gcd hypot isclose isfinite isinf isnan isqrt lcm ldexp lgamma log log10 log1p log2 modf nextafter perm pow prod radians remainder sin sinh sqrt sumprod tan tanh trunc ulp e pi tau fn __builtins__ x y


Instrucciones:

>>Al usar una funcion valida debes utilizar parentesis para escribir la variable.

        Ejemplo:
        Input: sin(5), log(3), sqrt(9).

>>Hay algunas funciones validas que requieren dos variables.

        Ejemplo:
        pow(2,2).

>>La calculadora utiliza la libreria matematica de python, si quieres mas detalles sobre una funcion los puedes encontrar aqui: https://docs.python.org/3/library/math.html
```

Para salir del archivo solo escribe exit

```bash
Input: exit
Fin del programa
```

La consola es sensible a los espacios asi que asegurate de siempre escribir exactamente el comando que deseas sin espacios adicionales, y respetando comillas, parentesis, letras, etc.

Gracias por utilizar la calculadora. 