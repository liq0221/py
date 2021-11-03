import random

class BakedSweetPotato():
        
    def __init__(self):
        self.cookLevel = 0
        self.cookStr = "生的"
        self.condiments = []
    def __str__(self):
        print("这个地瓜是【%s】,配料有【%s】"%(self.cookStr,self.condiments))
    
    def cook(self, time):
        self.cookLevel += time
        if 0 <= self.cookLevel < 3:
            self.cookStr = "生的"
        elif 3 < self.cookLevel <= 5:
            self.cookStr = "半生不熟"
        elif 5 < self.cookLevel <= 8:
            self.cookStr = "烤好了"
        else:
            self.cookStr = "烤成碳了"
            
    def auto_cook(self, time):
        self.cookLevel = time
        while True: 
            if 0 <= self.cookLevel <= 5:
                self.cookLevel += 1
            elif 5 < self.cookLevel <= 8:
                self.cookStr = "烤好了"
                break
            else:
                self.cookStr = "早就烤成炭了，无法使用自动烤的方法"
                break
    def addCondiments(self, ele):
        self.condiments.append(ele)
    def auto_addCondiments(self):
        randomCondiments = ["番茄酱", "沙拉酱", "芥末酱", "辣椒酱"]
        self.condiments.append(randomCondiments[random.randint(0,3)])


yarm = BakedSweetPotato()

yarm.cook(1)
yarm.addCondiments("芥末酱")
yarm.__str__()
yarm.auto_cook(15)
yarm.auto_addCondiments()
yarm.__str__()