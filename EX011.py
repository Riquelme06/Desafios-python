print('QUANTOS LITROS DE TINTA VOCÊ PRECISA COMPRAR?')
l = float(input('Qual a largura da sua parede?'))
h = float(input('Qual a altura da sua parede?'))

area = l * h
tinta = area/2

print('A área da parede é {} metros quadrados, você precisará de {} litros de tinta'.format(area,tinta))