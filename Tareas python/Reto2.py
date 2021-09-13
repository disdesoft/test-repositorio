print("\n====================")
print("PROMEDIO NOTAS UNAB")
print("====================\n")

print('Ingrese Nombre del Alumno:')
nombre = input()

print('Hola ', nombre,)

print('Ingrese nota de ingles: ')
ingles = float(input(''))

print('Ingrese nota de coaching: ')
coaching = float(input(''))

print('Ingrese nota de Fundamentos de Programación: ')
fundpro = float(input(''))

print('Ingrese nota de python: ')
python = float(input(''))

if ingles >= 3.5:
    print('aprobó la asignatura de ingles')
else:
    print('No aprobó la asignatura de ingles')

if coaching >= 3.5:
    print('aprobó la asignatura de coaching')
else:
    print('No aprobó la asignatura de coaching')

if fundpro >= 3.5:
    print('aprobó la asignatura de Fundamentos de programación')
else:
    print('No aprobó la asignatura de Fundamentos de programación')

if python >= 3.5:
    print('aprobó la asignatura de python')
else:
    print('No aprobó la asignatura de python')

aprobar = ingles*0.2 + coaching*0.2 + fundpro*0.25 + python*0.35

if aprobar >= 3.5:
    print ('FELICITACIONES!!! ', nombre, ' Aprobaste el curso de Desarrollo de aplicaciones moviles y paginas web')
else:
    print (nombre, 'lamentablemente no aprobaste el curso de Desarrollo de aplicaciones moviles y paginas web')