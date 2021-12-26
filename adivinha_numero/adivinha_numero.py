#%%
import random

digitos = 4
original = random.randint(0, 10**(digitos)-1)
original = str(original).zfill(digitos)
tentativas=0
while True:
    tentativas+=1
    num = original
    print(f'Tentativa #{tentativas}: ', end='')
    palpite = str(input())
    if len(palpite)!=len(num):
        print('Tamanho inválido. Digite Novamente')
        continue
    elif palpite==num:
        print('Parabéns, vc não é burro!')
        print(f'Número de tentativas: {tentativas}')
        break
    resp=''        
    for n, d in enumerate(palpite):
        if d==num[n] and d!='-':
            resp+='o'
            palpite = palpite[:n]+'-'+palpite[n+1:]
            num = num[:n]+'-'+num[n+1:]

    for n, d in enumerate(palpite):
        if d in num and d!='-':
            resp+='-'
            palpite = palpite[:n]+'-'+palpite[n+1:]
            num.replace(d, '', 1)
    while len(resp)!=len(num):
        resp+='x'
    print('              '+resp)