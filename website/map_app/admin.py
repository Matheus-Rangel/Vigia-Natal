from django.contrib import admin
from map_app.models import Instituicao, Despesa, Orgao, Localizacao
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.
class DespesaAdmin(admin.ModelAdmin):
    search_field = ['orgao']
    list_filter = [('data_inicio',DateRangeFilter), ('orgao', admin.RelatedOnlyFieldListFilter),]

# class LocalizacaoAdmin(admin.ModelAdmin):
#     list_fil

admin.site.register(Despesa, DespesaAdmin)
admin.site.register(Orgao)
admin.site.register(Instituicao)
admin.site.register(Localizacao)
