class people():
    def __init__(self, name):
        self.name = name
        pass
    def talk(self, talks):
        self.talks = talks
        print(talks)
        pass


christian = people('christian')
christian.talk(f'hi, i am {christian.name}')
bob = people('bob smith')
bob.talk(f'hi, i am {bob.name}')