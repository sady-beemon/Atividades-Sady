"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

sal = float(input("Insira o valor do seu salario atual: "))

if sal <=280:
    print("O seu salario antes era de $",sal,".\nResultando em um reajuste de 20%."
           "\nO valor ajustado foi um adicional de $",sal*0.2)
    sal = sal + (sal*0.2)
elif sal > 280 and sal < 700:
    print("O seu salario antes era de $",sal,".\nResultando em um reajuste de 15%."
           "\nO valor ajustado foi um adicional de $",sal*0.15)
    sal = sal + (sal*0.15)
elif sal >=700 and sal < 1500:
    print("O seu salario antes era de $",sal,".\nResultando em um reajuste de 10%."
           "\nO valor ajustado foi um adicional de $",sal*0.1)
    sal = sal + (sal*0.1)
else:
    print("O seu salario antes era de $",sal,".\nResultando em um reajuste de 5%.",
          "\nO valor ajustado foi um adicional de $",sal*0.05)
    sal = sal+(sal*0.05)

print("O valor total do seu salario atual é de $",sal)