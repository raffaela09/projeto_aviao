from Seat import Seat

#classe aviao
class Airplane:
    def __init__(self):
        self.seats = [] #lista de asssentos
        rows = 50 # faz com que sejam 50  fileiras
        cols = ["A","B","C","D","E"] #5 assentos por fileira (5x50 = 250), para que os assentos tenham numeros tipos A1, B2, etc
        for row in range(1, rows +1): 
            for col in cols:
                seat_number = f"{row}{col}"
                self.seats.append(Seat(seat_number))
#-----------------------------------------  

#classe de voo
class Flight:
    def __init__(self, code, price):
        self.number = code
        self.price = price
        self.airplane = Airplane()  #retorna a classe aviao
        self.crew_members = []       #lista de tripulantes
        self.passengers = []        #lista de passageiros
    #-----------------------------------------  

    #para adicionar o passageiro a lista de passageiros
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    #-----------------------------------------  

    #para adicionar os tripulantes a lista de tripulantes
    def add_crew_members(self, crew_member):
        self.crew_members.append(crew_member)  
    #-----------------------------------------  
    
    def __str__(self):
        return f"Flight {self.number} - Price R${self.price}"