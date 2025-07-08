from abc import ABC, abstractmethod
from Flight import Flight
from Seat import Seat

#Classe abstrata
class Person(ABC):
    def __init__(self, name:str, cpf:str):
        self.name = name
        self.__cpf = cpf #dado sensivel
    #-----------------------------------------   

    #properties
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf (self, value):
        self.__cpf = value
    #-----------------------------------------   
    
    #contrato
    @abstractmethod
    def show_informations(self):
        pass #metodo que funciona como um contrato, por ser uma classe abstrata, ele deve ter ao menos um metodo que seja abstrato
        #esse metodo é responsavel por mostrar as informacoes da pessoa (seja tripulantes, ou passageiros)
    #-----------------------------------------   

    #para que a pessoa possa se tornar um passageiro, ela precisa comprar uma passagem
    #a funcao é responsavel por associar a pessoa ao assento, logo, tornando a um passageiro
    def buy_ticket(self, flight: Flight, seat: Seat):
        from Passenger import Passenger#importar aqui, para evitar o erro circular que estava ocorrendo
        #verifica se a poltrona ja esta ocupada, se estiver, retorna uma mensagem ao usuario
        if seat.is_occupied():
            raise Exception(f"Assento {seat.number} já está ocupado!")

        passenger = Passenger(self, flight, seat)
        seat.to_occupy(passenger)
        flight.add_passenger(passenger)


        return passenger       
 #-----------------------------------------       