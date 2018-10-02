from django.contrib import admin
from map_app.models import Instituicao, Despesa, Orgao, Localizacao

# Register your models here.
admin.site.register(Despesa)
admin.site.register(Orgao)
admin.site.register(Instituicao)
admin.site.register(Localizacao)
