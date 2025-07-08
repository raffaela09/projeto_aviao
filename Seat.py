#classe de poltrona
class Seat:
    def __init__(self, number: str):
        self.number = number #str pq seria algo como A1, B2, etc
        self.passenger = None #ja que inicialmente a poltrona esta vazia
    #----------------------------------------- 

    #Funcao para ocupar a poltrona
    def to_occupy(self, passenger):
        #se ja estiver ocupada, retorna um erro
        if self.passenger:
            raise Exception(f"Poltrona {self.number} já está ocupada!")
        #se estiver vazia, ocupa a poltrona
        self.passenger = passenger
    #-----------------------------------------  

    #Funcao que diz que a poltrona ja esta ocupada
    def is_occupied(self):
        return self.passenger is not None #logo, a poltrona está ocupada
    #-----------------------------------------  

    