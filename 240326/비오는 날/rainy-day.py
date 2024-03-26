class weather_data:
    def __init__(self, day:str, date:str, weather:str):
        self.day:str = day
        self.date:str = date
        self.weather = weather
    
    def tell(self):
        print(self.day, self.date, self.weather)

n = int(input())

data = []
rain_idx = 0
rain_min = "9999-99-99"
for i in range(n):
    day, date, weather = map(str, input().split())
    if day < rain_min and weather == "Rain":
        rain_min = day
        rain_idx = i
    data.append(weather_data(day, date, weather))

data[rain_idx].tell()