from django.db import models
# Importamos o Cliente do outro app
from core.models import Cliente

class Honorario(models.Model):
    # Baseado na entidade Honorário [cite: 54, 59]
    STATUS_CHOICES = [
        ('PEN', 'Pendente'),
        ('PAG', 'Pago'),
        ('CAN', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='honorarios')
    descricao = models.CharField(max_length=200, help_text="Ex: Honorários da Causa Trabalhista")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"