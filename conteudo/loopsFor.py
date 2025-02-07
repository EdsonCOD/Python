print("-=-"*13)  
for numeros in range(1, 10+1):
    print(numeros)
print("-=-"*13)  

nome = input("Digite o seu nome: ")
for x in range(10):
    print(f"{x + 1} {nome}")
print("-=-"*13) 

feiras = ("pão", "maçã", "banana", "abacate", "jujuba")
for feira in feiras:
    if feira == "jujuba":
        continue
    print(feira)

