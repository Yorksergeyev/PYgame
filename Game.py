i = 300 #мои жизни
i1 = 300 #жизнь троля
print(' У вас', i ,'жизней\n \n У троля',i1,'жизней')
import random
while i > 0 and i1 > 0: 
    print('\n --------------------НОВЫЙ РАУНД------------------\n Выберете действие: Атака / Блок') 
    AT=input('\n Ваш выбор: ')
    if AT == 'атака':
        
        x = random.randint(1,50) #вероятность что троль блокирует
        x1 = random.randint(1,100) #вероятность что троль не блокирует
        if x >= x1:
            z = random.randint(1,100) #защита троля
            z1 = random.randint(1, 100) #моя атака
            if z1 > z:
                i1 -= z1
                print('\n Пробив защиту троля вы нанесли', z1,'урона. ', ' У троля', i1 ,('жизней'))
            if z1 <= z:
                i -= z1
                print('\n Троль блокировал', z1,'вашего урона. ', ' У вас', i ,('жизней'))
        if x < x1:
            z = random.randint(1,50) #атака троля
            z1 = random.randint(1, 50)#моя атака
            i -= z
            print(('\n Вам нанесли'), z,('урона. '),' У вас', i ,('жизней'))
            i1 -= z1
            print(('\n Вы нанесли тролю'), z1,('урона. '),' У троля', i1 ,('жизней'))
    elif AT == 'блок':
        x = random.randint(1,100) #атака троля
        x3= random.randint(50, 150) #вероятность что троль блокирует
        if x <= x3:
            z = random.randint(1,100) #атака троля
            z1 = random.randint(1, 100) #моя защита
            
            if z > z1:
                i -= z
                print('\n Троль пробив блок нанес', z,'урона. ', ' У вас', i ,('жизней'))
            if z <= z1:
                i1 -= z
                print('\n Блокировано', z,'урона троля. ', ' У троля', i1 ,('жизней'))
        if x > x3:
            print('\n Троль и вы заняли оборонительные стойки')
    elif AT == 'вызов Вани':
        x = random.randint(10000,1000000000)
        i1 -= x
        print('\n Прибегает Ваня Мартыненко и наности тролю', x,('урона'))
        print('\n У троля', i1 ,'жизней  ВСЕ в АХУЕ')
    elif AT == 'HP':
        print(' Ваши жизни', i,'\n Жизни троля', i1)
    else:
        print('\n Введите в строке \'атака\' или \'блок\' !!!')
if i <= 0:
    print('\n Ты убит')
elif i1 <= 0:
    print('\n Троль убит')

input()

