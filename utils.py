from faker import Faker
from Passenger import CrewMember, Passenger
from Person import Person
from Flight import Flight
import random



fake = Faker("pt-BR") #define a linguagem
#as funcoes do tripulabnte
roles_crewmembers = ["Piloto", "Copiloto", "Comissário", "Aeromoca"]


#classe de pessoa fake herdada por person, utilizada dessa forma, ja que person é uma classe abstrata, e portanto, n pode ser instanciada diretamente
class FakePerson(Person):
    #funcao para mostrar as informacoes da pessoa fake criada
    def show_informations(self):
        print(f"Nome: {self.name} - CPF: {self.cpf}")
#----------------------------------------- 

#funcao para criar os voos
def create_flights(n=10):
    fligths = [] #lista para adicionar os voos

    #for para gerar os voos
    for n in range(n):
        code = f"VOO{n+1:03d}" #faz o voo ser um prefixo do voo, e formata o codigo do voo com 3 digitos, preenchendo com zero para a esquerda se necessario
        price = round(random.uniform(100, 1000), 2) #gera um numero aleatorio de 100 a 1000, e arredonda esse numero para casas decimais, pra caso haja um preco com centavos
        fligth = Flight(code, price) #instancia a classe
        fligths.append(fligth) #adiciona o voo a lista
    return fligths
#----------------------------------------- 

#funcao responsavel por criar um tripulante, com nome, cpf e cargo
def create_crew_member(flight):
    roles_random = random.sample(roles_crewmembers, 4) #retorna elementos unicos da lista, impedindo a repeticao , o sample é responsavel por impedir a repeticao
    for role in roles_random:
        name = fake.name()      #utilizando o faker para criar um nome falso
        cpf = fake.cpf()        #criar cpf

        tripulante = CrewMember(name, cpf, role, flight)
        flight.add_crew_members(tripulante)
#----------------------------------------- 

#funcao para escolher o assento de forma aleatoria
def choice_seat(flight):
    free_seats = [seat for seat in flight.airplane.seats if not seat.is_occupied()]  #adiciona assentos a lista se o assento ja n estiver ocupado
    seat = random.choice(free_seats) #escolhe assentos aleatorios da lista de assentos livres
    return seat
#----------------------------------------- 

#funcao para criar um passageiro com dados aleatorios
def create_passenger(flight):
    name = fake.name()
    cpf = fake.cpf()
    pessoa_fake = FakePerson(name, cpf)
    seat = choice_seat(flight)

    passenger = Passenger(pessoa_fake, flight, seat)
    seat.to_occupy(passenger)
    flight.add_passenger(passenger)
    
    return passenger
#----------------------------------------- 

#funcao para associar o passaageiro com assento, voo etc
def populate_passengers(flights):
        for flight in flights:
            free_seats = [seat for seat in flight.airplane.seats if not seat.is_occupied()]
            for seat in free_seats:
                create_passenger(flight)
#----------------------------------------- 

# funcao para retornar a lista com os passareios
def list_random_passengers(flights, n=10):
    all_passengers = [] #lista para armazenar todos os passageiros

    for flight in flights:
        all_passengers.extend(flight.passengers) #adiciona todos os passageiros de cada voo na lista de todos os passageiros

    #no caso de nao ter passageiros, cria de forma automatica
    if not all_passengers:
       populate_passengers(flights)#chama a funcao para preencher os voos que estao vazios 
       all_passengers = []
       #para preencher a lista de todos os passageiros com os passageiros criados
       for flight in flights:
           all_passengers.extend(flight.passengers)

    
    passengers = random.sample(all_passengers, min(n, len(all_passengers)))#escolhe 10 passageiros de forma aleatoria com o random 
    return passengers
#----------------------------------------- 

#funcao para retornar a lista de tripulantes
def list_random_crew_members(flights, n=10):
    all_crew_members = [] #lista de tripulantes vazia

    #percorre os voos criados 
    for flight in flights:
        #cria os tripulantes 
        create_crew_member(flight)

        #relaciona o tripulante ao voo
        all_crew_members.extend(flight.crew_members)

    crew_members = random.sample(all_crew_members, min(n, len(all_crew_members))) #escolhe 10 tripulantes de forma aleatoria com o random

    return crew_members
#----------------------------------------- 





