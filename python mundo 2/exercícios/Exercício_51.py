primer = int(input("Primeiro termo: "))
razão = int(input('Razão: '))
pro_ar = primer + (11 - 1) * razão

for c in range(primer, pro_ar, razão):
    print(f'{c}', end='→ ')
