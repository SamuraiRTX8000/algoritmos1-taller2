
notas = float(input("ingrese la nota del estudiante")) 
aprobados = 0
reprobados = 0
contador = 0.0
acumulador = 0
if notas >= 1.0 and notas <= 5.0:
    while notas >= 1.0 and notas <= 5.0:
        contador += 1
        acumulador += notas
        if notas >= 3.0:
            aprobados += 1 
        else:
            reprobados += 1 
            
        notas = float(input("ingresa la nota"))
         
            
else:
    print("nota no valida")
promedio = (acumulador/contador)
print(f"resumen: Estudiantes. {contador} aprobados: {aprobados} numero de reprobados{reprobados}  promedio general {promedio}")