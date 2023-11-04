import os
# Solicitar al usuario el nombre del estudiante y sus notas
nombre_estudiante = (input("Ingrese el nombre del estudiante: "))
notas = []
for i in range(4):
    nota = int(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

# Calcular el promedio
promedio = (nota+ nota + nota + nota) / 4
print("promedio: ", promedio)
# Guardar los datos en el archivo "notas.txt"
with open("C:/Users/ACER/Downloads/Examen Final Algoritmos/examen_final_algoritmos/notas.txt"):
    os.write(f"Nombre del estudiante: ", {nombre_estudiante})
    os.write(f"Notas: " ,", ".join(map(int, notas)), "\n")
    os.write(f"Promedio:", {promedio}, "\n")
    os.save(f"C:/Users/ACER/Downloads/Examen Final Algoritmos/examen_final_algoritmos/notas.txt")
