class SuperHero:
    people = "people"
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def names(self):
        print("Name:", self.name)
    
    def hitpoints(self):
        self.health_points = self.health_points * 2 
        print(self.health_points, "HP")    
        
    def __str__(self) -> str:
        return f"Nickname: {self.nickname} \n"\
            f"Superpower: {self.superpower}\n"\
            f"HP: {self.health_points} "    
    
    def __len__(self):
        return len(self.catchphrase)
    
    
a = SuperHero("Chika","sultanov bnxwritecatm","suuuuuuuuuuu",15699,"writeeeeуууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууууу33333333333333333333333333333333333333333333333333333ууууууууууууууууууууууууууууууууу.")
a.names()
a.hitpoints()
print(a)
print(len(a))


#2
class Dendroheroes(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    
    def hitpoints(self):
        self.health_points = self.health_points ** 2
        self.fly = True
        print("HP:", self.health_points)
    def phrase(self):
        print(f"Hero flyes:{self.fly}")

c = Dendroheroes("Alhaitam","Haravatat","Particular Field: Fetters of Phenomena",12409,"A process of elimination.", 1333)
c.hitpoints()
c.phrase()

class AnemoHeroes(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    
    def hitpoints(self):
        self.health_points = self.health_points ** 2
        self.fly = True
        print("HP:", self.health_points)
    def phrase(self):
        print(f"Hero flyes:{self.fly}")
    
b = AnemoHeroes("Wanderer", "Scaramouche", "Kyougen: Five Ceremonial Plays", 9449, "You dare to gaze upon me!?", 1647)
b.hitpoints()
b.phrase()

class Villain(AnemoHeroes):
    people = "Monster"
    def gen_x(self):
        pass
    
    def crit_DMG(self):
        crit = self.damage ** self.damage
        print("Crit Damage:", crit)
        
d = Villain
print(d.people)
