class Persona:
    def __init__(self, nombre: str, apellido: str, direccion: str, telefono: str, edad: int, email: str):
        self._nombre = nombre
        self._apellido = apellido
        self._direccion = direccion
        self._telefono = telefono
        self._edad = edad
        self._email = email

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def apellido(self) -> str:
        return self._apellido

    @apellido.setter
    def apellido(self, value: str):
        self._apellido = value

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, value: str):
        self._direccion = value

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, value: str):
        self._telefono = value

    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, value: int):
        self._edad = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = value

class Empleado(Persona):
    def __init__(self, nombre: str, apellido: str, direccion: str, telefono: str, edad: int, email: str,
                 salario: float, jefe_inmediato: str, años_experiencia: int):
        super().__init__(nombre, apellido, direccion, telefono, edad, email)
        self._salario = salario
        self._jefe_inmediato = jefe_inmediato
        self._años_experiencia = años_experiencia
        self._cargo = self.calcular_cargo()

    @property
    def salario(self) -> float:
        return self._salario

    @salario.setter
    def salario(self, value: float):
        self._salario = value
        self._cargo = self.calcular_cargo()

    @property
    def jefe_inmediato(self) -> str:
        return self._jefe_inmediato

    @jefe_inmediato.setter
    def jefe_inmediato(self, value: str):
        self._jefe_inmediato = value

    @property
    def años_experiencia(self) -> int:
        return self._años_experiencia

    @años_experiencia.setter
    def años_experiencia(self, value: int):
        self._años_experiencia = value
        self._cargo = self.calcular_cargo()

    @property
    def cargo(self) -> str:
        return self._cargo

    def calcular_cargo(self) -> str:
        if self._salario >= 5000000 and self._años_experiencia >= 5 and 25 <= self.edad <= 45:
            return "Senior"
        elif 900000 <= self._salario <= 1200000 and 1 <= self._años_experiencia <= 2 and 18 <= self.edad <= 22:
            return "Junior"
        else:
            return "No definido"

    def mostrar_detalle(self) -> None:
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Edad: {self.edad}")
        print(f"Email: {self.email}")
        print(f"Salario: {self.salario}")
        print(f"Jefe Inmediato: {self.jefe_inmediato}")
        print(f"Años de Experiencia: {self.años_experiencia}")
        print(f"Cargo: {self.cargo}")

def main():
   
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el teléfono: ")
    edad = int(input("Ingrese la edad: "))
    email = input("Ingrese el email: ")
    salario = float(input("Ingrese el salario: "))
    jefe_inmediato = input("Ingrese el jefe inmediato: ")
    años_experiencia = int(input("Ingrese los años de experiencia: "))

  
    empleado = Empleado(nombre, apellido, direccion, telefono, edad, email, salario, jefe_inmediato, años_experiencia)
    
    
    empleado.mostrar_detalle()

if __name__ == "__main__":
    main()
