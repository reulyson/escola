from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudantesSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

''' ViewSets para visualização dos dados '''
class EstudanteViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication] # Define que o usuário deve fornecer um nome de usuário e uma senha para acessar as rotas da API.
    # permission_classes = [IsAuthenticated] # Define que apenas usuários autenticados possam acessar

    queryset = Estudante.objects.all() # seleciona todos os dados da tabela estudantes
    # serializer_class = EstudanteSerializer # definindo a serialização que será utilizada
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome'] # Permite ordenar pelo campo nome
    search_fields = ['nome', 'cpf'] # Permite buscar nome e cpf

    # Definindo que versão de API será usada
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()    
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nivel']

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudante(generics.ListAPIView):
    # Método que define o queryset a ser retornado
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']) # Filtrando as matrículas para retornar apenas as do estudante específico
        return queryset
    
    serializer_class = ListaMatriculasEstudantesSerializer

class ListaMatriculaCurso(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer