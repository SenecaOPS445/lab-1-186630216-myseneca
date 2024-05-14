#!/usr/bin/env python3
#Author: Eliza May Silvestre
#File name: lab1d.py
#Date Created: May 14, 2024

x = 10
y = 2
z = 5

total = (x + y * z)       #multiplication happens before addition

print(f"{x} + {y} * {z} = {total}")


#print((x + 5) * 2)         #parentheses happen before multiplication
#print(x + 5 * 2 - 10 ** 2) #first exponents, then multiplication, then addition and subtraction from left-to-right
#print(15 / 3 * 4)       #division and multiplication happen from left-to-right
#print(100 / ((5 + 5) * 2))  #the inner most parentheses are first performing addition, then parentheses again with multiplication, finally the division