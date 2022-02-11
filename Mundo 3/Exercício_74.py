from random import sample
num = tuple(sample(range(20), 5))
maior = max(num)
menor = min(num)
print(num)
print(f'O maior número sorteado foi {maior}.\nE o menor número foi {menor}')

