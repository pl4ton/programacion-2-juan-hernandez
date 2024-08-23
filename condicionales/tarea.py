class Datos:
    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo 

    def obtener_datos(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'sexo': self.sexo,
        }


try:
    opcion = int(input("Ingrese la edad \n"))

    if opcion > 0 and opcion <= 18:
        print("Es menor de edad")
    else:
        print("Es mayor de edad")    

except ValueError:
    print("Por favor, ingrese un número válido para la edad.")


persona = Datos("Juan", "hernandez", 20, "Masculino")


print(persona.obtener_datos())

