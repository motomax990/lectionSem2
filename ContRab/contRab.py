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
        self.vx = rnd(5,11)
        self.vy = rnd(5,11)
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
    def set_set(self,x):
        """
            Установить состояние мишени
        """
        pass
    def get_set(self):
        """
            Возвращает состояние мишени
        """
        pass
    
    
class Bullet:
    """
        Класс пули    
    """
    def __init__(self):
        pass
    def new_bullet(self):
        """
            Создаёт новую пулю
        """
        pass
    def move(self):
        """
            Двигает пулю
        """
    def delete_yourself(self):
        """
            Удаляет пулю
        """
    def check_hit(self):
        """
            Проверяет поподание в мишень
        """
    
    
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
