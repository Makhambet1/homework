asd = []        
zxc = []
old = 0         
citizen = 0         
makha = input('Введите длину очереди: ')
for a in range(int(makha)):
    name = input('Выберите: Мусульманин или христианин : ')
    if (int(name) == 2):   
        citizen = citizen + 1
    else:     
        asd.insert(old, 1)
        old = old + 1


for a in range(int(makha)):
    if old == 0:  
        for a in range(citizen):
            print('Православный христианин ')
            zxc.append('Православный христианин')
        break      
    print('Правоверный мусульманин ')
    old = old - 1
    zxc.append('Правоверный мусульманин')   
print(zxc)   
