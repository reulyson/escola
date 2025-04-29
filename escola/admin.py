from django.contrib import admin
from escola.models import Estudante, Curso, Matricula

''' Admin para estudantes '''
class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular') # Campos a serem exibidos
    list_display_links = ('id', 'nome',) # Campos que podem ser clicados
    list_per_page = 20 # Total de registros por pagina
    search_fields = ('nome',) # Campo de busca por nome

# Registra os modelos no admin 
admin.site.register(Estudante, Estudantes)

''' Admin para cursos '''
class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo',)
    search_fields = ('codigo',)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'periodo', 'estudante', 'curso')
    list_display_links = ('id','periodo')

admin.site.register(Matricula, Matriculas)