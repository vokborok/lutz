class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay*(1+percent))
    def __repr__(self):
        return 'Person: %s, %s' % (self.name, self.pay)

if __name__ ==  '__main__':
    bob = Person('Sponge Bob')
    sue = Person('Sue Sue', job='dev', pay=2000)
    print bob.name, bob.job, bob.pay
    print sue.name, sue.job, sue.pay
    print bob.lastName()
    sue.giveRaise(.10)
    print sue.pay
    print sue
