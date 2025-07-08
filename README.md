**🛫Reserva de voo**

Este projeto simula um sistema de reserva para voos comerciais. Ele gerencia múltiplos voos, passageiros, assentos e tripulação de forma integrada e realista.

**Funcionalidades principais:**

Criação de 10 voos com códigos únicos (exemplo: VOO001, VOO002, etc.).

  Cada voo possui 250 assentos disponíveis para reserva.
  Cada voo tem um preço individual associado.
  Passageiros são associados a voos e a assentos específicos, garantindo que cada reserva vincule um cliente a um assento disponível.
  Utilização da biblioteca Faker para popular dados fictícios de passageiros e tripulantes com informações realistas (nomes, CPFs, etc.).
  Tripulantes (pilotos, copilotos, comissários) são criados e associados a seus respectivos voos.
  Implementação de uma função para escolher assentos de forma aleatória (choice) garantindo alocação eficiente e sem conflito.
  No final, o sistema exibe:
  10 passageiros, com seus respectivos voos, com o preco de cada voo e seu assento.
  10 tripulantes, com seus respectivos cargos e vvoos.
  
**Instalacao:**

git clone https://github.com/raffaela09/projeto_aviao.git
cd projeto_aviao
pip install -r requirements.txt


