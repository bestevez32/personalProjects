class Enemy:
    life = 5

    def attack(self):
        print('You hit me!')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('You slay your enemy')
        else:
            print(str(self.life) + " life remaining")

enemy1 = Enemy()
enemy2 = Enemy()
enemy1.attack()
enemy2.attack()
enemy1.checkLife()
enemy2.checkLife()

