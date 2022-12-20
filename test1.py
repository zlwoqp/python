from random import randint
import time,sys

# 玩家
class Player:

    def __init__(self,stoneNumber,warriors):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵

# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')



# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print('''
***************************************
****           游戏开始             ****
***************************************

'''
)
#(1)产生森林和妖怪.程序随机为7座森林分别产生 鹰妖或者狼妖。然后在屏幕上打印出7座森林里面的妖怪 分别是什么。注意，只显示10秒钟就会消失（这就是游戏考验玩家的记忆力，暂时可以用 打印20个换行 翻屏实现）。
# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '
print('注意：十秒后内容消失\n')
      

# 显示 妖怪信息
print(notification,end='')
#打印20个换行 翻屏实现
for i in range(20):
    print('\n')

#(2)雇佣战士玩家有 1000 灵石，让玩家根据自己记忆的妖怪种类和数量，选择雇佣多少个弓箭兵和斧头兵。每雇佣一个士兵，给他起一个名字。
player1 = Player()
print(f'你有{player1.stoneNumber},准备开始雇佣士兵')
print('雇佣战士')
while True:
    Warrior_type = input('请输入您想雇佣的士兵\n  输入2雇佣斧头兵\n 输入3雇佣弓箭兵\n')
    if Warrior_type.isdigit():
        Warrior_type = int(Warrior_type)
        if Warrior_type == 2:
            name1 = input('请给您的斧头兵取个名字\n')
            player1.hire(Axeman(name))
        elif Warrior_type == 3:
            name2 = input('给您的弓箭兵取个名字\n')
            player1.hire(Archer(name))
            break
print(player1.stoneNumber)

#(3)然后开始征途，要通过7座森林，系统不会提示你森林里面是什么妖怪（玩家凭记忆回想），每座森林只能派出一个战士去消灭里面的妖怪，让玩家选择派出哪个战士。
print('开始闯关')
print('欢迎来到第{i+1}关')
while True:
    warriors= input('请选择士兵')
    if warriors == 'warriors':
        for m in player1.warriors.keys():
             print(m)
    elif strength > 0:
        print('闯关成功')
                         
    else:
        if strength< 0:
            print('闯关失败')
            break
