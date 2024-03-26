n = int(input())

class person_data:
    def __init__(self, name:str, loca_num:str, location:str):
        self.name:str = name
        self.loca_num:str = loca_num
        self.location:str = location
    
    def tell(self):
        print("name", name)
        print("addr", loca_num)
        print("city", location)

person_datas = []

max_name = "a"
max_idx = 100

for i in range(n):
    name, loca_num, location = map(str, input().split())
    if name > max_name:
        max_name = name
        max_idx = i
    person_datas.append(person_data(name, loca_num, location))

person_datas[max_idx].tell()