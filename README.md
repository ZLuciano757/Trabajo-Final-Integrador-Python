# Trabajo Final Integrador - Laboratorio de Python

## Sistema elegido

Simulador de cajero automatico.

## Integrantes

- Thiago Fernandez
- Luciano Emmanuel Gatti Flekenstein
- Guadalupe Maria Itati Hofstetter
- Yeny Elisa Velazquez
- Luciano Miqueas Gaspar Zamparo

## Comision

Completar con la comision correspondiente.

## Descripcion general del sistema

El sistema simula operaciones basicas de un cajero automatico ejecutado por consola. Permite iniciar sesion con usuario y contrasena, consultar saldo, extraer dinero, depositar dinero, realizar transferencias simples entre usuarios, ver el registro de operaciones realizadas y consultar estadisticas basicas.

El programa incluye validaciones para evitar montos incorrectos, operaciones con saldo insuficiente, extracciones por encima del limite permitido, transferencias a cuentas inexistentes y errores al ingresar datos no numericos.

## Usuarios de prueba

| Usuario | Contrasena | Saldo inicial |
| --- | --- | --- |
| admin | 1234 | $100000 |
| juan | 4321 | $75000 |
| maria | 1111 | $120000 |

## Funcionalidades

- Validacion de acceso mediante usuario y contrasena.
- Consulta de saldo.
- Extraccion de dinero con limite por operacion.
- Deposito de dinero.
- Transferencia de dinero entre cuentas.
- Control de saldo insuficiente.
- Registro de operaciones realizadas.
- Estadisticas basicas con contadores y acumuladores.
- Manejo basico de errores al ingresar opciones o montos invalidos.

## Requisitos tecnicos aplicados

- Estructuras condicionales: se utilizan para validar opciones, montos, saldo disponible y usuarios.
- Estructuras repetitivas: se utilizan en el menu principal, en el ingreso de opciones y en el ingreso de montos.
- Funciones: el sistema esta dividido en funciones para organizar las responsabilidades.
- Validaciones: se validan credenciales, montos, opciones del menu, saldo y cuentas destino.
- Acumuladores y contadores: se registran cantidades de operaciones y montos totales.
- Modularizacion basica: cada operacion principal del cajero esta separada en una funcion.
- Manejo basico de errores: se usa try/except para evitar errores cuando se ingresan letras en campos numericos.

## Instrucciones de ejecucion

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el programa con:

bash
python main.py


Si el sistema usa Python 3 con otro comando, ejecutar:

bash
python3 main.py


## Caso de prueba valido

1. Ingresar usuario: admin.
2. Ingresar contrasena: 1234.
3. Elegir opcion 1 para consultar saldo.
4. Elegir opcion 3 y depositar 5000.
5. Elegir opcion 2 y extraer 2000.
6. Elegir opcion 4, transferir a juan y colocar monto 1000.
7. Elegir opcion 5 para ver operaciones.
8. Elegir opcion 6 para ver estadisticas.
9. Elegir opcion 7 para salir.

## Caso de prueba con validaciones

- Intentar ingresar una opcion con letras, por ejemplo abc.
- Intentar extraer un monto mayor al saldo disponible.
- Intentar extraer mas de $50000.
- Intentar transferir a un usuario inexistente.
- Intentar depositar un monto negativo.

## Uso de Inteligencia Artificial

Se utilizo una herramienta de Inteligencia Artificial como apoyo para generar una estructura inicial del codigo, organizar las funciones, proponer validaciones y redactar el README. El grupo reviso y adapto la solucion para comprender el funcionamiento general del sistema.
