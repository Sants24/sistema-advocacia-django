from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    # Dados baseados na seção 6.2 do documento [cite: 63-71]
    ESTADO_CIVIL_CHOICES = [
        ('S', 'Solteiro(a)'),
        ('C', 'Casado(a)'),
        ('D', 'Divorciado(a)'),
        ('V', 'Viúvo(a)'),
    ]

    nome_completo = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=20, unique=True, verbose_name="CPF/CNPJ")
    rg = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(verbose_name="Endereço Completo")
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)
    profissao = models.CharField(max_length=100)
    contato = models.CharField(max_length=100, help_text="Email ou Telefone")
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_completo

class ModeloDocumento(models.Model):
    # Entidade citada na seção 6.1 (Diagrama ER) [cite: 53, 58]
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    arquivo_template = models.FileField(upload_to='templates_docs/', help_text="Arquivo .docx base com as tags {{nome}}, etc.")
    
    def __str__(self):
        return self.titulo

class Documento(models.Model):
    # Dados baseados na Tabela Documento [cite: 72-77]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='documentos')
    modelo = models.ForeignKey(ModeloDocumento, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=50, help_text="Ex: Procuração, Contrato")
    arquivo_gerado = models.FileField(upload_to='documentos_gerados/')
    data_geracao = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT) # Segurança: saber quem gerou [cite: 57]

    def __str__(self):
        return f"{self.tipo} - {self.cliente.nome_completo}"