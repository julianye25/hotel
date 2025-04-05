import User
from datetime import datetime

class Empleado(User):
    def __init__(self, id, name, last_name, phone, email, password, status, cargo, salario):
        super().__init__(id, name, last_name, phone, email, password, status)
        self._cargo = cargo
        self._salario = salario
        self._historial_actividades = []
        self._hora_entrada = None
        self._hora_salida = None
        self._habitaciones_asignadas = []

    # Propiedades cargo y salario
    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    # Registro de turno
    def registrar_entrada(self):
        self._hora_entrada = datetime.now()
        self._historial_actividades.append(f"Entró al turno a las {self._hora_entrada}")
        print(f"{self.name} ha iniciado su turno a las {self._hora_entrada}")

    def registrar_salida(self):
        self._hora_salida = datetime.now()
        self._historial_actividades.append(f"Salió del turno a las {self._hora_salida}")
        print(f"{self.name} ha terminado su turno a las {self._hora_salida}")

    # Actividades
    def agregar_actividad(self, descripcion):
        ahora = datetime.now()
        self._historial_actividades.append(f"[{ahora}] {descripcion}")

    def ver_historial(self):
        print(f"Historial de {self.name} {self.last_name}:")
        for actividad in self._historial_actividades:
            print(f" - {actividad}")

    # Gestión de habitaciones asignadas
    def asignar_habitacion(self, room_number):
        if room_number not in self._habitaciones_asignadas:
            self._habitaciones_asignadas.append(room_number)
            self.agregar_actividad(f"Habitación {room_number} asignada.")
        else:
            print(f"Habitación {room_number} ya está asignada.")

    def listar_habitaciones_asignadas(self):
        return self._habitaciones_asignadas

    # Cambiar estado
    def actualizar_estado(self, nuevo_estado):
        self.status = nuevo_estado
        self.agregar_actividad(f"Estado actualizado a '{nuevo_estado}'.")

    # Cambiar contraseña
    def cambiar_contrasena(self, nueva_password):
        self.password = nueva_password
        self.agregar_actividad("Contraseña actualizada.")

    def __str__(self):
        return (f"Empleado: {self.name} {self.last_name} | Cargo: {self.cargo} | "
                f"Salario: ${self.salario} | Estado: {self.status} | Email: {self.email}")
