code, place, time = map(str, input().split())
time = int(time)

class secret:
    def __init__(self, code:str, place:str, time:int):
        self.code:str = code
        self.place:str = place
        self.time:int = time
    
    def tell(self):
        print("secret code : "+self.code)
        print("meeting point : "+self.place)
        print("time : "+str(self.time))

secret1 = secret(code, place, time)
secret1.tell()