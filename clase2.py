materias = []
for i in range (2):
    materias.append(input("materia"))
    print("--------------------------------------------")
for materia in materias : 
    print("yo estudio:",materia)
    print("--------------------------------------------")
notas = {}
for materia in materias:
    nota = input("Digite su nota" + materia + "?")
    notas[materia] = nota
    print("--------------------------------------------")
for materia,nota in notas.items():
    print("-tu nota es:"  ,  materia  ,  "es"  ,  nota)
    print("--------------------------------------------")
    repetir = []
for materia,nota in notas.items():
    if float(nota)<65:
        repetir.append(materia)
for materia in repetir:
    materias.remove(materia)
    if repetir:
     print("Lo sentimos has reprovado:" , materia)
     print("--------------------------------------------")