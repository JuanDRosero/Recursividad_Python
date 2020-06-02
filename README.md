# Recursividad Operador lambda en Python
## Juan David Rosero Torres 20181020071
##¿Que hace el programa?
El programa es un script en python que permite calcular el valor de las cesantias que tendra una persona, ingresando su salario y la cantidad de meses que desea consultar.
##¿Como lo hace?
Se le pide al usuario el valor del salario (mensual) y la cantidad de meses que lleva trabajando. Luego se le pasan como parametros a valorCesantias, que es una expresión lambda recursiva, en donde se van sumando (llamado a llamado) (100/12) multiplicado por el salario, hasta que llega al mes cero, en donde regresa el cero.
