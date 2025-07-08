from utils import create_flights, list_random_passengers, list_random_crew_members

def main():
    fligths = create_flights(10) 
    passengers = list_random_passengers(fligths) #retorna os 10 passageiros aleatorios
    crew_members = list_random_crew_members(fligths) #retorna os 10 tripulantes aleatorios

    #mostra os passageiros
    print("---------------PASSAGEIROS---------------")
    for passenger in passengers:
        print(f"🧍 - Passageiro: {passenger.person.name}, CPF: {passenger.person.cpf}")
        print(f"🛫 - Voo: {passenger.flight.number} - Preço: R${passenger.flight.price}")
        print(f"💺 - Assento: {passenger.seat.number}")
        print("-" * 30)

    #mostra os tripulantes
    print("\n---------------TRIPULANTES---------------")
    for crew in crew_members:
        print(f"🧑‍✈️ - {crew.name} - {crew.role} -  Voo: {crew.flight.number} ")
        print("-" * 30)

main()

