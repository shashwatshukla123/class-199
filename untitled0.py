# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h5cSdGzeWxDT-gjfmbmTmKHkLRUPpNji
"""

#print the first 10 odd numbers using a while loop in Python.

#—————————————— create a function which takes a dictionary and prints 2 lists. First list would contain all the keys and the second would contain all the values.

count=0
number=0
while count<10:
  if number%2==1:
   print (number)
   count=count+1
  number+=1

def print_dict(dict):
  keys=[],
  values=[],
  for k,v in dict.items():
    keys.append(k)
    values.append(v)
  print(keys)
  print(values)

dict_1={
    "apple":1,
    "oranges":5,
    "pineapple":2,
    "watermelon":3,
}
print_dict(dict_1)
print(dict_1)