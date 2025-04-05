class Room:

        def __init__(self, room_number, room_type, price_per_night, is_available=True):
            self.room_number = room_number
            self.room_type = room_type
            self.price_per_night = price_per_night
            self.is_available = is_available

        def __str__(self):
            availability = "Disponible" if self.is_available else "No disponible"
            return (f"Habitación {self.room_number} | Tipo: {self.room_type} | "
                    f"Precio por noche: ${self.price_per_night} | {availability}")

        def reservar(self):
            if self.is_available:
                self.is_available = False
                print(f"Habitación {self.room_number} reservada.")
            else:
                print(f"Habitación {self.room_number} no está disponible.")

        def liberar(self):
            self.is_available = True
            print(f"Habitación {self.room_number} ahora está disponible.")