#!/usr/bin/env python
# coding: utf-8

#  Paint room

# In[8]:


L = eval(input("What is the length of the room in ft?"))
H = eval(input("What is the height of the room in ft?"))
W = eval(input("What is the width of the room in ft?"))
D = eval(input("How many doors?"))
wi = eval(input("How many windows?"))
a = 2*(L * W + L * H + H * W)
A = a - D * 20 - wi * 15
G = A / 350
C = "You will need to cover {} square feet."
c = "You will need {} gallons of paint to paint this room."
print(C.format(T))
print(c.format(G))


#  
