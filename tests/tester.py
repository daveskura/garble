"""
  Dave Skura
"""
import os

from garble_package.garble import garble 

print (" Starting ") # 
char_string =  input('any string: ')

garbled_str = garble().garbleit(char_string)
print(garbled_str)

#print(garble().ungarbleit(garbled_str))