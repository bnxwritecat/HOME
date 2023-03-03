
#########################################################
class A:
    def __init__(self,name) -> None:
        self.name = name
class B:
    def __init__(self,age) -> None:
        self.age = age
class C:
    def A():
        pass
class D:
    def B():
        pass
class Ask(A,B,C,D):
    def __init__(self, name,age) -> None:
        A.__init__(self,name)
        B.__init__(self,age)
    def __str__(self) -> str:
        return f"{self.name}, {self.age}"
ask = Ask("chika",18)
print(ask)