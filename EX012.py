preco = float(input('Digite o preço do produto:'))
desc = preco - (5 * 0.01 * preco)

print('O novo preço do produto com desconto é: R$ {:.2f} '.format(desc))
