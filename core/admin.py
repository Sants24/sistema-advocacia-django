from django.contrib import admin
from .models import Cliente, ModeloDocumento, Documento


admin.site.register(Cliente)
admin.site.register(ModeloDocumento)
admin.site.register(Documento)