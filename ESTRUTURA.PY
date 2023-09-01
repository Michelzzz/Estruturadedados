import random

# 1 - media de 3 numeros inseridos pelo usuario

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
total = (num1 + num2 + num3) /3

print("A media dos numeros é de: ", {total})


# 2 - Se o numero inserido é impar ou par

numero1 = int(input("Insira um numero: "))

if numero1 % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")


# 3 - todos os numeros pares de 0 ate ele

numeros_pares = int(input("Digite um numero: "))

print("Numeros pares de 0 ate", numeros_pares,":")
for i in range (0, numeros_pares + 1, 2):
    print(i)


# 4 - Lista e ler o maior e menor numero

lista_numeros = []
    
elementos_da_lista = int(input("Digite o número de elementos na lista: "))
    
for i in range(elementos_da_lista):
        numero = float(input(f"Digite o {i+1}º número: "))
        lista_numeros.append(numero)

if lista_numeros:
        maior = max(lista_numeros)
        menor = min(lista_numeros)
        
        print(f"O maior número na lista é: {maior}")
        print(f"O menor número na lista é: {menor}")
else:
        print("A lista está vazia.")


# 5 - Lista de numeros e media dos numeros pares

tamanho_lista = int(input("Digite o tamanho da lista: "))
limite_superior = int(input("Digite o limite superior para os números aleatórios: "))
    
lista_numeros1 = [random.randint(1, limite_superior) for _ in range(tamanho_lista)]
    
numeros_pares = [numero for numero in lista_numeros1 if numero % 2 == 0]
    
if numeros_pares:

    media = sum(numeros_pares) / len(numeros_pares)
    print(f"A lista de números aleatórios é: {lista_numeros1}")
    print(f"A média dos números pares é: {media}")
else:

    print("Não há números pares na lista.")

# 6 - Numero inteiro positivo do usuario + fatorial

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("O fatorial não está definido para números negativos.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}")


# 7 - Sequencia de Fibonacci

maximo = int(input("Digite um valor máximo para a sequência de Fibonacci: "))

a, b = 0, 1

while a <= maximo:
    print(a, end=" ")
    a, b = b, a + b


# 8 - Primo ou nao

numero = int(input("Digite um número inteiro positivo: "))

if numero > 1:
    primo = True

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")
else:
    print("O número deve ser maior que 1 para ser considerado primo.")


# 9 - Lista de nome com letra A 

nomes = input("Digite uma lista de nomes separados por vírgulas: ")

lista_de_nomes = nomes.split(',')

nomes_com_A = []

for nome in lista_de_nomes:
    nome = nome.strip()
    if nome.startswith('A') or nome.startswith('a'):
        nomes_com_A.append(nome)

print("Nomes que começam com 'A':")
for nome in nomes_com_A:
    print(nome)

# 10 - Pedra, papel e tesoura

import random

opcoes = ["Pedra", "Papel", "Tesoura"]

print("Escolha uma opção:")
print("1. Pedra")
print("2. Papel")
print("3. Tesoura")

escolha_usuario = int(input("Digite o número da sua escolha: "))

if escolha_usuario < 1 or escolha_usuario > 3:
    print("Opção inválida. Por favor, escolha um número entre 1 e 3.")
else:
    escolha_usuario -= 1
    escolha_computador = random.randint(0, 2)

    print(f"Sua escolha: {opcoes[escolha_usuario]}")
    print(f"Escolha aleatoria: {opcoes[escolha_computador]}")

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 0 and escolha_computador == 2) or \
         (escolha_usuario == 1 and escolha_computador == 0) or \
         (escolha_usuario == 2 and escolha_computador == 1):
        print("Você venceu!")
    else:
        print("O computador venceu!")