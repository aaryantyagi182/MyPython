# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:58:04 2020

@author: aaryan
"""

import random
li=["Stone","Paper","Scissor"]
a=input("Welcome to the game\nChoose Stone,Paper or Scissor\n")
b=random.choice(li)
print(b)
if((a=='Stone'and b=='Stone') or (a=='Paper'and b=='Paper') or (a=='Scissor'and b=='Scissor')):
    print('Game tied')
elif((a=='Stone'and b=='Paper') or (a=='Scissor'and b=="Stone") or (a=='Paper'and b=='Scissor')):
    print('You lose')
elif((a=='Scissor'and b=='Paper') or (a=='Paper'and b=="Stone") or (a=='Stone'and b=='Scissor')):
    print('You Win')