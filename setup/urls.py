from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante,ListaMatriculaCurso
from rest_framework import routers

router = routers.DefaultRouter() # Determina um objeto que será da classe DefaultRouter
router.register('estudantes', EstudanteViewSet, basename='Estudantes') # Registra a rota estudante
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), # Incluimos todas as rotas registradas no caminho
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()),  # Rota para listar matrículas de um estudante
    path('cursos/<int:pk>/matriculas/', ListaMatriculaCurso.as_view()),
]