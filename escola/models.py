from django.db import models
from django.core.validators import MinLengthValidator

''' Modelo com os campos da tabela estudante '''
class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)

    # Retorna o nome do estudante quando for chamado
    def __str__(self):
        return self.nome

''' Modelo com os campos da tabela cursos '''
class Curso(models.Model):

    # Tupla com os niveis de cursos
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )

    # validando o valor de código como valor único e com 3 dígitos no minimo
    codigo = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(3)])
    descricao = models.CharField(max_length=100, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.codigo
    
''' Modelo com os campos da tabela matricula '''
class Matricula(models.Model):

    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )

    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE) # Referencia ao estudante e apaga os dados quando o estudante for apagado
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE) # Referencia ao curso e apaga os dados quando o curso for apagado
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')