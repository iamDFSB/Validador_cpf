from functions import primeiro_digito,segundo_digito,is_equal

# Modelo de como deve escrever o cpf no input → 545.975.408-90
cpf_input = input('Digite o cpf para validar: ')

# Validando o primeiro digito, depois do "-"
primeiro_digito, listaInt = primeiro_digito(cpf_input)

# Validando o segundo digito, depois do "-"
cod_cpf = segundo_digito(cpf_input,primeiro_digito,listaInt)

# Validando se o cpf do código é igual ao do input
is_equal(cod_cpf,cpf_input)