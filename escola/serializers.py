from escola.models import Estudante, Curso, Matricula
from rest_framework import serializers
from escola.validators import cpf_invalido, nome_invalido, celular_invalido


class EstudanteSerializer(serializers.ModelSerializer):
    '''
    Serializer para o modelo Estudante.

    Campos incluídos:
    - id
    - nome
    - email
    - cpf
    - data_nascimento
    - celular

    Validações aplicadas:
    - nome: verifica se contém apenas letras
    - cpf: verifica se o CPF é válido
    - celular: verifica se segue o formato correto (99 99999-9999)
    '''
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate(self, dados):
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome dever conter apenas letras.'})
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter um valor válido.'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'Celular precisa seguir o modelo: 99 99999-9999'})
        return dados
    
    # Validação única
    # def validate_nome(self, nome):
    #   if not nome.isalpha():
    #       raise serializers.ValidationError('O nome deve conter apenas letras.')
    #   return nome

class CursoSerializer(serializers.ModelSerializer):
    '''
    Serializer para o modelo Curso.

    Inclui todos os campos definidos no modelo.
    '''
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    '''
    Serializer para o modelo Matriculas.

    Inclui todos os campos definidos no modelo.
    '''
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudantesSerializer(serializers.ModelSerializer):
    '''
    Serializer para exibir as matrículas de um estudante.

    Campos:
    - curso: descrição do curso (read-only)
    - periodo: valor legível do período (via método)
    '''
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    '''
    Serializer para exibir os nomes dos estudantes matriculados em um curso.

    Campos:
    - estudante_nome: nome do estudante (read-only)
    '''
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')

    class Meta:
        model = Matricula
        fields = ['estudante_nome']

class EstudanteSerializerV2(serializers.ModelSerializer):
    '''
     Versão simplificada do serializer de Estudante.

    Campos incluídos:
    - id
    - nome
    - email
    - celular
    '''
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'celular']