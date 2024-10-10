class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas, es_automatico):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        self.es_automatico = es_automatico

    def mostrar_informacion(self):
        automatico_texto = "Automático" if self.es_automatico else "Manual"
        return f"{super().mostrar_informacion()}, Puertas: {self.numero_puertas}, Transmisión: {automatico_texto}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje, tipo):
        super().__init__(marca, modelo, año)
        self.cilindraje = cilindraje
        self.tipo = tipo

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Cilindraje: {self.cilindraje} cc, Tipo: {self.tipo}"


def gestion_vehiculos():

    auto1 = Auto("BMW", "Serie 3", 2021, 4, True)
    auto2 = Auto("Bugatti", "Chiron", 2022, 2, True)
    auto3 = Auto("Rolls-Royce", "Phantom", 2020, 4, True)
    
    moto1 = Moto("Honda", "CBR600RR", 2021, 600, "Ninja")
    moto2 = Moto("BMW", "R 1250 GS", 2022, 1250, "Cruiser")
    
    vehiculos = [auto1, auto2, auto3, moto1, moto2]
    
    for vehiculo in vehiculos:
        print(vehiculo.mostrar_informacion())

gestion_vehiculos()

def menu_interactivo():
    vehiculos = [
        Auto("BMW", "Serie 3", 2021, 4, True),
        Auto("Bugatti", "Chiron", 2022, 2, True),
        Auto("Rolls-Royce", "Phantom", 2020, 4, True),
        Moto("Honda", "CBR600RR", 2021, 600, "Ninja"),
        Moto("BMW", "R 1250 GS", 2022, 1250, "Cruiser")
    ]
    
    while True:
        print("\n--- Sistema de Gestión de Vehículos ---")
        print("\n--- =============================== ---")
        print("1 -> Ingresar nuevo vehículo")
        print("2 -> Mostrar lista de vehículos")
        print("3 -> Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":

            tipo_vehiculo = input("Ingrese el tipo de vehículo (Auto/Moto): ").lower()
            
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            año = int(input("Año: "))
            
            if tipo_vehiculo == "auto":
                numero_puertas = int(input("Número de puertas: "))
                es_automatico = input("¿Es automático? (si/no): ").lower() == "si"
                vehiculo = Auto(marca, modelo, año, numero_puertas, es_automatico)

            elif tipo_vehiculo == "moto":
                cilindraje = int(input("Cilindraje: "))
                tipo = input("Tipo (Ninja, Cruiser, etc.): ")
                vehiculo = Moto(marca, modelo, año, cilindraje, tipo)
                
            else:
                print("Tipo de vehículo no válido. Inténtelo de nuevo.")
                continue
            
            vehiculos.append(vehiculo)
            print(f"{tipo_vehiculo.capitalize()} ingresado correctamente.")
        
        elif opcion == "2":

            if not vehiculos:
                print("Lista vacía.")
            else:
                print("\n--- Lista de Vehículos ---")
                print("\n--- ================== ---")
                for vehiculo in vehiculos:
                    print(vehiculo.mostrar_informacion())
        
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Inténtelo de nuevo.")

menu_interactivo()
