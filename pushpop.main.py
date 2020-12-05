asd = []
zxc = []
old = 0
citizen = 0
asik = input('Введите длину очереди: ')
for a in range(int(asik)):
    name = input('Выберите: 1.ветеран 2.обычный : ')
    if (int(name) == 2):
        citizen = citizen + 1
    else:
        asd.insert(old, 1)
        old = old + 1


for a in range(int(asik)):
    if old == 0:
        for a in range(citizen):
            print('обычный гражданин ')
            zxc.append('обычный гражданин')
        break
    print('ветеран В.О.В ')
    old = old - 1
    zxc.append('ветеран В.О.В')

print(zxc)
