# 1 наследование - полное или частичное копирование\наследование всех методов и аргументов
# 2 полиморфизм изменение поведения унаследованный методов


# 3 инкапсуляция

class A:  # супер класс
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'my name is {self.name}\n'
              f'age is {self.age}')


# a = A('beka', 19)
# a.info()


# дочерний класс (А)
class B(A):
    def best(self):
        self.age *= 2
        print(self.age)


class C(B):
    def __init__(self,name,age,lastname):
        # B.__init__(self,name,age)
        super().__init__(name,age)
        self.last=lastname


    def num(self):
        self.age -= self.age / 2
        print(self.age,'умножаю ')

    def metod(self):
        # B.best(self)
        super().best()
        self.best()
        self.num()
        self.info()

    def best(self):
        self.age **= 20
        print(f"{self.age} возвожу в степень")

    def info(self):
        super().info()
        print(f'my last {self.last}')


b = B('николай', 10)
# b.best()
c = C('Atai', 10,'Мырзаев')
c.metod()