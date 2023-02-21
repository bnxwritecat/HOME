# class Boss:
#     people = "people" # атрибуты 
#     def a(self,name,first_name, nickname, hilpoint, damage):#метод
#         return f"name: {name}, f-name: {first_name}, nickname:{nickname}, hilpoint:{hilpoint}, damage: {damage}"
# boss = Boss()
# print(boss.a("rig","dark","tom", 100,22))
# print(boss.people)


# class HelloWorld(): #Создаем класс HelloWorld
#     name = "Adilet" #Создаем атрибут name
#     age = 16 #Создаем атрибут age

#     def walk(self): #Создаем метод walk
#         return "Ходить"

#     def run(self): #Создаем метод run
#         return "Бегать"

#     def info(self): #Создаем метод info
#         return f"Имя: {self.name}, возраст {self.age}"

# hello = HelloWorld() #Создаем экземпляр класса
# print(hello.walk()) #Вызываем метод walk
# print(hello.run()) #Вызываем метод run
# # print(hello.name)
# # print(hello.age)
# print(hello.info())

# Статические поля (поля класса) можно использовать без создания объекта. А значит, конструктор вам не нужен.

# Динамические поля (поля объекта) задаются с помощью конструктора, и тут уже, как вы видели, экземпляр нужно создать, а полям присвоить значения.

# class Person(): #Создаем динамический класс Person
#     def init(self, name, surname, age): #Создаем конструктор
#         self.name = name 
#         self.surname = surname 
#         self.age = age 

#     def walk(self): #Создаем метод walk
#         return f"{self.name} гуляет"

#     def run(self): #Создаем метод run
#         return f"{self.name} бегает"

#     def info(self): #Создаем метод info
#         return f"Имя {self.name}, фамилия {self.surname}, возраст {self.age}"

# adilet = Person("Adilet", "Python", 17) #Создаем экземпляр класса
# print(adilet.info())
# print(adilet.walk())
# print(adilet.run())
# kurmanbek = Person("Kurmanbek", "Toktorov", 18)
# print(kurmanbek.info())

class Car():
    def init(self, brand, model, year,color, type, volume):
        self.brand = brand 
        self.model = model 
        self.year = year 
        self.color = color 
        self.type = type 
        self.volume = volume 
        self.odometer = 0
        self.is_going = False 

    def info_car(self):
        return f"Brand {self.brand}, model {self.model}, year {self.year}, type {self.type}, volume {self.volume}, {self.odometer} km, status {self.is_going}"

    def start_engine(self):
        self.is_going = True 
        return f"{self.brand} {self.model} заведена"

    def drive(self, km):
        if self.is_going == True:
            self.odometer += km 
            return f"Вы проехали на машине {km} 1000000 км"
        else:
            return "Вы не завели машину"

    def stop_engine(self):
        self.is_going = False 
        return "Вы заглушили машину"

mersedes = Car("Mersedes", "W223", 2022, "White", "Sedan", 3.0)
print(mersedes.info_car())
print(mersedes.start_engine())
print(mersedes.info_car())
print(mersedes.drive(20))
print(mersedes.info_car())
print(mersedes.stop_engine())
print(mersedes.info_car())
