import json,subprocess
data = {"average":[],"max":[],"min":[],"open":[],"close":[]}
n = open("setting.tr","r").read().split(",")[0]
with open(f"DATA/{n}/input.scd","r") as datas:
    origin = datas.read().split(";")
    for i in origin:
        total = list(map(float,i.split(",")))
        data["average"].append(sum(total)/len(total))
        data["max"].append(max(total))
        data["min"].append(min(total))
        data["open"].append(total[0])
        data["close"].append(total[-1])
with open("DATA/graph.json","w") as file:
    dataToShare = []
    for j in range(len(data["average"])):
        dataToShare.append({
            "average":data["average"][j],
            "max":data["max"][j],
            "min":data["min"][j],
            "open":data["open"][j],
            "close":data["close"][j]
        })
    file.write(str(json.dumps(dataToShare)))
subprocess.run(["python", "graphRender.py"])