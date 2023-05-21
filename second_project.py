print('----------------------------- Seja Bem-Vindo a Sorveteria ---------------------------------------')
print('-------------------------------------------CARDÁPIO----------------------------------------------')
print('|Código| Descriação          | Tamanho P (500ml)  | Tamanho M (1000ml)     | Tamanho G (2000ml) |')
print('|  TR  | Sabores Tradicionais|     R$ 6,00        |     R$ 10,00           |      R$18,00       |')
print('|  ES  | Sabores Especiais   |     R$ 7,00        |     R$ 12,00           |      R$21,00       |')
print('|  PR  | Sabores Premium     |     R$ 8,00        |     R$ 14,00           |      R$24,00       |')
print('-------------------------------------------------------------------------------------------------')
#Menu

acumulador = 0 #acumulador global

while True:
 tamanho = input('Digite o tamanho do pote desejado (P/M/G): ').upper() #váriavel que recebe o tamanho com .upper() caso o usuário digite letras minúsculas
 codigo = input('digite o código do sorvete desejado (TR/ES/PR): ').upper() #váriavel que recebe o codigo com .upper() caso o usuário digite letras minúsculas
 if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
   print('Opção inválida, Pare de digitar códigos que não existem!')
   continue
 if codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
    print('Opção inválida, Pare de digitar códigos que não existem!')
    continue   #se o usuário digitar algo inválido volta para o começo 
 
 if tamanho == 'P' and codigo == 'TR':   
    print('Você pediu um sorvete sabor TRADICIONAL tamanho P de R$6,00')
    acumulador = acumulador + 6.00 

 elif codigo == 'TR' and tamanho == 'M':
    print('Você pediu um sorvete sabor TRADICIONAL tamanho M de R$10,00')
    acumulador = acumulador + 10.00 

 elif codigo == 'TR' and tamanho == 'G':
    print('Você pediu um sorvete sabor TRADICIONAL tamanho G de R$18,00')
    acumulador = acumulador + 18.00 

 elif codigo == 'ES' and tamanho == 'P':
    print('Você pediu um sorvete sabor ESCPECIAL tamanho P de R$7,00')
    acumulador = acumulador + 7.00 

 elif codigo == 'ES' and tamanho == 'M':
    print('Você pediu um sorvete sabor ESPECIAL tamanho M de R$12,00')
    acumulador = acumulador + 12.00  
    
 elif codigo == 'ES' and tamanho == 'G':
    print('Você pediu um sorvete sabor ESPECIAL tamanho G de R$21,00')
    acumulador = acumulador + 21.00  

 elif codigo == 'PR' and tamanho == 'P':
    print('Você pediu um sorvete sabor PREMIUM tamanho P de R$8,00')
    acumulador = acumulador + 8.00  

 elif codigo == 'PR' and tamanho == 'M':
    print('Você pediu um sorvete sabor PREMIUM tamanho M de R$14,00')
    acumulador = acumulador + 14.00 

 elif codigo == 'PR' and tamanho == 'G':
    print('Você pediu um sorvete sabor PREMIUM tamanho G de R$24,00')
    acumulador = acumulador + 24.00 

 pedir_mais = input('Deseja pedir mais alguma coisa ? (S/N)?: ').upper()
 if pedir_mais == 'S':
   continue 
 else:
   print('O valor total a ser pago: R${:.2f}'.format(acumulador)) 
   break 