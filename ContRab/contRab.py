from random import randrange as rnd, choice
import tkinter as tk
import math
import time 


def main():
    """
    главня функция
    
    """
    pass



class Target:
    """
        Класс мишени
    
    """
    def __init__(self):
        pass
    def new_target(self):
        """
            Создаёт новую мишень
        """
    def move(self):
        """
            Двигает мишень
        """
        pass
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
