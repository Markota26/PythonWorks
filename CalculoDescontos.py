while True:
    valor_hora = input('Quanto você recebe por hora?: ')
    try:
        valor_hora = float(valor_hora)
        print(type(valor_hora))
        break
    except:
        print('Valor invalido, tente novamente.')
        continue

while True:
    horas_trabalhadas = input('Quantas horas você trabalha por mês?: ')
    try:
        horas_trabalhadas = int(horas_trabalhadas)
        print(type(horas_trabalhadas))
        break
    except:
        print('Valor invalido, tente novamente.')
        continue

salario_Bruto = valor_hora * horas_trabalhadas

print(f'seu salario bruto é de: {salario_Bruto} reais por mês.')

valor_IR = round((salario_Bruto * 0.11), 2)
print(f'Será descontado de seu salário referente ao IR: {valor_IR}')

valor_INSS = round((salario_Bruto * 0.08), 2)
print(f'Será descontado de seu salário referente ao INSS: {valor_INSS}')

valor_Sindicato = round((salario_Bruto * 0.05), 2)
print(f'Será descontado de seu salário referente ao Sindicato: {valor_Sindicato}')

salario_Liquido = round((salario_Bruto - valor_IR - valor_INSS - valor_Sindicato), 2)
print(f'Salario liquido mensal: {salario_Liquido}')

