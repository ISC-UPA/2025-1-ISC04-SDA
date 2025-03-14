from datetime import date  # Para manejar fechas

class Persona:
    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
    
    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}, Fecha Nacimiento: {self.fecha_nacimiento}')

class Estudiante(Persona):
    counter = 0
    def __init__(self, nombre, fecha_nacimiento, carrera):
        super().__init__(nombre, fecha_nacimiento)
        self.carrera = carrera
        Estudiante.counter += 1
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f'Carrera: {self.carrera}')

    def __pareja(self):
        return ("Adivina Adivinanza")        

class Asignatura:
    def sueldo(self, horas):
        self.horas = horas

class PTC:
    def sueldo(self, horas):
        self.horas = 40

class Profesor(Persona):
    def __init__(self, nombre, fecha_nacimiento, materia, controller):
        super().__init__(nombre, fecha_nacimiento)
        self.materia = materia
        self.controller = controller
        self.horas = 0

    def horas(self, horas):
        self.controller.sueldo(horas)

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f'Materia: {self.materia}')


class ProfesorTitular(Profesor):
    def __init__(self, nombre, fecha_nacimiento, materia, departamento):
        super().__init__(nombre, fecha_nacimiento, materia)
        self.departamento = departamento
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f'Departamento: {self.departamento}')

    def __str__(self):
        return ("{" + "Nombre:" + self.nombre + ", " 
                    + "fecha:"  + str(self.fecha_nacimiento) + ", "
                    + "materia:" + self.materia + ", "
                    + "departamento:" + self.departamento 
                    + "}")        

def printBases(cls):    # Indica la clase padre, (Muestra la Herencia)
    print('( ', end='')
    for x in cls.__bases__: # 
        print(x.__name__, end=' ')
    print(')')


# Ejemplo de uso
estudiante = Estudiante('Pepito', date(2005, 5, 23), 'ISC')
estudiantes = []
estudiantes.append(Estudiante("Ana López", date(1985, 12, 15), "MTR"))
estudiantes.append(Estudiante("Pedro Infante", date(1970, 3, 3), "ELE"))

profesorA = Profesor('Candido Pérez', date(1980,5, 25) , 'Estructuras de Datos', Asignatura())
profesorA.horas(20)
profesorPTC = Profesor('Carmen Salinas', date(1975, 7, 15), 'Cálculo Diferencial', PTC())


#profesor_titular = ProfesorTitular('Gutierritos', date(1970, 10, 1), 'Inteligencia Artificial', 60, 'ISC')
'''
print("Datos del Estudiante:")
estudiante.mostrar_datos()
print("\nDatos del Profesor:")
profesor.mostrar_datos()
print("\nDatos del Profesor Titular:")
profesor_titular.mostrar_datos()
print(profesor_titular)

print("Clase: ", type(profesor_titular).__name__)     # type(obj) es la clase a la que pertenece el objet
print("Clase: ", profesor_titular.__class__.__name__)

print("Herencia: ", ProfesorTitular.__bases__)
printBases(ProfesorTitular) # Muestra la Herencia

print("dict: ", profesor_titular.__dict__) 
print("str:  ", profesor_titular)

print("nombre:", profesor_titular.nombre)
print("nombre:", getattr(profesor_titular, 'nombre'))

print("pareja: ", estudiante._Estudiante__pareja()) # método oculto

print("Modulos")
print(ProfesorTitular.__module__)  # __main__ 
print(profesor_titular.__module__) # __main__

texto3=""
texto1= "UPA"
texto2= "UPA"
texto3 += texto1 
print(texto1 is texto3) # True
print(texto1 == texto3) # True
'''