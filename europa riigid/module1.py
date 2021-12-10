from random import *
def haf(riigid:dict,riigid2:dict):
     x=input('Какой страны вы хотите увидеть столицу? ')
     if x not in riigid and riigid2:
        b=input('Такой страны или столицы нет в списках. Хотите ввести её сами?\n1-да\n2-нет\n')
        if b=='1':
            c=input('Введите страну')
            v=input('Введите столицу')
            riigid.update({c:v})
     else:
        print(riigid[x])
     u=input('Какой столицы вы хотите увидеть страну?')
     print(riigid2[u])

def test(riigid:dict,riigid2:dict,riig:list,linn:list):
    h=int(input('Сколько вопросов вы хотите?'))
    for i in range(h):
        n=randint(0,50)
        a=riig[n]
        h=riigid[riig[n]]
        k=input(f'Введите столицу данного государства,{a},')
        if k!=h:
            print('Неправильно')
        else:
            print('Правильно')
