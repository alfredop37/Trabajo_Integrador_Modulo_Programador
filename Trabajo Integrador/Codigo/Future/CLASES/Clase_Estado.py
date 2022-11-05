class Estado:
    
    Nombre_Estado = ""
    
    def __init__(self, Nombre_Estado):
        self.Nombre_Estado = Nombre_Estado
        
    
    def get_Nombre_Estado(self):
        return self.Nombre_Estado
    
    
    def set_Nombre_Estado(self, Nombre_Estado):
        self.Nombre_Estado = Nombre_Estado
        
    
    def _str_(self):
       print('Nombre_Estado: '+self.Nombre_Estado)