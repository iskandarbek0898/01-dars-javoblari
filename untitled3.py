# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 13:10:51 2022

@author: User2
"""

son =int(input("istalgan butun son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo\'linadi")