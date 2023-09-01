Atividade2.py

# 1 - Calculando circulo

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):

        area = math.pi * (self.raio ** 2)
        return area


raio_do_circulo = 5.0  # Posso substituir pelo valor do raio que eu desejar
circulo = Circulo(raio_do_circulo)
area_do_circulo = circulo.calcular_area()
print(f"A área do círculo com raio {raio_do_circulo} é {area_do_circulo:.2f}")

# 2 - Livro, autor e titulo.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"


meu_livro = Livro("Diário de uma paixão", "Nicholas Sparks")
informacoes = meu_livro.detalhes()
print(informacoes)

# 3 - Retangulo

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


meu_retangulo = Retangulo(5, 10)
area_do_retangulo = meu_retangulo.calcular_area()
print(f"A área do retângulo é {area_do_retangulo}")

# 4 - Conta bancaria 

class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser maior que zero.")

    def consultar_saldo(self):
        return self.saldo


minha_conta = ContaBancaria("Jessica")
print(f"Saldo inicial da conta de {minha_conta.titular}: R${minha_conta.consultar_saldo():.2f}")

minha_conta.depositar(1000.0)
print(f"Saldo após o depósito: R${minha_conta.consultar_saldo():.2f}")

minha_conta.sacar(500.0)
print(f"Saldo após o saque: R${minha_conta.consultar_saldo():.2f}")

# 5 - Pessoa, nome, idade e falar

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome}.")

# Exemplo de uso da classe
pessoa1 = Pessoa("Benny", 30)
pessoa2 = Pessoa("Sophie", 25)

pessoa1.falar()
pessoa2.falar()

# 6 - Produto, nome, preço, qualidade.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

# Exemplo de uso da classe
produto1 = Produto("Vestido", 20.0, 3)
produto2 = Produto("Body", 30.0, 2)

total_produto1 = produto1.calcular_total()
total_produto2 = produto2.calcular_total()

print(f"Total do {produto1.nome}: R${total_produto1:.2f}")
print(f"Total do {produto2.nome}: R${total_produto2:.2f}")

# 7 - Carro, marca, modelo e ano.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"


meu_carro = Carro("Toyota", "Corolla", 2022)
informacoes_carro = meu_carro.detalhes()
print(informacoes_carro)

# 8 - Aluno, nome notas.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0  # Retorna 0 se não houver notas


notas_aluno1 = [9.4, 6.6, 9.2, 8.6]
aluno1 = Aluno("Douglas", notas_aluno1)

notas_aluno2 = [10, 5.5, 9.5, 7.0]
aluno2 = Aluno("Jossicleide", notas_aluno2)

media_aluno1 = aluno1.calcular_media()
media_aluno2 = aluno2.calcular_media()

print(f"A média das notas de {aluno1.nome} é {media_aluno1:.2f}")
print(f"A média das notas de {aluno2.nome} é {media_aluno2:.2f}")

# 9 - Triangulo, lado1, lado2, lado3

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3


triangulo1 = Triangulo(4, 5, 6)
triangulo2 = Triangulo(6, 6, 6)

perimetro1 = triangulo1.calcular_perimetro()
perimetro2 = triangulo2.calcular_perimetro()

print(f"O perímetro do primeiro triângulo é {perimetro1}")
print(f"O perímetro do segundo triângulo é {perimetro2}")

# 10 - Funcionario, nome, salario e cargo

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        if percentual_aumento > 0:
            aumento = (percentual_aumento / 100) * self.salario
            self.salario += aumento
            print(f"O salário de {self.nome} houve aumentado de {percentual_aumento}% para R${self.salario:.2f}")
        else:
            print("O percentual de aumento deve ser maior que zero.")


funcionario1 = Funcionario("Diego", 1300, "Caixa")
funcionario2 = Funcionario("Larissa", 5000, "Chefe")

funcionario1.aumentar_salario(10)
funcionario2.aumentar_salario(5)