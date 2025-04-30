# Criando validadores

def cpf_invalido(cpf):
    return len(cpf) != 11 or not cpf.isdigit()

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    return len(celular) != 13 or not celular.isdigit()