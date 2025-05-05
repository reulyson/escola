from django.db import models
from django.core.validators import MinLengthValidator

class Estudante(models.Model):
    '''
    Modelo que representa um estudante.

    Campos:
    - nome: Nome completo do estudante.
    - email: Email de contato.
    - cpf: CPF único do estudante (11 dígitos).
    - data_nascimento: Data de nascimento.
    - celular: Número de celular no formato '99 99999-9999'
    '''
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    '''
    Modelo que representa um curso disponível.

    Campos:
    - codigo: Código único do curso (mínimo 3 caracteres).
    - descricao: Descrição do curso.
    - nivel: Nível do curso (Básico, Intermediário ou Avançado).
    '''

    # Tupla com os niveis de cursos
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )

    codigo = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(3)])
    descricao = models.CharField(max_length=100, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.codigo

class Matricula(models.Model):
    '''
    Modelo que representa a matrícula de um estudante em um curso.

    Campos:
    - estudante: Referência ao estudante matriculado.
    - curso: Referência ao curso no qual o estudante está matriculado.
    - periodo: Período da aula (Matutino, Vespertino ou Noturno).
    """
    '''

    # tupla com os períodos
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )

    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE) # CASCADE indica que quando um aluno for exluido sua matricula também é.
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')