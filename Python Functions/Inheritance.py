class Parent():
    def print_last_name(self):
        print('Estevez')


class Child(Parent):
    def print_first_name(self):
        print('Brandon')

brandon = Child()
brandon.print_first_name()
brandon.print_last_name()


