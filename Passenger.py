from Person import Person
from Flight import Flight
from Seat import Seat

#optei por nao ser heranca, pq a pessoa nao nasce sendo passageiro, ele se torna apartir do momento que compra uma passagem
class Passenger:
    def __init__(self, person: Person, flight: Flight, seat: Seat):
        self.person = person
        self.flight = flight
        self.seat = seat
#----------------------------------------- 

#classe de Tripulante, tripulante é uma pessoa, portanto, por isso a heranca, optei por ser diferente de passageiro, pra que passageiro pudesse comprar a passagem
class CrewMember(Person):
    def __init__(self, name, cpf, role: str, flight: None):
        super().__init__(name, cpf) #da heranca
        self.role = role #funcao do tripulante, tipo piloto, aeromoca etc
        self.flight = flight
    #funcao para mostrar as informacoes
    def show_informations(self):
        print(f"Tripulante: {self.name} - ({self.role})")
#-----------------------------------------  