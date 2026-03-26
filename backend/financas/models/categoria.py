from .base_model import *

class Categoria(BaseModel):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'