from .base_model import *
from django.contrib.auth.models import User

class TransacaoRecebimento(BaseModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Transações | Recebimentos"

    def __str__(self):
        return f'Recebeu R${self.valor} no Dia {self.data}'