class Base:

    def superToto(self):
        return 'supertoto'

class SecondBase:

    def superTiti(self):
        return 'supertiti'

class Toto(Base, SecondBase):

    def __init__(self):
        print(self.superToto())
        print(self.superTiti())