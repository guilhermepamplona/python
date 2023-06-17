n1 = float(input('Digite a altura da parede: '))
n2 = float(input('Digite a largura da parede: '))
print('Você possui uma parede de {}m² e precisará de {:.2f}l de tinta para pintar ela por completo.'.format(n1*n2, (n1*n2)/2))