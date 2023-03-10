# -*- coding: utf-8 -*-
"""ASSIGN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FCu7vLxDVUP7trT25c4AoQ7cGC_18-sG
"""

#Assignment-1
#create one example of list,touple,set and dictionary, for different types of datatyes use in the python
#1]LIST-
#List is mutable implies the elements of the list can be modified after creating the list.list is iterabel, 
#A list is data structure which contains comma separated heterogeneous elements enclosed within a pair of square brackets[].
#list maintain insertion order and list is ordered.
list1=[10,20,30,"python","c",3]
print(list1)
list1[2]="java"
print(list1)
for i in list1:
  print(i)
list1.insert(4,22)
print(list1)  
list1.append("teju")
print("The values after appending are",list1)



#2]Touple-
#Touple is data structure which contains comma separated heterogeneous elements enclosed within a pair of parentheses().
#Touple is immutable that the elements of a tuple cannot be modifies once the touples is created.
#Touple is iterable and ordered ,two tuples are considered to be equal if and only if they contain same elements also in the same order.
t=(1,2,3,4,5)
print(t)
t=t+(6,"teju")
print(t)
for ele in t:
  print(ele)
print(len(t))

#3]Set-
#Set elements are not indexed,Set is immutable implies that the elements of 
#a set cannot be modified once the set is created.set itself is mutable.set is iterable.
set1={2,11,5,43,6,4}
print(set1)
for ele in set1:
   print(ele)
print("Sorted set:",sorted(set1))
print(type(sorted(set1)))
set1.add("false")
print(set1)

#4]Dictionary-
#Dictionaries are enclosed by curly braces{} and values can be assigned and accessed using square braces[].
#Dictionary is mutable.
dict={}
dict["Course"]="M.sc"
dict[2]="Two"
print(dict)
print(dict["Course"])
print(dict[2])
print(dict.keys())
print(dict.values())
del dict["Course"]
print(dict)

#ASSIGNMENT-2
#What is r+,,w+,a+ modes in python with an example.
#1]r+
#Opens a file for both reading and writing.The file pointer placed at the beginning of the file.
#if we write the file directly,it will overwrite the beginning content.
with open('file2.txt','r+') as f:
  f.read()
  f.write("new line \n")

#2]w+
#Opens a file for both writing and reading.Overwrites the existing file if the file exits.
#if the file does not exist, creates a new file for reading and writing.
with open('file2.txt','w+')as f:
  f.write("test 1\n")
  f.write("test 2\n")
  f.write("test 3\n")
  f.seek(0)
  lines=f.read()
  print(lines)



#3]a+
#Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists
# The file opens in the append mode if the file does not exits it creates a new file for reading and writing.
with open("file2.txt",'a+') as f:
  f.seek(0)
  lines=f.readlines()
  f.write("\n" + str(len(lines)))

