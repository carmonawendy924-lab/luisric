#agregar estudiante(nombre y calificasion)
#listar todos los estudiantes 
#calcular el promedio general
#identificar al estudiante con la calificasion mas alta

estudiantes=[]

def agregar_estudiante():
    nombre=input("nombre: ")
    calificasion=float(input("calificasion: ")) 
    estudiantes.append((nombre, calificasion))

def lista_estudiantes():
    for nombre,calificasion in estudiantes:
        print(f"{nombre}: {calificasion}")

def calcular_promedio():
    returm sum(calificasion for _, calificasion in estudiantes) len(estudiantes)

def mejor_estudiante():
    max_calificasion=max(calificasion for _, calificasion in estudiantes)
    returm[nombre for nombre,calificasion in estudiantes if calificasion== max_calificasion]