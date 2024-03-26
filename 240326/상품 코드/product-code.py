class product:
    def __init__(self, name:str="codetree", code:int=50):
        self.name:str = name
        self.code:int = code
    
    def tell(self):
        print("product", self.code, "is", self.name)

product1 = product()
product1.tell()

name, code = map(str, input().split())
code = int(code)

product2 = product(name, code)
product2.tell()