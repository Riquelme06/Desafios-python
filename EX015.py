km = float(input('Quantos quilometros foram percorridos pelo carro? '))
d = float(input('Por quantos dias o carro foi alugado? '))

preço = (60 * d) + (0.15 * km)

print('O preço que deve ser pago pelo aluguel do carro é de R$ {:.2f}' .format(preço))

