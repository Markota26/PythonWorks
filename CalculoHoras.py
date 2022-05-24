while True:
    salario_Bruto = input('Digite seu salario bruto: ')

    try:
        salario_Bruto = float(salario_Bruto)
        print('Valor válido. Vamos prosseguir!')
        break
    except:
        print('Valor invalido. Tenten Novamente')
        continue

while True:
    horas_trabalhadas = input('Digite suas horas trabalhadas por dia: ')

    try:
        horas_trabalhadas = float(horas_trabalhadas),
        print('Valor válido. Vamos prosseguir!')
        break
    except:
        print('Valor invalido. Tenten Novamente')
        continue

horas_trabalhadas = round((horas_trabalhadas * 30), 2)

valor_hora = round((salario_Bruto / horas_trabalhadas), 2)

print(f'Você recebe R${valor_hora} por hora.')
