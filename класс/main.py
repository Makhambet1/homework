class stydent():
    def __init__(self, name, surname, age, group):
        self.name = name
        self.surname = surname
        self.age = age
        self.group = group

    def info(self):
        return 'Имя:' + (self.name) + '\nФамиля:' + (self.surname) + '\nВозраст:' + (self.age) + '\nГруппа:' + (
            self.group) + '\n >>>>>>>>>>>'


stydent1 = stydent("Махамбет", "Маскар", "+18+", "АиУп-19р/о")
stydent2 = stydent("Азамат", "Амантайулы ", "18", "АиУп-19р/о")
stydent3 = stydent("Нурболат", "Жабасов ", "18", "АиУп-19р/о")
stydent4 = stydent("Султанбек", "Женисбеков ", "19", "АиУп-19р/о")

print(stydent1.info())
print(stydent2.info())
print(stydent3.info())
print(stydent4.info())