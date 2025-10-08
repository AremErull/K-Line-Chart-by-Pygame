import json,pygame,sys
from tkinter import messagebox,Tk
root = Tk()
root.withdraw()
MAX = max
MIN = min
n = open("option.txt","r").read()
proportion = float(n.split(",")[1])
with open("DATA/graph.json","r") as file:
    read = file.read()
if read != "":
    data = json.loads(read);pygame.init()
    screen = pygame.display.set_mode((960,560))
    pygame.display.set_caption("K-Line Chart")
    data = data[-60:]
    avg = []
    min = []
    max = []
    op = []
    cl = []
    for i in range(len(data)):
        avg.append(data[i]["average"])
        min.append(data[i]["min"])
        max.append(data[i]["max"])
        op.append(data[i]["open"])
        cl.append(data[i]["close"])
    pygame.draw.line(screen,(255,255,255),(10,550),(950,550),1)
    for i in range(len(data)):
        re = (4+i*15,MIN(550-op[i]/proportion,550-cl[i]/proportion),12,abs(op[i]/proportion-cl[i]/proportion))
        if avg[i] >= avg[i-1]:
            c = (255,100,100)
            pygame.draw.rect(screen,c,re,1)
        else:
            c = (100,255,100)
            pygame.draw.rect(screen,c,re)
        pygame.draw.line(screen,c,(10+i*15,550-min[i]/proportion),(10+i*15,550-max[i]/proportion),1)
    for i in range(len(data)-1):
        pygame.draw.line(screen,(250,250,250),(10+i*15,550-avg[i]/proportion),(25+i*15,550-avg[i+1]/proportion),1)
    pygame.display.flip()
    q = n.split(",")[0]
    with open(f"DATA/{q}/history.txt","r") as f:
        value = 0
        volume = 0
        reading = f.read()
        if reading != "":
            shops = reading.split(";")
            for i in shops:
                volume += int(i.split(",")[0])
                value += int(i.split(",")[0])*int(i.split(",")[1])
        print("当前总收益",volume*cl[-1]-value)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
else:

    messagebox.showerror("Error","No data to graph")

