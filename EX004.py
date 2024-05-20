algo = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(algo))
print('Só tem espaços?', algo.isspace())
print('é um numero?', algo.isnumeric())
print('é alfabético?', algo.isalpha())
print('É alfanumérico?',algo.isalnum())
print('Está em maiusculas?', algo.isupper())
print('Está em minusculas?', algo.islower())