n = int(input("enter a three digit number:"))
sum = 0
temp = n
while temp>0:
    digit = temp%10
    #print(digit)
    sum += digit**3
    #print(sum)
    temp = temp//10
    #print(temp)

if sum == n:
    print("entered numbered is armstrong number:")

def hcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x

    for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            hcf = i
    print(i,"is the required hcf")

hcf(18,12)
hcf(12,18)
hcf(54,24)

#there is inbuilt finction for calender

import calendar

yy = int(input("Enter year number:"))
mm = int(input("Enter month:"))

print(calendar.month(yy,mm))

#fabonacci in recursion
def fab(n):
    if n<=1:
        return n
    else:
        return (fab(n-1) + fab(n-2))

nterms = 100

if nterms<=0:
    print("please enter a positive number")
else:
    print("fabonacci sequence")
    for i in range(nterms):
        print(fab(i))

#sum with recrusion
def sums(m):
    if m<=1:
        return m
    else:
        return m + sums(m-1)

n = int(input("enter number uppto which u want to sum:"))

if n<0:
    print("enter natural numbers")
else:
    print("sum is:")
    print(sums(n))

#addition of matrices
x = [[12,3,4],
     [14,2,4],
     [16,3,2]]

y = [[3,5,2],
     [3,5,6],
     [7,5,8]]

#list comphrehension also do that
#results = [[x[i][j] +y[i][j] for j in range(len(x))] for i in range(len(x))]

results = [[0,0,0],
           [0,0,0],
           [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        results[i][j] = x[i][j]+y[i][j]

for r in results:
    print(r)

#multiply matrices
x = [[12,3,4],
     [14,2,4],
     [16,3,2]]

y = [[3,5,2],
     [3,5,6],
     [7,5,8]]

results = [[0,0,0],
           [0,0,0],
           [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        for k in range(len(y)):
            results[i][j] += x[i][k]*y[k][j]

for r in results:
    print(r)

# python offer some data types called sets and whose element must be unique.
# it can be used to perform different sets operations like union,
# intersections, difference and symmetric difference and also called operations

e = {0,2,4,6,8}
f = {1,3,5,7,9}

print("Union of e and f is :",e|f)
print("intersection of e and f is:",e&f )
print("difference of e and f is:", e-f)
print("symmetric difference of e and f is:",e^f)

# finding vowels or count of each vowels
vowels = 'aeiou'
str = "hello, is ths is a way to write the code when i dont get te correct answer"
#casefold method returns a string where all char are in lowercase or remove the case of string
str = str.casefold()
#it is used to make a dict. with each vowel as a key and va;ue is 0
count = {}.fromkeys(vowels,0)
#print(count)

for char in str:
    if char in count:
        count[char] +=1
print(count)

#there can be another method for do this
#using list and dictonary comprehension
str = "hello, is ths is a way to write the code when i dont get te correct answer"
str = str.casefold()
count = {x: sum([1 for char in str if char == x]) for x in 'aeiou'}

print(count)


#to know which python version
import sys
print("python version")
print(sys.version)
print("version info")
print(sys.version_info)

#calculate the number of days b/w two dates
from datetime import date
date1 = date(2014,7,2)
date2 = date(2014,7,11)
date3 = date2-date1
print(date3.days)


# python methods of sets
# add()- add the elements to the sets
# clear() - removes all the elements
# copy() - return a copy of the sets
# difference() - Return a ser contaning the difference b/w two sets
# difference_update() - Remove the items in this set that are also included in another, specified test
# discard() - Remove the specified items
# intersection() - Return a set, that is the intersection of two other intersections
# intersection_update() - Removes the itens in this set that are not present in other, specified sets
# isdisjoint() - Return whether two sets have a intersection or not
# issubset() - Return wheather another set contains this set or not
# issuperset() - Returns wheather this set contains this set or not
# pop() - Removes the specified element
# symmetric_difference - Returns a set with the symmetric difference of two sets
# symmetric_difference_update() - Inserts the symmetric difference from this sets and another
# union() Return a set contaning the union function
# update() Update the set with the union of this set and others

#check if the file exist
import os.path
open('abc.txt','w')
print(os.path.isfile('abc.txt'))


# For 32 bit it will return 32 and for 64 bit it will return 64
# python shell is executing in 32 bit or 64bit mode on OS
import struct
print(struct.calcsize("P") * 8)


#python program to get OS name, platform and release information
import os
import platform
print(os.name)
print(platform.system())
print(platform.release())


# python program to locate python site-packages
import site
print(site.getsitepackages())


# python program to call an external command in python
from subprocess import call
call(["ls","-1"])


# python program to get the path and name of the file that is currently executing
import os
print("Current file name:",os.path.realpath(__file__))


#python program to find out the number of CPU using
import multiprocessing
print(multiprocessing.cpu_count())


#program to list all files in a directory in python
from os import listdir
from os.path import isfile, join
file_list = [f for f in listdir('home/students') if isfile(join('/home/students',f))]
print(file_list)


# python program to determine profiling of python programs
import cProfile
def sum():
    print(1+2)
cprofile.run('sum()')


# programme for access environmental variables
improt os

print("_______________________________")
print(os.environ)
print("_______________________________")
print(os.enivron['jmv'])
print("_______________________________")
print(os.environ["PATH"])


#program to get the curret=nt user name
import getpass
print(getpass.getuser())


#program to find local IP addresses using python's stdlib
import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


#program to get height and the width of console window
def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

print('Number of columns and Rows: ',terminal_size())

#57
#63
#64


# program to get the copyright information
import sys
print("\nPython copyright INformation")
print(sys.copyright)
print()


#program to hash a word
soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]

word=input("Input the word be hashed: ")

word=word.upper()

coded=word[0]

for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print()
print("The coded word is: "+coded)
print()


#progrm to get the details of math module
import math
math_ls = dir(math)
print(math_ls)


#program to sort files by date
import glob
import os

files = glob.glob("*.txt")
files.sort(key= os.path.getmtime)
print("/n".join(files))


#program to get a directory listing, sorted by creation table
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))


#program to find the host name in which the routine is running
import socket
host = socket.gethostname()
print("Host_Name:",host)

#program to clear the screen or terminal
import os
import time
#for windows
#os.system('cls')
os.system('ls')
time.sleep(2)
#Ubuntu
os.system('clear')

#program to get the system time
import time
print()
print(time.ctime())
print()

#program to product a list of integer without loop
from functools import reduce
nums = [10,20,30]
nums_product = reduce((lambda x,y: x*y),nums)
print(nums_product)

# program to get actucal module object for a given object
from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))

