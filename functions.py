def primeiro_digito(cpf):
  lista = cpf.replace('-',' ').replace('.',' ').replace('',' ').split()
  del lista[-1]
  del lista[-1]
  listaInt=[int(x) for x in lista]
  soma=0
  for x,valor in enumerate(listaInt):
    soma += valor * (abs(x-len(listaInt)) + 1)

  primeiro_digito = 0 if (10 * soma) % 11 > 9 else (10 * soma) % 11
  return primeiro_digito,listaInt
  

def segundo_digito(cpf,primeiro_digito,listaInt):
  listaInt.append(primeiro_digito)
  
  listaPrimeiro_feita=[]

  soma2 = 0  
  for x,valor in  enumerate(listaInt):
      soma2 += valor * (abs(x-len(listaInt)) + 1)
      listaPrimeiro_feita.append(soma2)

  resultado_final = 0 if (10 * soma2) % 11 > 9 else (10 * soma2) % 11

  cod_cpf = '{}-{}{}'.format(cpf[0:11],primeiro_digito,resultado_final)
  return cod_cpf 


def is_equal(cod_cpf,cpf_input):
  if cod_cpf == cpf_input:
    print('CPF correto 😍')
    print(f'{cod_cpf=}')
  else:
    print('CPF invalido')
    print(f'Seu cpf correto é {cod_cpf}')  