import re
from validate_docbr import CPF

def cpf_invalido(numero_cpf):
    '''
    Valida se um número de CPF é inválido.

    Utiliza a biblioteca `validate-docbr` para verificar a validade do CPF.

    Parâmetros:
    - numero_cpf (str): CPF a ser validado, como string.

    Retorno:
    - bool: True se o CPF for inválido, False se for válido.
    '''
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def nome_invalido(nome):
    '''
    Verifica se o nome contém apenas letras.

    Parâmetros:
    - nome (str): nome a ser validado.

    Retorno:
    - bool: True se o nome for inválido (ou seja, contiver números ou caracteres especiais), False se for válido.
    '''
    return not nome.isalpha()

def celular_invalido(celular):
    '''
    Verifica se o número de celular está no formato correto: 99 99999-9999.

    Utiliza uma expressão regular para checar o padrão.

    Parâmetros:
    - celular (str): número de celular a ser validado.

    Retorno:
    - bool: True se o celular for inválido, False se estiver no padrão correto.
    '''
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return not resposta