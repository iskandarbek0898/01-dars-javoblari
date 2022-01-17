# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 10:11:13 2022

@author: User2
"""

yosh =int(input("Yoshingiz nechida?"))
if yosh<=4 or yosh<=60:
     narh = 0
elif yosh < 18:
     narh = 10000
else:
   narh = 20000
print(f'Chipta {narh} so\'m')
