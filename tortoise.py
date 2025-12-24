import random
import battle


def random_1():
    random_number_1 = 0
    state_1 = 0
    random_number_1=random.randint(1, 100)
    if random_number_1<30:
        state_1=1
    elif 30 <= random_number_1 <= 80:
        state_1=2
    elif 80 < random_number_1 <= 100:
        state_1=3
    return random_number_1,state_1

class tti:
    life = True
    def __init__(self):
        self.value=1#基础等级
        self.eat = 50#基础饱腹感
        self.water = 50#基础解渴度
        self.sleep = 50#基础解乏度
        self.life = True#死亡状态
        self.i = 3#行动数
        self.ii = 1#天数
        self.level = 1 #乌龟等级
        self.die =0#死亡判断
        self.death = 0#死亡选择
        self.life_or_death = 0 #战斗是否死亡判断

        print("/*创建乌龟实例")
    def do_eat(self,random_number):#吃饭函数
        self.eat=min(self.eat+50+random_number,self.level*100)
        self.i -= 1
        print(" "*10+"(乌龟吃饭)"+" "*10)
    def do_water(self,random_number):#喝水函数
        self.water=min(self.water+50+random_number,self.level*100)
        self.i -= 1
        print(" "*10+"(乌龟喝水)"+" "*10)
    def do_sleep(self,random_number):#睡觉函数
        self.sleep=min(self.sleep+50+random_number,int(self.level*100))
        self.i -= 1
        print(" "*10+"(乌龟睡觉)"+" "*10)
    def do_day(self):#每日结算
        self.eat-=20
        self.water-=20
        self.sleep-=20
        self.i = 3
        self.ii += 1
        print("结束一天")
        print("?",self.eat,self.water,self.sleep)
        self.die_1()

    def die_1(self,life_or_death=0):#判断死亡原因，死亡判断，如果死了抛出self.life = False
        self.death="未知原因"

        if self.eat<-1 or self.water<-1 or self.sleep<-1 or life_or_death==4:#死亡判断
            death_reasons = []#用列表的方式来获取死亡原因
            if self.eat < -1:
                death_reasons.append("饥饿")
                self.life = False
            elif self.water < -1:
                death_reasons.append("缺水")
                self.life = False
            elif self.sleep < -1:
                death_reasons.append("缺觉")
                self.life = False
            elif life_or_death == 4:
                death_reasons.append("打不过")
                self.life = False

            self.death=",".join(death_reasons) if death_reasons else "未知原因"

        if self.life == False:
            print("乌龟死了，死于"+str(self.death))

tortoise=tti()#每次重开都从新载入(懒还是算了)
battle_1=battle.abt()#传入乌龟战斗类

while True:

    while tortoise.life:#死亡判断抛出假的时候，会跳出，然后进入从开判断
        print("-"*35,"\n","    （乌龟任一数值小于0都会死）","\n",
              " 吃饭"+str(tortoise.eat)+"/"+str(tortoise.level*100),"喝水"+str(tortoise.water)+"/"+str(tortoise.level*100),"睡觉"+str(tortoise.sleep)+"/"+str(tortoise.level*100),"等级："+str(tortoise.level),"剩余次数"+str(tortoise.i),"天数"+str(tortoise.ii))
        while True:

            try:
                mode=int(input(" 1：投喂，2：喝水，3：睡觉，4：结束这一天\n 5：战斗（吃喝睡都是战斗的属性） \n 请输入数字:\n"+"-"*35))
                if mode in [1,2,3,4,5]:
                    break
                else:
                    print(" 请输入范围内的模式")
            except ValueError:
                print(" 请输入数字")

        random_number,state = random_1()
        stare = state
        random_number = random_number
        if tortoise.i>0 and mode==1:
            tortoise.do_eat(random_number)
            print(("  (吃的差，额外饱腹感"+str(random_number))+")" if state==1 else("  (吃的简简单单，额外饱腹感"+str(random_number)+")") if state==2 else "  (吃的不错，额外饱腹感"+str(random_number)+")")

        elif tortoise.i>0 and mode==2:
            tortoise.do_water(random_number)
            print(("  (喝的差，额外解渴度"+str(random_number))+")" if state==1 else ("  (喝的简简单单，额外解渴度"+str(random_number)+")") if state==2 else "  (喝的不错，额外解渴度"+str(random_number)+")")

        elif tortoise.i>0 and mode==3:
            tortoise.do_sleep(random_number)
            print(("  (睡的差，额外解乏感"+str(random_number))+")" if state==1 else ("  (睡的简简单单，额外解乏感"+str(random_number)+")") if state==2 else "  (睡的不错，额外解乏感"+str(random_number)+")")

        elif mode==4:
            tortoise.do_day()

        elif mode==5:
            tortoise.ii=1#调试等级
            tortoise.life_or_death,tortoise.eat,tortoise.water,tortoise.sleep=battle_1.fire(tortoise.eat,tortoise.water,tortoise.sleep,tortoise.ii,tortoise.level)#战斗(血量，攻击力，蓝量，天数，等级)
            if tortoise.life_or_death in [1,2]:
                tortoise.level+=1
                print("普通攻击击败敌人，等级+1")
            elif tortoise.life_or_death in [3]:

                print("艰难跑路")
            elif tortoise.life_or_death in [4]:

                tortoise.life = False
                tortoise.die_1(tortoise.life_or_death)



        else:
            print("没行动力了，结束这一天吧")

    if not tortoise.life:
        tortoise.life = True
        while True:
            try:
                tortoise.die = int(input("是否结束 （1：继续，2：结束）"))
                if tortoise.die in [1, 2]:
                    break
                else:
                    print("请输入范围内的选择")
            except ValueError:
                print("请输入数字")
        if tortoise.die == 1:
            print("-" * 10 + "换新乌龟" + "-" * 10)
            tortoise.eat = 50
            tortoise.water = 50
            tortoise.sleep = 50
            tortoise.ii = 0

            tortoise.die = 0

        elif tortoise.die == 2:
            print("-" * 10 + "丢弃乌龟" + "-" * 10)
            day = round(((tortoise.ii + 1) / (356 * 25)) * 100,6)
            print("乌龟活了" + str(tortoise.ii) + "天，度过了其他龟龟生命的" + str(day) + "%")

            tortoise.die = 0
            break

print("游戏结束")

