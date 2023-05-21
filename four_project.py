#----------- Início das Variáveis Globais ------------
lista_funcionario = []
id_funcionario = 0
#------------- Fim das Variáveis Globais -------------

#------------- Início de cadastrar_funcionario() -------------
def cadastrar_funcionario(id):
  print('Bem-vindo ao menu de Cadastrar Funcionário')
  print('ID do Funcionário: {}'.format(id))
  nome = input('Digite o Nome do Funcinário: ')
  setor = input('Digite o Setor do Funcinário: ')
  salario = int(input('Digite o Salário do Funcinário: '))
  dicionario_funcionario = {'ID'     : id,
                            'nome'   : nome, 
                            'setor'  : setor,
                            'salario': salario}
  lista_funcionario.append(dicionario_funcionario.copy())
#------------- Fim de cadastrar_funcionario() -------------

#------------- Início de consultar_funcionario() -------------
def consultar_funcionario():
  print('Bem-vindo ao menu de Consultar Funcionário')
  while True:
    opcao_consultar = input('\n Escolha a opção desejada: \n' +
                            '1-Consultar Todos os Funcionário \n' +
                            '2-Consultar Funcionário(s) por ID \n' +
                            '3-Consultar Funcionário(s) por Setor \n' +
                            '4-Sair \n' +
                            '>>')
    if opcao_consultar == '1':
      print('Você escolheu a opção Consultar Todos os Funcionários')
      for funcionario in lista_funcionario: #funcionario irá varrer toda a lista de funcionarios
        print('-------------------------------')
        for key, value in funcionario.items(): #varrer todos os items chave e valor do dicionario_funcionario
          print('{}: {}' .format(key,value))
        print('-------------------------------')
    elif opcao_consultar == '2':
      print('Você escolheu a opção Consultar Funcionário(s) por ID')
      id_desejado = int(input('Digite o ID desejado: '))
      for funcionario in lista_funcionario:
        if funcionario['ID'] == id_desejado:
          print('-------------------------------')
          for key, value in funcionario.items(): #varrer todos os items chave e valor do dicionario_funcionario
            print('{}: {}' .format(key,value))
        print('-------------------------------')
    elif opcao_consultar == '3':
      print('Você escolheu a opção Consultar Funcionário(s) por Setor')
      id_desejado = input('Digite o Setor desejado: ')
      for funcionario in lista_funcionario:
        if funcionario['setor'] == id_desejado:
          print('-------------------------------')
          for key, value in funcionario.items(): #varrer todos os items chave e valor do dicionario_funcionario
            print('{}: {}' .format(key,value))
        print('-------------------------------')
    elif opcao_consultar == '4':
      return #sai da opção consultar_funcionario e volta para o Main
    else:
      print('!!! Opção inválida tente novamente !!!')
      continue #volta para o ínicio
#------------- Fim de consultar_funcionario() -------------

#------------- Início de remover_funcionario() -------------
def remover_funcionario():
  print('Bem-vindo ao menu remover Funcionário')
  id_desejado = int(input('Digite o ID do Funcionário que deseja Remover: '))
  for funcionario in lista_funcionario: 
    if funcionario['ID'] == id_desejado:
      lista_funcionario.remove(funcionario)
      print('Funcionário Removido')
#------------- Fim de remover_funcionario() -------------

#------------- Início de Main -------------
print('Bem-vindo ao Controle de Funcionários do Gustavo Lourenço Marcondes da Silveira ')
while True:
  opcao_principal = input('\n Escolha a opção desejada: \n' +
                          '1-Cadastrar Funcionário \n' +
                          '2-Consultar Funcionário(s) \n' +
                          '3-Remover Funcionário \n' +
                          '4-Sair \n' +
                          '>>')
  if opcao_principal == '1':
    id_funcionario = id_funcionario + 1 
    cadastrar_funcionario(id_funcionario)
  elif opcao_principal == '2':
    consultar_funcionario()
  elif opcao_principal == '3':
    remover_funcionario()
  elif opcao_principal == '4':
    break # encerra o laço e o progrma acaba
  else:
    print('!!! Opção inválida tente novamente !!!')
    continue #volta para o ínicio 
#------------- Fim de Main -------------