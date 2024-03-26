class bomb:
    def __init__(self, code:str, color:str, time:int):
        self.code:str = code
        self.color:str = color
        self.time:int = time

    def telldata(self):
        print('code :', code)
        print('color :', color)
        print('second :', time)

code, color, time = map(str, input().split())
time = int(time)

bomb1 = bomb(code, color, time)
bomb1.telldata()