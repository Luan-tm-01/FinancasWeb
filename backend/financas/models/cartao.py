from .base_model import *
from django.core.validators import MaxValueValidator, MinValueValidator

class Cartao(BaseModel):
    banco = models.CharField(max_length=150)
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento_fatura = models.IntegerField(validators=[MaxValueValidator(30), MinValueValidator(1)])
    melhor_dia = models.IntegerField(validators=[MaxValueValidator(30), MinValueValidator(1)])

    class Meta:
        verbose_name_plural = "Cartões"

    def __str__(self):
        return f'{self.banco}'
    