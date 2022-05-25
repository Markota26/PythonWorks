while True:
    valor_hora = input('Quanto você recebe por hora?: ')
    if not valor_hora.isdecimal():
        print('Valor invalido, tente novamente.')
        continue
    else:
        valor_hora = float(valor_hora)
        print('Valor válido.')
        break
while True:
    horas_trabalhadas = input('Quantas horas você trabalha por mês?: ')
    if not horas_trabalhadas.isnumeric():
        print('Valor invalido, tente novamente.')
        continue
    else:
        horas_trabalhadas = int(horas_trabalhadas)
        print('Valor válido.')
        break
  

salario_Bruto = valor_hora * horas_trabalhadas

print(f'seu salario bruto é de: R${salario_Bruto} por mês.')

valor_IR = round((salario_Bruto * 0.11), 2)
print(f'Será descontado de seu salário referente ao IR: R${valor_IR}')

valor_INSS = round((salario_Bruto * 0.08), 3)
print(f'Será descontado de seu salário referente ao INSS: R${valor_INSS}')

valor_Sindicato = round((salario_Bruto * 0.05), 2)
print(f'Será descontado de seu salário referente ao Sindicato: R${valor_Sindicato}')

salario_Liquido = round((salario_Bruto - valor_IR - valor_INSS - valor_Sindicato), 2)
print(f'Salario liquido mensal: R${salario_Liquido}')

