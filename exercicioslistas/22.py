"""Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%"""

ids = 0
problema = ['necessita da esfera',"necessita de limpeza","necessita troca do cabo ou conector","quebrado ou inutilizado" ]
df = [0,0,0,0]

while True:
    mouse = int(input("Digite o codigo do mouse(igual a zero encerra o programa): "))
    if mouse == 0:
        break
    ids += 1
    pro = int(input("Digite o problema:\n1 - Necessita da esfera;\n2 - Necessita de limpeza; \n3 - Necessita troca do cabo ou conector; \n4 - Quebrado ou inutilizado;\n"))
    df[pro-1] += 1

print("\nQuantidade de mouses: ",ids)
for i in range(4):
    print(i+1," - ",problema[i]," = Quantidade: ",df[i]," Percentual: ",round((df[i]/ids)*100,1),"%")