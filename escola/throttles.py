from rest_framework.throttling import AnonRateThrottle

class MatriculaAnonRateThrottle(AnonRateThrottle):
    '''
    Classe de controle de taxa (throttling) para requisições anônimas na view de matrícula.

    Limita o número de requisições que usuários não autenticados podem fazer para 
    a view relacionada a matrícula.

    Configuração:
    - Limite de 5 requisições por dia para usuários anônimos (não autenticados).
    
    Essa classe pode ser usada para evitar abuso de endpoints públicos.
    '''
    rate = '5/day'