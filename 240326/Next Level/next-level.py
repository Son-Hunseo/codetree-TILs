id, level = map(str, input().split())
level = int(level)

class user:
    def __init__(self, id: str="codetree", level: int=10):
        self.id: str = id
        self.level: int = level

    def printdata(self):
        print("user "+self.id+" lv "+str(self.level))

user1 = user()
user1.printdata()

user2 = user(id, level)
user2.printdata()