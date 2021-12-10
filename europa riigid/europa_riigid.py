from module1 import *
f = open('TextFile1.txt' , 'r')
riigid ={}
riigid2 ={}
riig=linn=[]
for line in f:
    k, v=line.strip().split('-')
    riigid[k.strip()] = v.strip()
    riigid2[v.strip()] = k.strip()
    riig.append(k)
    linn.append(riigid[k.strip()])
z=''
while True:
    z=input('Что вы хотите сделать?\nВвод страны и показ его столицы - 1\nТест - 2\n')
    if z=='1':
        haf(riigid,riigid2)
    elif z=='2':
        test(riigid,riigid2,riig,linn)
    else:
        print('Ты что-то не то ввёл')
        break

