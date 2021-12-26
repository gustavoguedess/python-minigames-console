#%%
with open('palavras.csv', 'r') as f:
    palavras = f.read().split('\n')
palavras

#%%
import random
palavra = random.choice(palavras)

#%%
def clr():
    print('\n'*100)
#%%
import sys

letras = ''
tentativa=1
palavra_mostrada = '_'*len(palavra)

rosto = lambda t: 'o' if t>=1 else ' '
corpo = lambda t: '|' if t>=2 else ' '
besq = lambda t: '/' if t>=3 else ' '
bdir = lambda t: '\\' if t>=4 else ' '
pesq = lambda t: '/' if t>=5 else ' '
pdir = lambda t: '\\' if t>=6 else ' '

t=0
while palavra_mostrada!=palavra and t<=6:
    clr()
    print(f'-----')
    print(f'|   |')
    print(f'|   {rosto(t)}')
    print(f'|  {besq(t)}{corpo(t)}{bdir(t)}')
    print(f'|  {pesq(t)} {pdir(t)}')
    print(f'|')
    print(f'|', ' '*5, ' '.join(palavra_mostrada))
    print(f'Tentativas: {tentativa}')
    print('  '.join(letras))
    l = input()
    if len(l)!=1:
        print('Digite somente uma letra!\n')
        continue
    elif l in letras:
        print('Você já digitou essa letra\n')
        continue
    letras=l+letras
    new_response=''
    usado = False
    for n, _ in enumerate(palavra):
        if _ == l:
            new_response+=_ 
            usado=True
        else:
            new_response+=palavra_mostrada[n]
    if not usado:
        t+=1
    palavra_mostrada = new_response

if palavra_mostrada!=palavra:
    print('Acabou as tentativas')
else:
    print('PARABÉNS, VC CONCLUIU!')