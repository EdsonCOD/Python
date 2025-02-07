for externo in range(1,6):
    print(f"\nRodada: {externo}")
    for interno in range(5, 0, -1):
        print(f"Valor: {interno}")

print("Fim dos laços")
print()

import random

for A in range(1, 6):
    print(f"\nConjunto {A}")
    for b in range(5):
        numero = random.randint(1,100)
        print(f"Valor: {numero}")