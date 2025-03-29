"""
Este programa demonstra conceitos básicos de programação em Python, incluindo:
- Uso de variáveis de diferentes tipos (inteiros, flutuantes, strings, listas e dicionários);
- Estruturas de controle de fluxo como if-elif-else;
- Estruturas de repetição como for e while;
- Simulação de um switch-case utilizando um dicionário;
- Simulação de um loop do-while usando while True.

O usuário pode interagir com o programa digitando números para testar diferentes condições e fluxos.
"""

def switch_case(option):
    cases = {
        1: "Opção 1 escolhida",
        2: "Opção 2 escolhida",
        3: "Opção 3 escolhida",
    }
    return cases.get(option, "Opção inválida")

# Uso de variáveis de diferentes tipos
inteiro = 10
flutuante = 5.5
texto = "Olá, mundo!"
lista = [1, 2, 3, 4]
dicionario = {"chave1": "valor1", "chave2": "valor2"}

# Estrutura de controle if-elif-else
numero = int(input("Digite um número: "))
if numero > 10:
    print("Número maior que 10")
elif numero == 10:
    print("Número é 10")
else:
    print("Número menor que 10")

# Estrutura de repetição for
for i in range(5):
    print(f"Contagem: {i}")

# Estrutura de repetição while
contador = 0
while contador < 3:
    print(f"While: {contador}")
    contador += 1

# Simulando do-while em Python
while True:
    opcao = int(input("Escolha uma opção (1-3) ou 0 para sair: "))
    print(switch_case(opcao))
    if opcao == 0:
        break

# Classificação do Herói
nome_heroi = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de experiência (XP) do herói: "))

def classificar_heroi(xp):
    niveis = {
        range(0, 1000): "Ferro",
        range(1001, 2001): "Bronze",
        range(2001, 5001): "Prata",
        range(5001, 7001): "Ouro",
        range(7001, 8001): "Platina",
        range(8001, 9001): "Ascendente",
        range(9001, 10001): "Imortal",
    }
    for faixa, nivel in niveis.items():
        if xp in faixa:
            return nivel
    return "Radiante"

nivel = classificar_heroi(xp)
print(f"O herói {nome_heroi} está no nível {nivel}!")
