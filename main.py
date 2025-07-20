class Bird():
    def __init__(self, name, voice, colour):
        self.name = name
        self.voice = voice
        self.colour = colour

    def fly(self):
        print(f'{self.name} летает')

    def eat(self):
        print(f'{self.name} кушает')

    def sing(self):
        print(f'{self.name} поёт {self.voice}')

    def info(self):
        print(f'{self.name} имя')
        print(f'{self.voice} голос')
        print(f'{self.colour} окрас')

class Pigeon(Bird):
    def __init__(self, name, voice, colour, favourite_food):
        super().__init__(name, voice, colour)
        self.favourite_food = favourite_food

    def sing(self):
        print(f'{self.name} курлык')

    def walk(self):
        print(f'{self.name} гуляет')


bird1 = Pigeon('Гоша', 'курлык', 'серый', 'хлебные крошки')
bird2 = Bird('Маша', 'чирик', 'коричневый')

bird1.sing()
bird1.info()
bird1.walk()

bird2.info()
