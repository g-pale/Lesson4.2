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
    pass

bird1 = Pigeon('Гоша', 'курлык', 'серый')

bird1.sing()
bird1.info()

