print('Bem-vindo a loja') 
valor_unitario = float(input('Entre com o valor do produto: '))  # Variavel para o valor unitário
quantidade = int(input('Entre com o valor da quantidade: '))  # Variavel para a quantidade
valor_frete = 0 

if 0 <= quantidade < 11:
   valor_frete = 30
elif 11 <= quantidade < 101:
   valor_frete = 60
elif 101 <= quantidade < 1001:
   valor_frete = 120
else:
   valor_frete = 240

valor_parcial = float(valor_unitario * quantidade)  # Variavel que define o valor (sem frete)
valor_total = float(valor_parcial + valor_frete)  # Variavel para o valor com frete
print('O valor sem frete foi: R$ {:.2f}'.format(valor_parcial)) 
print('O valor com desconto foi: R$ {:.2f} '.format(valor_total) + '(frete de R$ {:.2f})'.format(valor_frete))