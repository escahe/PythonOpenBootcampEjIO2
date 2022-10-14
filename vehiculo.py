class Vehiculo:
    marca,referencia,color ="","",""
    def __init__(self,marca,referencia,color):
        self.marca = marca
        self.referencia = referencia
        self.color = color
    
    def __repr__(self) -> str:
        return f"{self.marca}{self.referencia}{self.color}"
    
    def __str__(self) -> str:
        return f"Soy un {self.marca} {self.referencia} de color {self.color}"