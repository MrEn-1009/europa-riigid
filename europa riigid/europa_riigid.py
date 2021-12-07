f = open('TextFile1.txt' , 'r')
riigid ={}
for line in f:
    k, v=line.strip().split('-')
    riigid[k.strip()] = v.strip()
z=''
z=input('Что вы хотите сделать?\nВвод страны и показ его столицы - 1\nДобавление страны и столицы - 2\nУдаление страны и столицы - 3\nТест - 4\n ')
if z=='1':
    x=input('Какой страны вы хотите увидеть столицу? ')
    print(riigid[x])