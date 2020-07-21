from random import randrange as rnd, choice
import tkinter as tk
import math
import time 


def main():
    global root, canv, targets, bullets
    """
    главня функция
    
    """
    root = tk.Tk()
    root.geometry('800x600')
    canv = tk.Canvas(root, bg='white')
    canv.pack(fill=tk.BOTH, expand=1)
    targets = []
    for i in range(3):
        t = Target()
        t.new_target()
        targets.append(t)
    move_targets()
    gun1 = Gun()
    canv.bind('<Button-1>', gun1.strat_fire)
    canv.bind('<ButtonRelease-1>', gun1.end_fire)
    canv.bind('<Motion>', gun1.targetting)
    bullets = [] 
    move_bullets()
    #ids = [] FIXME: реализавать несколько стволов
    root.mainloop()
    while(len(targets) > 0):
        if (gun1.fire_on == True):
            gun1.power_up()
        for i in range(len(targets) - 1):
            gun1.power_up()
            for b in bullets:
                gun1.power_up()
                if b.check_hit(targets[i],i):
                    gun1.power_up()
                    i = i-1

def move_targets():
    for i in targets:
        i.move()
    root.after(50,move_targets)
def move_bullets():
    for i in bullets:
        
        i.move()
    root.after(50,move_bullets)

class Target:
    """
        Класс мишени
    
    """
    def __init__(self):
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        self.vx = rnd(7,22)
        self.vy = rnd(3,30)
        colors = ['red','green', 'blue']
        color = self.color = choice(colors)
        self.state = 22
        self.direction = 1

    def new_target(self):
        """
            Создаёт новую мишень
        """
        x = self.x
        y = self.y
        r = self.r
        color = self.color
        self.target = canv.create_oval(x-r,y-r,x+r,y+r, fill=color)
        
    def move(self):
        """
            Двигает мишень
        """
        if self.y+self.r > 600:  
            self.direction = -self.direction
        if self.y-self.r < 0:
            self.direction = -self.direction
        canv.delete(self.target)
        self.y -= self.vy * self.direction
        canv.move(self.target,self.x,self.y)
        self.target = canv.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r, fill=self.color)
    def set_state(self,x):
        """
            Установить состояние мишени
        """
        self.state = x
    def get_state(self):
        """
            Возвращает состояние мишени
        """
        if state == 1:
            return True
        elif state == 0:
            return False
    
    
class Bullet:
    """
        Класс пули    
    """
    def __init__(self,x=40,y=450):
        self.x = x
        self.y = y
        r = self.r = 10
        self.vx = 0
        self.vy = 0
        colors = ['red','green', 'blue', 'green','black', 'orange']
        color = self.color = choice(colors)
        self.directionX = 1
        self.directionY = 1
        self.bullet = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30
        
        

    def move(self):
        """
        FIXME: Движение пуль поразной траектории
            Двигает пулю
        """
        if self.x >= 800:  
            #print('r')
            self.directionX = -self.directionX
        if self.x <= 0:
            canv.delete(self.bullet)
        if self.y >= 600:  
            #print('d')
            self.directionY = -self.directionY
        if self.y < 0:
            self.directionY = -self.directionY
        canv.delete(self.bullet)
        self.x = self.x + self.vx * self.directionX
        self.y = self.y - self.vy * self.directionY
        #canv.move(self.target,self.x,self.y)
        self.bullet = canv.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r, fill=self.color)
    def set_state(self,x):
        self.live = x
        
            
    def get_state(self):
        return self.live
        
        
    def delete_yourself(self):
        """
            Удаляет пулю
        """
        canv.delete(self.bullet)
    def check_hit(self, obj, n):
        global targets
        """
            Проверяет поподание в мишень
        """
        length = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5

        return length <= self.r + obj.r
    
class Gun:
    """
        Класс оружия
    
    """    
    def __init__(self):
        """
        Иницилизирует переменные стандартными значениями
        
        
        self.x =  координата x
        self.y =  координата y
        self.a = альфа
        self.id = ствол
        self.f2_power = сила выстрела
        self.fire_on = идёт сейчас выстрел или нет
        self.x1 = координата x1
        self.y1 = координата y1

        
        """
        self.x =  0
        self.y =  450   
        self.a = 0
        self.id = canv.create_line(self.x, self.y, self.x+20, self.y, width=6, fill="black")
        self.f2_power = 10
        self.fire_on = False
        self.x1 = 0
        self.y1 = 0

    def targetting(self, event):
        """
            Производит прицеливание
        """
        
        #print(self.a)
        self.a = math.atan2(self.y, self.x) - math.atan2(event.y, event.x)
        a = abs(event.x - self.x)
        b = abs(self.y - event.y)
        
        r1 = math.sqrt((a*a)+(b*b))
        #print(a,b)
        x = a/r1*20
        y = 0
        if self.y < event.y:
            y = b/r1*20+self.y
        elif self.y > event.y:
            y = (-b)/r1*20+self.y
        
        #print(y)
        self.x1 = x
        self.y1 = y
        canv.delete(self.id)
        if self.fire_on == False:
            self.id = canv.create_line(self.x, self.y, x, y, width=6, fill="black")
        elif self.fire_on == True:
            self.id = canv.create_line(self.x, self.y, x+self.f2_power, y, width=6, fill="orange")
            


    def strat_fire(self, event):
        """
            Взводит флаг начала зарядки выстрела
        """
        self.fire_on = True
    def end_fire(self, event):
        global bullets, Bullet
        """
            Опускает флаг начала зарядки выстрела
        """
        self.fire_on = False
        new_bullet = Bullet(self.x1, self.y1)
        new_bullet.r += 5
        new_bullet.vx = self.f2_power * 2
        new_bullet.vy =  self.f2_power * 2
        print(new_bullet.vx)
        print(new_bullet.vy)
        bullets.append(new_bullet)
        self.fire_on = False
        self.f2_power = 10
    def power_up(self):
        """
            Увеличивает силу выстрела до возможного предела
            Если выстрел происходит то увеличивает силу выстрела на десять каждый такт цикла
            если нет то ничего не делает
        """
        global canv
        canv.delete(self.id)
        self.a = math.atan2(self.y, self.x) - math.atan2(event.y, event.x)
        a = abs(event.x - self.x)
        b = abs(self.y - event.y)
        
        r1 = math.sqrt((a*a)+(b*b))
        #print(a,b)
        x = a/r1*20
        y = 0
        if self.y < event.y:
            y = b/r1*20+self.y
        elif self.y > event.y:
            y = (-b)/r1*20+self.y
        
        #print(y)
        self.x1 = x
        self.y1 = y
        if self.fire_on == True:
            print("ubgrade powe")
            if self.f2_power < 400:
                self.f2_power +=10
            self.id = canv.create_line(self.x, self.y, x+self.f2_power, y, width=6, fill="orange")

        else:
            self.id = canv.create_line(self.x, self.y, x, y, width=6, fill="black")
            

if __name__ == "__main__":
    main()
else:
    print("GO TO FAT ASS")
