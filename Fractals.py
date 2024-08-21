# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:45:36 2024

@author: Fernando Xicot
"""

import turtle

s ='A'
r1 ='B-A-B'
r2 ='A+B+A'

for i in range (4):
    ss = ''
    for m in s:
        if m == 'A':
            ss = ss + r1
        elif m == 'B':
            ss = ss + r2
        else:
            ss = ss + m
    s=ss
print (ss)    
theta=60

for i in s:
    if i =='A':
        turtle.forward(10)
    elif i =='B':
        turtle.forward(10)
    elif i == '+':
        turtle.left(theta)
    else:
        turtle.right(theta)