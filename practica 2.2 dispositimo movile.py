class Vehiculo:
  """
  Clase base para representar un vehículo genérico.
  """

  def __init__(self, marca, modelo, color):
    """
    Constructor de la clase Vehículo.

    Parámetros:
      marca (str): Marca del vehículo.
      modelo (str): Modelo del vehículo.
      color (str): Color del vehículo.
    """
    self.marca = marca
    self.modelo = modelo
    self.color = color

  def arrancar(self):
    """
    Simula el arranque del vehículo.
    """
    print(f"El vehículo {self.marca} {self.modelo} está arrancando...")

  def detener(self):
    """
    Simula la detención del vehículo.
    """
    print(f"El vehículo {self.marca} {self.modelo} se está deteniendo...")

class Coche(Vehiculo):
  """
  Clase que representa un coche heredando de la clase Vehículo.
  """

  def __init__(self, marca, modelo, color, num_puertas):
    """
    Constructor de la clase Coche.

    Parámetros:
      marca (str): Marca del vehículo.
      modelo (str): Modelo del vehículo.
      color (str): Color del vehículo.
      num_puertas (int): Número de puertas del coche.
    """
    super().__init__(marca, modelo, color)
    self.num_puertas = num_puertas

  def abrir_capota(self):
    """
    Simula la apertura de la capota del coche.
    """
    print(f"Se está abriendo la capota del {self.marca} {self.modelo}")

class Moto(Vehiculo):
  """
  Clase que representa una moto heredando de la clase Vehículo.
  """

  def __init__(self, marca, modelo, color, cilindrada):
    """
    Constructor de la clase Moto.

    Parámetros:
      marca (str): Marca del vehículo.
      modelo (str): Modelo del vehículo.
      color (str): Color del vehículo.
      cilindrada (int): Cilindrada de la moto en cc.
    """
    super().__init__(marca, modelo, color)
    self.cilindrada = cilindrada

  def poner_cascos(self):
    """
    Simula la acción de ponerse el casco.
    """
    print(f"Se están poniendo los cascos para usar la moto {self.marca} {self.modelo}")

# Creando objetos
coche1 = Coche("Toyota", "Corolla", "Azul", 4)
coche2 = Coche("Audi", "A4", "Negro", 2)
moto1 = Moto("Honda", "CBX", "Rojo", 250)
moto2 = Moto("Yamaha", "R6", "Amarillo", 600)

# Utilizando los métodos de las clases
coche1.arrancar()
coche2.abrir_capota()
moto1.poner_cascos()
moto2.detener()