from random import randrange as rnd, choice
import tkinter as tk
import math
import time 


def main():
    global root, canv, targets
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
    #bullets = [] FIXME: реализавать пули
    #guns = [] FIXME: реализавать несколько стволов
    root.mainloop()

def move_targets():
    for i in targets:
        i.move()
    root.after(50,move_targets)
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
        pass
    def get_state(self):
        """
            Возвращает состояние мишени
        """
        pass
    
    
class Bullet:
    """
        Класс пули    
    """
    def __init__(self,x=40,y=50):
        x = self.x = x
        y = self.y = y
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
            Двигает пулю
        """
        if self.x+self.r > 800:  
            self.direction = -self.directionX
        if self.x-self.r < 0:
            canv.delete(self.bullet)
        if self.y+self.r > 600:  
            self.direction = -self.directionY
        if self.y-self.r < 0:
            self.direction = -self.directionY
        canv.delete(self.target)
        self.x -= self.vx * self.directionX
        self.y -= self.vy * self.directionY
        canv.move(self.target,self.x,self.y)
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
    def check_hit(self):
        """
            Проверяет поподание в мишень
        """
        a = abs(clicX-(objX+(this['size']/2)))
        b = abs(clicY-(objY+(this['size']/2)))
        r1 = math.sqrt((a**2)+(b**2))
        if r1 <= self.r:
            returnt True
        return False
    
class Gun:
    """
        Класс оружия
    
    """    
    def __init__(self):
        pass

    def new_gun(self):
        """
            Создаёт новый ствол
        """
    def targetting(self):
        """
            Производит прицеливание
        """
        pass
    def strat_fire(self):
        
        """
            Взводит флаг начала зарядки выстрела
        """
    def end_fire(self):
        
        """
            Опускает флаг начала зарядки выстрела
        """
    def power_up(self):
        
        """
            Увеличивает силу выстрела до возможного предела
        """



if __name__ == "__main__":
    main()
else:
    print("GO TO FAT ASS")