#program to add leading and trailing zeros to a string
str1 = '122.22'
str2 = '122.22'
print("the original strig is:",str1)
print("adding triling zeros")
str1 = str1.ljust(10,'0') #we can also add 1 to string change 0 to 1
print(str1)
print("adding the leading zeros:")
str2 = str2.rjust(10,'0')
print(str2)

# program  for change the decimal to binary digit
def dtb(num):
    if num>1:
        dtb(num//2)
    print(num%2,end="")

dtb(17)

# program to print the largest word in the string
str = input("enter a string:")
list = []
largest = -1
str = str.split()
for i in range(len(str)):
    x = len(str[i])
    list.append(x)
print(list)
for num in list:
    if num >largest:
        largest = num
print(largest)
for word in str:
    if len(word) == largest:
        print(word)
#same program but better perforamance
str = input("enter a string:")
str = str.split()
word_len = []
for n in str:
    word_len.append((len(n), n))
word_len.sort()
#print(word_len)
print(word_len[-1][1])


#for list of letter to find largest letter
largest = -1
mylist  = []
list = ["list","helloworld", "goodforoneispython"]
for words in list:
    x = len(words)
    mylist.append(x)
    for num in mylist:
        if num > largest:
            largest = num
for i in range(len(list)):
    if len(list[i]) == largest:
        print(list[i])
#smae as upper
str = ["list","wordsisbetter","jokerman"]
word_len = []
for n in str:
    print(n)
    word_len.append((len(n), n))
word_len.sort()
#print(word_len)
print(word_len[-1][1])

#TO remove the ident form the given string
import textwrap
sample = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
sample2 = textwrap.dedent(sample)
print(sample2)

#display formatted text (width = 50) as output
import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print(textwrap.fill(sample_text, width = 50))

# program to add a prefix text to all the lines in string
import textwrap
sample = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
sample2 = textwrap.dedent(sample)
wrapped = textwrap.fill(sample2, width = 50)
final = textwrap.indent(wrapped,'>')

# program to print the interger with zeros on the left of specified width
x = 3
print("{:0>4d}".format(x))
