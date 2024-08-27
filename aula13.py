nome = "João Dias"
altura = 1.76
peso = 78
imc = peso / (altura * altura)
# print(nome,altura )
# print(peso)
# print(imc)
# o f string ele le a variavel na string atraves de {}
linha_1 = f'{nome} tem {altura} de altura'  
linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'

print(linha_1, linha_2)


# print(nome, 'tem', altura, 'de altura')
# print('pesa', peso, 'quilos e seu IMC é')
# print(imc)