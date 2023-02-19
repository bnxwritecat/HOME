class SuperHero:
    people='people' 
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name=name
        self.nicname=nickname
        self.superpower=superpower
        self.health_points=health_points
        self.catchphrase=catchphrase
    def  info(self):
        return f'{self.name}catchphrase :{self.catchphrase}'
    def healthpoints(self):
        return f"{self.name} его хп {self.health_points*2}"
    def str(self):
        return f"nicname:{self.nicname},superpower(self.superpower), health: {self.health_points}, catchphrase: {self.catchphrase}"
    def len(self):
        return len(self.catchphrase)

class NewSuper(SuperHero):
    def init(self, name, nickname, supername, health_points, catchphrase) -> None:
         super().init(name, nickname, supername, health_points, catchphrase)
         self.damage = False
         self.fly = False
    def kvodrat(self):
        self.fly = True
        return f"Квадрат: {self.health_points,*2}, Fly: {self.fly}"
    def newmetod(self):
        return f"newdamage: {self.damage}, newfly: {self.fly}"
    def flyg(self):
        return f"catchphrase: {self.catchphrase}"
newsuper = NewSuper("chiken", "spotify", "web",60,"fly in the True phrase")
print(newsuper.kvodrat())
print(newsuper.flyg())
print(newsuper.newmetod())
class Villain(SuperHero):
    people = "monstr"
    def gen_x(self):
        pass
    def crit(self,damage1,damage2):
        return f"uron: {damage1 ,damage2}"
villain = Villain("nurbolot", "kot", "sperma",100,"sperma man")
print(villain.crit(6,10))