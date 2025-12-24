import random

class abt:#tortoise属性
    def __init__(self):
        self.name = "name"  # 角色名称
        self.HP = 0  # 最大血量（用于显示）
        self.AP = 0  # 当前攻击力（乌龟喷水）
        self.EEC = 0  # 当前行动力
        self.ii= 0 #当前天数
        self.random_number = 0 #随机时刻
        self.name_enemmy = "name"  # 角色名称
        self.HP_enemmy = 0  # 最大血量（用于显示）
        self.AP_enemmy = 0  #攻击力
    def enemmy(self,ii,name="怪物"):#创建敌人
        self.ii=ii+1
        self.name_enemmy = name  # 角色名称
        self.HP_enemmy = int((10+(5*self.ii))*random.uniform(0.9, 1+(self.ii*0.2)))  # 最大血量（用于显示），血量随着时间增加并且受到随机因子波动
        self.AP_enemmy = int((2+(2*self.ii))*random.uniform(0.9, 1+(self.ii*0.1)))  # 当前攻击力（乌龟喷水），攻击力随着时间增加并且受到随机因子波动

    def fole(self,eat,water,sleep,ii,name="主角"):#乌龟
        self.name = name  # 角色名称
        self.HP = eat  # 最大血量（用于显示）
        self.AP = water  # 当前攻击力（乌龟喷水）
        self.EEC = sleep  # 当前行动力
        self.ii = ii  # 当前天数
        self.random_number = random.randint(1, ii)  # 随机时刻

    def fire(self,eat,water,sleep,ii,name="主角",name_1="怪物"):
        #for i in range(1,5):
        self.enemmy(ii,name_1)
        self.fole(eat,water,sleep,ii,name)
        self.oe = 0
        mode_1 = 0
        HP_1 = 0
        HP_2 = 0
        HP_3 = 0
        EEC_1 = 0
        print(self.name_enemmy,"等级:"+str(ii))
        print(self.name, "HP："+str(self.HP), "AP："+str(self.AP), "MP："+str(self.EEC))

        while self.oe==0:

            while True:#战斗小循环

                try:
                    mode = int(input("-" * 35+"\n 1：普通，2：技能，3：跑路\n 请输入数字:\n" + "-" * 35))
                    if mode in [1, 2, 3, 4]:
                        break
                    else:
                        print(" 请输入范围内的模式")
                except ValueError:
                    print(" 请输入数字")
            if self.EEC>0 and mode == 1:#普通公鸡
                HP_1 = self.HP_enemmy
                self.HP_enemmy=int(self.HP_enemmy-self.AP)
                EEC_1 = self.EEC
                self.EEC-=20
                self.EEC = max(self.EEC, 0)  # 最低101
                mode_1 = 1
                print("mode1")
                print(str(self.name)+"造成伤害",f"{int(HP_1-self.HP_enemmy)}","扣除精力", f"{int(EEC_1 - self.EEC)}")
                if self.HP_enemmy<=0:
                    self.oe=1

            elif self.EEC>100 and mode==2:#技能，后面用字典做各种技能
                HP_2 = self.HP_enemmy
                self.HP_enemmy = int(self.HP_enemmy - self.AP)
                EEC_1 = 0
                EEC_1 = self.EEC
                self.EEC -= 20+int(self.EEC*random.uniform(0.01, 0.05))
                self.EEC = max(self.EEC, 1)#最低1
                mode_1=1
                print("mode2")
                print(str(self.name_enemmy)+"造成伤害", f"{int(HP_2 - self.HP_enemmy)}","扣除精力", f"{int(EEC_1 - self.EEC)}")
                if self.HP_enemmy<=0:
                    self.oe = 2


            elif mode==3:
                print("mode3")
                self.oe = 3

            else:
                print("没有精力了")
            if mode==1:
                HP_3 = self.HP
                self.HP=int(self.HP-self.AP_enemmy*random.uniform(0.6, 1+(self.ii*0.1)))
                print("被"+str(self.name_enemmy)+"伤害了",f"{HP_3-self.HP}")
                mode_2=0
            if self.HP<=0:
                self.oe = 4

            print(self.name_enemmy, "HP：" + str(self.HP_enemmy), "AP：" + str(self.AP_enemmy))
            print(self.name, "HP：" + str(self.HP), "AP：" + str(self.AP), "MP：" + str(self.EEC))
        return self.oe


# aa=abt()#调试接口，记得关
# aa.fire(500,1,200,100,str("主"),str("怪"))


