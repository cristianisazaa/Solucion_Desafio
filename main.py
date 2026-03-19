from dataclasses import replace

print("Por favor ingrese su primer calificación")
calificacion1 = input()
calificacion1 = float(calificacion1.replace(",","."))
if (calificacion1 > 100) or (calificacion1 < 0):
    print("Recuerde que los valores validos de las calificaciones"
          "son entre 0 y 100")
    print("Ingrese nuevamente su primer calificación")
    calificacion1=input()
    calificacion1 = float(calificacion1.replace(",", "."))


print("Por favor ingrese su segunda calificación")
calificacion2 = input()
calificacion2 = float(calificacion2.replace(",","."))
if (calificacion2 > 100) or (calificacion2 < 0):
    print("Recuerde que los valores validos de las calificaciones"
          "son entre 0 y 100")
    print("Ingrese nuevamente su segunda calificación")
    calificacion2 = input()
    calificacion2 = float(calificacion2.replace(",", "."))

print("Por favor ingrese su tercer calificación")
calificacion3 = input()
calificacion3 = float(calificacion3.replace(",","."))
if (calificacion3 > 100) or (calificacion3 < 0):
    print("Recuerde que los valores validos de las calificaciones"
          "son entre 0 y 100")
    print("Ingrese nuevamente su tercer calificación")
    calificacion3 = input()
    calificacion3 = float(calificacion3.replace(",", "."))

print("Por favor ingrese su cuarta calificación")
calificacion4 = input()
calificacion4 = float(calificacion4.replace(",","."))
if (calificacion4 > 100) or (calificacion4 < 0):
    print("Recuerde que los valores validos de las calificaciones"
          "son entre 0 y 100")
    print("Ingrese nuevamente su cuarta calificación")
    calificacion4 = input()
    calificacion4 = float(calificacion4.replace(",", "."))

print("Por favor ingrese su quinta calificación")
calificacion5 = (input())
calificacion5 = float(calificacion5.replace(",","."))
if (calificacion5 > 100) or (calificacion5 < 0):
    print("Recuerde que los valores validos de las calificaciones"
          "son entre 0 y 100")
    print("Ingrese nuevamente su quinta calificación")
    calificacion5 = input()
    calificacion5 = float(calificacion5.replace(",", "."))

promedio = (calificacion1+calificacion2+calificacion3+calificacion4+calificacion5)/5

if promedio >= 60.0:
    print("Aprobado")
else:
    if promedio < 40.0:
        print("Reprovado")

    else:
        if 60.0 < promedio >= 40.0 :
            print("En recuperacion")


