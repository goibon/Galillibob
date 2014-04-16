import random
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
beginnings = []
middles = []
endings = []

file = open('names.txt', 'r')
names = file.readlines()

for name in names:
   name = name.lower()
   name = name.strip()
   for vowel in vowels:
       name = name.replace(vowel, "|" + vowel)
   firstVocal = name.find("|")
   name = name[0:firstVocal] + name[firstVocal+1:]
   arrName = name.split("|")

   if not arrName[0] in beginnings:
      beginnings.append(arrName[0])
   if len(arrName) > 1:
      if not arrName[len(arrName) -1] in endings:
         endings.append(arrName[len(arrName) - 1])

   if len(arrName) > 2:
      for i in range(1, len(arrName) - 1):
         if not arrName[i] in middles:
            middles.append(arrName[i])

fileBeg = open('beginnings.txt', 'w')
fileMid = open('middles.txt', 'w')
fileEnd = open('endings.txt', 'w')

for beg in beginnings:
   fileBeg.write(beg + "\n")
for mid in middles:
   fileMid.write(mid + "\n")
for end in endings:
   fileEnd.write(end + "\n")

#Print to a common.py file
random.shuffle(beginnings)
random.shuffle(middles)
random.shuffle(endings)
fileCom = open('common.py', 'w')
fileCom.write('#!/usr/bin/python\n')
fileCom.write('# -*- coding: utf-8 -*-\n')
fileCom.write('beginnings = ' + str(beginnings[:64]) + '\n')
fileCom.write('middles = ' + str(middles[:64]) + '\n')
fileCom.write('endings = ' + str(endings[:64]) + '\n')
