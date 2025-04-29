from escola.models import Estudante, Curso, Matricula
from rest_framework import serializers

''' Serializers para os modelos '''
class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante # passando o modelo
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular'] # passando os campos que serão exibidos

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' # passando todos os campos

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] # passando todos os campos

class ListaMatriculasEstudantesSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao') # Definindo o campo como somente leitura para descrição do curso
    periodo = serializers.SerializerMethodField() # Definindo um campo que chama um metodo para obter o periodo de forma legivel

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display() # Chamando o método que retorna o valor legível do período
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome') # Definindo o campo como somente leitura para o nome do estudante

    class Meta:
        model = Matricula
        fields = ['estudante_nome']