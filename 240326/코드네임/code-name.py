class Agent:
    def __init__(self, name:str, score:int):
        self.name:str = name
        self.score:int = score

data = []
min_score = 101
min_idx = 999
for i in range(5):
    name, score = map(str, input().split())
    score = int(score)
    if score < min_score:
        min_score = score
        min_idx = i
    data.append(Agent(name, score))

print(data[min_idx].name, data[min_idx].score)