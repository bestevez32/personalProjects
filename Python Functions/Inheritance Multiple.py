class Human():
    def language(self):
        print('I can speak')

class Gender():
    def my_gender(self):
        print('I am male')

class Preference():
    def favorite_food(self):
        print('I like pizza')

class humanMale(Human, Gender, Preference):
    pass

hM = humanMale()
hM.language()
hM.my_gender()
hM.favorite_food()



