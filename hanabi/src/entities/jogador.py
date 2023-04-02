class Jogador:

    def __init__(self, nome, id, posicao):
        self.__nome = nome
        self.__mao_de_cartas = []
        self.__jogou_ultimo_turno = False
        self.__posicao = posicao
        self.__jogador_id = id
        self.__eh_local = False
    
    def __repr__(self):
        return str(self.__dict__)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_mao_de_cartas(self):
        return self.__mao_de_cartas
    
    def set_mao_de_cartas(self, baralho):
        self.__mao_de_cartas = baralho

    def get_jogou_ultimo_turno(self):
        return self.__jogou_ultimo_turno

    def set_jogou_ultimo_turno(self, jogou: bool):
        self.__jogou_ultimo_turno = jogou

    def jogar_descartar_carta(self, carta_jogada):
        index = 0
        for i in range(len(self.get_mao_de_cartas())):
            if self.get_mao_de_cartas()[i] == carta_jogada:
                index = i
        self.__mao_de_cartas.pop(index)

    def comprar_carta(self, carta):
        self.__mao_de_cartas.append(carta)

    def get_posicao(self):
        return self.__posicao
       
    def get_id(self):
        return self.__jogador_id
    
    def set_id(self, id):
        self.__jogador_id = id
        
    def get_eh_local(self):
        return self.__eh_local
    
    def set_eh_local(self, eh_local):
        self.__eh_local = eh_local
        
    def is_carta_no_baralho(self, carta):
        for carta_jogador in self.__mao_de_cartas:
            if carta_jogador == carta:
                return True
        return False

    def reset(self):
        self.set_mao_de_cartas([])
        self.set_jogou_ultimo_turno(False)
    

        

