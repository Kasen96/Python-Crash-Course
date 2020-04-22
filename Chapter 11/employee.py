# 11-3

class Employee():

    def __init__(self, last_name, first_name, wage):
        self.last_name = last_name
        self.first_name = first_name
        self.wage = wage

    def give_raise(self, wage=''):
        if wage:
            self.wage += int(wage)
        else:
            self.wage += 5000
