from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudantesSerializer, EstudanteSerializerV2
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework import viewsets, generics, filters
from rest_framework.throttling import UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EstudanteViewSet(viewsets.ModelViewSet):
    '''
    Descrição da ViewSet:
    - Endpoint para CRUD de estudantes.

    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.

    Campos de pesquisa:
    - nome: permite pesquisar o resultado por nome.
    - cpf: permite pesquisar os resultados por CPF.

    Métodos HTTP Permitidos:
    - GET, POST, PATCH, DELETE

    Classe de Serializer:
    - EstudanteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa EstudanteSerializerV2.
    '''

    # authentication_classes = [BasicAuthentication] # Define que o usuário deve fornecer um nome de usuário e uma senha para acessar as rotas da API.
    # permission_classes = [IsAuthenticated] # Define que apenas usuários autenticados possam acessar
    queryset = Estudante.objects.all().order_by('id')
    # serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    '''
    Descrição da ViewSet:
    - Endpoint para CRUD de curso.

    Campos de filtragem:
    - nivel: permite filtar os cursos pelo nível.

    Métodos HTTP Permitidos:
    - GET, POST, PATCH, DELETE
    '''

    queryset = Curso.objects.all().order_by('id') 
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nivel']
    permission_classes = [IsAuthenticatedOrReadOnly]

class MatriculaViewSet(viewsets.ModelViewSet):
    '''
    Descrição da ViewSet:
    - Endpoint para CRUD de estudantes.

    Métodos HTTP Permitidos:
    - GET, POST.

    Throttle Classes:
    - MatriculaAnonRateThrottle: Limite de taxa para usuários anônimos
    - UserRateThrottle: Limite de taxa para usuários autenticados.
    '''

    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ['get', 'post',]

class ListaMatriculaEstudante(generics.ListAPIView):
    '''
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parêmetros:
    - pk (int): O indentificador primário do objeto. Deve ser o número inteiro.
    '''

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id') 
        return queryset
    
    serializer_class = ListaMatriculasEstudantesSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    '''
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parêmetros:
    - pk (int): O indentificador primário do objeto. Deve ser o número inteiro.
    '''

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer