lar = float(input('Largura da parede(m): '))
alt = float(input('Altura da parede(m): '))
area = lar * alt
tinta = area / 2
print(f'Sua parede te a dimensão de {lar}x{alt} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}L de tinta.')
