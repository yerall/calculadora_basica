
# Descripción

**LA CLASICA CALCULADORA BASICA EN PYTHON**. Permite realizar las operaciones aritméticas básicas de forma interactiva mediante un menú en la consola.

## Requisitos

Este programa solo requiere tener Python 3 instalado.

## Funcionalidades

1. **Suma** - Calcula la suma de dos números.
2. **Resta** - Calcula la diferencia entre dos números.
3. **Multiplicación** - Multiplica dos números.
4. **División** - Realiza la división de dos números y muestra el resultado con decimales. Incluye control para evitar la división por cero.
5. **División Exacta** - Realiza la división entera de dos números, también evitando divisiones por cero.
6. **Exponente** - Calcula la potencia de un número elevado a otro.
7. **Salir del programa** - Permite al usuario salir del programa.

## Estructura del Código

- **Funciones de Operaciones**: Cada operación está implementada en una función separada para una mejor organización y reutilización de código.
- **Control de Errores**: Se verifica que los valores ingresados sean válidos y evita la división por cero.
- **Función `menu_principal()`**: Presenta las opciones al usuario y gestiona la selección.
- **Función `obtener_numeros()`**: Permite solicitar y validar los números de entrada del usuario para cada operación, asegurando que el programa no falle por entradas inválidas.
