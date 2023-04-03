class Jogador:

    def __init__(self, nome, id, posicao):
        self.__nome = nome
        self.__mao_de_cartas = []
        self.__jogou_ultimo_turno = False
        self.__posicao = posicao
        self.__jogador_id = id
        self.__eh_local = False
    




    def get_mao_de_cartas(self):
        return self.__mao_de_cartas
    
    def set_mao_de_cartas(self, baralho):
        self.__mao_de_cartas = baralho

    def get_jogou_ultimo_turno(self):
        return self.__jogou_ultimo_turno


    def comprar_carta(self, carta):
        self.__mao_de_cartas.append(carta)

    def get_posicao(self):
        return self.__posicao
       
    def get_id(self):
        return self.__jogador_id

        
    def get_eh_local(self):
        return self.__eh_local
    
    def set_eh_local(self, eh_local):
        self.__eh_local = eh_local
        
    def is_carta_no_baralho(self, carta):
        for carta_jogador in self.__mao_de_cartas:
            if carta_jogador == carta:
                return True
        return False

