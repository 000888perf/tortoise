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
        self.out = 0 #小怪越刷越强
        self.out_1 = 1 #回合数
    def enemmy(self,ii,name="怪物"):#创建敌人
        self.ii=ii
        self.out+=1
        self.name_enemmy = name  # 角色名称
        self.HP_enemmy = int(((self.out-0)*15) + 10 + (3 * self.ii) * random.uniform(0.9, 1 + (self.ii * 0.2)))  # 最大血量（用于显示），血量随着时间增加并且受到随机因子波动
        self.AP_enemmy = int(((self.out*4)+ 2 + (1 * self.ii) * random.uniform(0.7, 1 + (self.ii * 0.2))))  # 当前攻击力（乌龟喷水），攻击力随着时间增加并且受到随机因子波动

    def fole(self,eat,water,sleep,ii,value,name="主角"):#乌龟
        self.name = name  # 角色名称
        self.HP = int((eat*1.3)+1)  # 最大血量（用于显示）
        self.AP = int((water/4)+1)  # 当前攻击力（乌龟喷水）
        self.EEC = sleep  # 当前行动力
        self.ii = ii  # 当前天数
        self.value = value
        self.random_number = random.randint(1, ii)  # 随机时刻

    def fire(self,eat,water,sleep,ii,value,name="主角",name_1="怪物"):
        #for i in range(1,5):
        self.enemmy(ii,name_1)
        self.fole(eat,water,sleep,ii,value,name)
        self.oe = 0



        while self.oe==0:#所有跳出条件最终都指向修改 self.oe 的值（赋值为 1/2/3/4），使其不再等于 0；

            while True:#战斗小循环
                print("所以攻击为基础数值+等级+当前数值")
                print("-" * 35,"\n"+str(self.name_enemmy), "等级:" + str(ii), "血量:" + str(self.HP_enemmy),
                      "攻击力:" + str(self.AP_enemmy)+" 回合数："+str(self.out_1))  # 最大血量（用于显示），血量随着时间增加并且受到随机因子波动

                print("“"+str(self.name)+"”", "等级"+str(self.value), "血量：" + str(self.HP), "攻击力：" + str(self.AP), "精神力：" + str(self.EEC)+"\n"+"-" * 35)
                try:
                    mode = int(input("⚔" * 28+"\n 1：普通攻击，2：喷水，3：跑路\n 请输入数字:\n" + "⚔" * 28))
                    if mode in [1, 2, 3, 4]:
                        break
                    else:
                        print(" 请输入范围内的模式")
                except ValueError:
                    print(" 请输入数字")
            if self.EEC>0 and mode == 1:#普通公鸡
                self.out_1 += 1  # 回合数+1
                HP_1 = self.HP_enemmy
                self.HP_enemmy=int(self.HP_enemmy-(15+self.AP+(self.value*2)))
                EEC_1 = self.EEC
                self.EEC-=5
                self.EEC = max(self.EEC, 0)  # 最低101

                print("（"+str(self.name)+"普通攻击造成伤害",f"{int(HP_1-self.HP_enemmy)}","消耗精力", f"{int(EEC_1 - self.EEC)}"+"）")
                if self.HP_enemmy<=0:
                    self.oe=1
                    self.out_1 = 1  # 回合数结算清零

            elif self.EEC>100 and mode==2:#技能，后面用字典做各种技能
                self.out_1 += 1  # 回合数+1
                HP_2 = self.HP_enemmy
                self.HP_enemmy = int(self.HP_enemmy -( 20+(self.AP*(self.value/2))))
                AP = self.AP
                self.AP = int(self.AP-20+int(self.AP*random.uniform(0.1, 0.10)))

                EEC_1 = self.EEC
                self.EEC -= 20+int((self.EEC*random.uniform(0.01, 0.05))+(self.AP/0.2))
                self.EEC = max(self.EEC, 1)#最低1

                print("（"+str(self.name)+"喷水攻击造成伤害", f"{int(HP_2 - self.HP_enemmy)}","损耗攻击力", f"{int(AP - self.AP)}","消耗精力", f"{int(EEC_1 - self.EEC)}"+"）")
                if self.HP_enemmy<=0:
                    self.oe = 2
                    self.out_1 = 1  # 回合数结算清零


            elif mode==3:
                self.out_1 = 1  # 回合数结算清零
                self.oe = 3

            else:
                print("            （精力不够）")
            if mode==1:#怪物反击
                HP_3 = self.HP
                self.HP=int(self.HP-self.AP_enemmy*random.uniform(0.6, 1+(self.ii*0.1)))
                print("        (被"+str(self.name_enemmy)+"伤害了",f"{HP_3-self.HP}"+")")

            if self.HP<=0:#主角死亡判定
                self.oe = 4
                self.out_1 = 1  # 回合数结算清零
                print("              （死了）")


        self.out_1 = 1
        self.HP_enemmy = 0#结束复位怪的数值
        self.AP_enemmy = 0#结束复位怪的数值
        self.HP = self.HP/1.4 #恢复数值
        self.AP = self.AP*4 #恢复数值
        self.EEC = self.EEC #恢复数值
        return self.oe,self.HP,self.AP,self.EEC



# aa=abt()#调试接口，记得关
# aa.fire(500,1,200,10,1,str("主"),str("怪"))


