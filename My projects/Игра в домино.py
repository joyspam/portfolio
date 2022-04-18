import time
print('Игра ДОМИНО') #https://trinket.io/python3/ef0daedda5?outputOnly=true
print('')
print("игра до 101 очка")
print('')
print("Введите имя первого игрока")
name1 = input()
print("Введите имя второго игрока")
name2 = input()
x = 1
i = 0
l = 0 
def game(x,i,l,name1,name2):
    
    print(x,'раунд')
    x+=1
    import time
    a = 0
    n = 0
    c = 0
    d = 0
    
    def num(n):
        if n % 100 == 1 or n % 10 == 1 and n % 100 != 11:
            print(n, 'очко')
        elif n % 10 == 0 or n % 100 == 0 or n % 10 == 5:
            print(n, 'очков')
        elif n % 2 == 0 and n % 100 != 0 and n % 10 != 6 and n % 10 != 8 and n % 100 != 12 and n % 100 != 13 and n % 100 != 14 or n % 10 == 3 and n % 100 != 13:
            print(n, 'очка')
        else:
            print(n, 'очков')
    
    def inputint(prompt=None): #функция проверки числа
        while True:
            s = input(prompt)
            try:
                return int(s)
            except ValueError:
                print('Ошибка. Ожидалось число.')

       
    while n < 101:
        print(name1+': ввести количество новых очков ("0" если их нет)' '\n')
        a = inputint('')
        
        if a > 0: 
            n += a
            print(name1, end =' ')
            num(n)
            print(name2, end =' ')
            num(d)
            if n < 101:
                print('ИГРА ПРОДОЛЖАЕТСЯ!','\n', '_______________________')
            elif n >= 101:
                l+=1
                print(name1, 'победитель!''\n')
        
        else:
            print(name2+': ввести количество новых очков ("0" если их нет)' '\n')
            c = inputint('')
            d += c
            print(name2, end =' ')
            num(d)
            print(name1, end =' ')
            num(n)
            if d < 101:
                print('ИГРА ПРОДОЛЖАЕТСЯ!','\n', '_______________________')
            elif d >= 101:
                print(name2,' победил!''\n')
                i+=1
                break
    print('ˁ˚ᴥ˚ˀ')
    print('Окончен',x-1,'раунд. Счёт: ',name2,i,':',l,name1)
    print('Еще раз? написать "да" или "нет"')
    
    yesno = input()
    if yesno =='да':
        print('ok')
        game(x,i,l,name1,name2)
    elif yesno == 'нет':
        print('Bye')
    else:
        print('Только "да" или "нет"')
        time.sleep(2)
        yesno = input()
        
        if yesno =='да':
            game(x,i,l,name1,name2)
        elif yesno == 'нет':
            print('Bye')
            time.sleep(2)
        else:
            print('ну и пока')
            time.sleep(2)

game(x,i,l,name1,name2)
print('GAME OVER')
time.sleep(2)
