from django.contrib import admin
from .models import *

class detUsuarios(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'fone', 'ativo')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Usuarios, detUsuarios)


class detMaterias(admin.ModelAdmin):
    list_display = ('id','nome', 'ativo')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Materias, detMaterias)