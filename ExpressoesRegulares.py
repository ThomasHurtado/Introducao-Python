import re

telefone = 'Meu nome é Thomas e meu numero de telefone é (11)96644-7592'

print(re.search('\(\d{2}\)\d{4,5}\-\d{4}', telefone))

placa = "A placa do carro que encontrei foi EGQ-0011 ou EGQ-0012"

result = re.search('[A-Z]{3}-\d{4}', placa)
print(result)

email = "Meu email é thomashurtado@outlook.com ou thomasreis@unect.com.br"
result2 = re.findall('\w+@\w+\.\w*', email)
print(result2)