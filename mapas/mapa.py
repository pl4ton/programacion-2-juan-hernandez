class Usuario:
    def _init_(self, nombrecompleto, nickname, clave, tipo, fecha_creacion):
        self.datos = {
            'nombrecompleto': nombrecompleto,
            'nickname': nickname,
            'clave': clave,
            'tipo': tipo,
            'fecha_creacion': fecha_creacion
        }
    
    def obtener_datos(self):
        return self.datos


def agregar_usuario(usuarios):
    nombrecompleto = input("Ingrese el nombre completo: ")
    nickname = input("Ingrese el nickname: ")
    clave = input("Ingrese la clave: ")
    tipo = input("Ingrese el tipo de usuario: ")
    fecha_creacion = input("Ingrese la fecha de creación (YYYY-MM-DD): ")
    
    nuevo_usuario = Usuario(nombrecompleto, nickname, clave, tipo, fecha_creacion)
    usuarios[nickname] = nuevo_usuario
    print("Usuario agregado exitosamente.")

def buscar_usuario(usuarios):
    nickname = input("Ingrese el nickname del usuario a buscar: ")
    if nickname in usuarios:
        datos = usuarios[nickname].obtener_datos()
        print("Datos del usuario encontrado:")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario(usuarios):
    nickname = input("Ingrese el nickname del usuario a eliminar: ")
    if nickname in usuarios:
        del usuarios[nickname]
        print("Usuario eliminado exitosamente.")
    else:
        print("Usuario no encontrado.")

def menu():
    usuarios = {}
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar Usuario")
        print("2. Buscar Usuario")
        print("3. Eliminar Usuario")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            agregar_usuario(usuarios)
        elif opcion == '2':
            buscar_usuario(usuarios)
        elif opcion == '3':
            eliminar_usuario(usuarios)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if _nickname_ == "_main_":
    menu()