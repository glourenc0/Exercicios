#Início da função metragem_limpeza()
def metragem_limpeza():
  print('------------------------------------------------ Menu 1 de 3 - Metragem de Limpeza -------------------------------------------------')
  while True:
    try: 
      valor_metragem = 0
      metragemF = int(input('Digite a metragem da casa: '))  
      if (metragemF >= 30) and (metragemF < 300):
        valor_metragem += 60 + 0.3 * metragemF
        print('É necessário contratar 1 pessoa')
      elif (metragemF >= 300) and (metragemF < 700):
                valor_metragem += 120 + 0.5 * metragemF
                print('É necessário contratar 2 pessoas')
      else:
          print('Não aceitamos casas com metragem menor que 30m² ou maior que 700m²')
          continue # retorna para a pergunta 
      return valor_metragem
    except ValueError:  #caso o usuário digite valores não inteiros ou letras 
      print('Opção Inválida, pare de digitar letras ou valores não inteiros!')
#Fim da função metragem_limpeza() 

#Início da função tipo_limpeza()
def tipo_limpeza():
  print('-------------------------------------------------- Menu 2 de 3 - Tipo de Limpeza ---------------------------------------------------')
  while True:
    multiplicador = 0 
    tipoF = input('Escolha qual o tipo de limpeza \n' +
                  'B - Básica (indicadas para sujeiras semanais ou quinzenais) \n' +
                  'C - Completa (indicadas para sujeiras antigas e/ou não rotineiras) \n').upper()
    tipoF = tipoF.upper()
    tipoF = tipoF.strip()
    if tipoF == 'B':
      print('Você selecionou a limpeza Básica')
      multiplicador += 1.00
    elif tipoF == 'C':
      print('Você selecionou a limpeza Completa')
      multiplicador += 1.30
    else:
      print('Opção inválida pare de digitar opções diferente de B/C')
      continue #volta para o início
    return multiplicador
#Fim da função tipo_limpeza() 

#Início da função adicional_limpeza()
def adicional_limpeza():
  print('--------------------------------------- Menu 3 de 3 - Adicional de Limpeza -------------------------------------------------------')
  acumulador = 0 
  while True:
    adicionalF = input('Deseja mais algum adicional: \n' +
                       '0- Não desejo mais nada (encerrar pedido) \n' +
                       '1- Passar 10 peças de roupas - (R$ 10.00) \n' +
                       '2- Limpeza de 1 Forno/Micro-ondas - (R$ 12,00) \n' +
                       '3- Limpeza de 1 Geladeira/Freezer - (R$ 20,00) \n')    
    if adicionalF == '0':
      return acumulador
    elif adicionalF == '1':
      acumulador = acumulador + 10
      continue #volta para o início do while True
    elif adicionalF == '2':
      acumulador = acumulador + 12
      continue #volta para o início do while True
    elif adicionalF == '3':
      acumulador = acumulador + 20
      continue #volta para o início do while True  
#Fim da função adicional_limpeza() 

#Início do Main()
print('-------------------------------------- Bem-Vindo ao Programa de serviços de Limpeza ------------------------------------------------')
metragem = metragem_limpeza() #invocando a função
tipo = tipo_limpeza() #invocando a função
adicional = adicional_limpeza() #invocando a função
total = metragem * tipo + adicional #varialvel que dedfine o total
print('O Total Ficou: R$ {:.2f} (Metragem: R$ {:.2f}), Tipo de Limpeza: R$ {:.2f}, Adicional R$ {:.2f}'.format(total, metragem, tipo, adicional))