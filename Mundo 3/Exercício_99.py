def maior(*valores):
    print(f'Foram informados {len(valores)}!')
    print(f'Dentre {valores}, {max(valores)} é o maior valor')


maior(5, 4, 6, 9, 8)
maior(4, 5, 1)
maior(8, 17, 26, 56)
maior(0)
