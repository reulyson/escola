from escola.models import Estudante, Curso, Matricula
from rest_framework import serializers
from escola.validators import cpf_invalido, nome_invalido, celular_invalido

''' Serializers para os modelos '''
class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante # passando o modelo
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular'] # passando os campos que serão exibidos
    def validate(self, dados):
        # Validação Nome
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome dever conter apenas letras.'})
        # Validação CPF
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter um valor válido.'})
        # Validação Celular
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'Celular precisa seguir o modelo: 99 99999-9999'})
        return dados
    
    # Validação única
    # def validate_nome(self, nome):
    #   if not nome.isalpha():
    #       raise serializers.ValidationError('O nome deve conter apenas letras.')
    #   return nome

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