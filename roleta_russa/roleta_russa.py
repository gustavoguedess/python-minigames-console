import random 

while True:
    print('PRESSIONE ENTER PARA APERTAR O GATILHO')
    input()
    n = random.randint(0,6)
    if n==1:
        print('BANG!!!!')
        break 
    print('clack...')
    print('Próximo')