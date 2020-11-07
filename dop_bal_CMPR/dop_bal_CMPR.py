import numpy as np
from collections import defaultdict
import ast

print("Здравтсвйте,введите размерность матрицы")
dx=int(input("Кол-во строк="))
dy=int(input("Кол-во столбцов="))
print(f"\nРазмерность ваших  матриц будет {dx}x{dy}\n ")
#Двумерный вектор размерностью dx na dy
matrix1=np.zeros((dx,dy), dtype=int)
i=0
j=0
print("Заполните матрицу первого игрока")
#Заполнение матрицы
while i <dx:
    while j<dy:
        matrix1[i][j]=input(f"Введите значение элемента на позиции({i+1},{j+1})=")
        j+=1
    i+=1
    j=0

print(f"Матрица первого игрока =\n{matrix1}")

 #Функция поиска пула наилучших решения для игроков 
def max1(matr):
    otvet=[]
    new = {}
    y=np.shape(matr)#Размерность
    dx=y[0]
    dy=y[1]
    d=f=0
    while d<dx:
        max_num=-999999999999999999999999
        while f<dy:
            if matr[d][f]>=max_num:
                 max_num=matr[d][f]
            f+=1;
        f=0
        while f<dy:
            if matr[d][f]==max_num:
                 new.setdefault(d, []).append(f)
                 otvet.append(matr[d][f])
            f+=1
        f=0
        d+=1
    return(new)


#Создание двумерного вектора размерностью dx na dy  для 2 игрока
matrix2=np.zeros((dx,dy), dtype=int)
i=0
j=0
print("Заполните матрицу второго игрока")
while i <dx:
    while j<dy:
        matrix2[i][j]=input(f"Введите значение элемента на позиции({i+1},{j+1})=")
        j+=1
    i+=1
    j=0

 

print("Матрица игрока 1=\n",matrix1)
print(f"Матрица игрока 2=\n{matrix2}")
matrix  = matrix1.transpose() #ТРАНСПОНИРОВАТЬ МАТРИЦУ
one=max1(matrix)
two=max1(matrix2)
print("Множество наилучший ответов для певрого игрока=\n",one)
print("Множество наилучший ответов для второго игрока=\n",two)


#Тут мы проверяем тип матрицы,квадратная или нет (Можно было сделать лучше,но имеем, что имеетм)
#Затем проходимся по множествам наилучших решений двух игроков ()поиск пересечений их множеств для нахождения равновесия по нэшу)
if dx==dy:
    print("Матрица квадратная")
    i=0
    otwet=[]
    while i<dx:
        znac=one[i]
        if len(znac)==1:
            try:
                (two[znac[0]]).index(i)
                otwet.append(f"({znac[0]},{i})")
            except :
                print(" ")
                #print("Значение не входит в список")
        else:
           size=len(znac)
           while size!=0:  
               try:
                   #
                    two[znac[size-1]].index(i)
                    otwet.append(f"({znac[size-1]},{i})") 
               except:
                   print(" ")
                   #print("Значение не входит в список")
               size-=1
        i+=1
    
    print(f"\nМножество ответов={otwet}")

 #Аналогично верхнему но не для квадратной матрицы
else:
    max_=max(dx,dy)
    if len(one)<len(two):
        promejutok=two
        two=one
        one=promejutok  
    i=0
    otwet=[]
    while i<max_:
        znac=one[i]
        if len(znac)==1:
            try:
                (two[znac[0]]).index(i)
                otwet.append(f"({znac[0]},{i})")
            except :
                print(" ")
                #print("Значение не входит в список")
        else:
             size=len(znac)
             while size!=0:  
                try:
                    two[znac[size-1]].index(i)
                    otwet.append(f"({znac[size-1]},{i})") 
                except:
                    print(" ")
                    #print("Значение не входит в список")
                size-=1
        i+=1
    
    print(f"\nМножество ответов={otwet}")
 
if (otwet==[]):
    print("\n!!!!!!!!!!ОТСУСТВУЕТ РЕШЕНИЕ В ЧИСТЫХ СТРАТЕГИЯХ.!!!!!!!!!!!!!")