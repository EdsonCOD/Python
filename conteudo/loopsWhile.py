print("-=-"*13)  
numero = 1

while (numero <= 10):
    print(numero , end =" ")
    numero += 1
print("Laço encerrado")  
print("-=-"*13)  

nome = None
while True:
    print("Digite o seu nome: [x strop] ")
    nome = input()

    if nome in "xX":
        break

    print(f"Bem-Vindo, {nome}")
print("Concluido.")
print("-=-"*13)  