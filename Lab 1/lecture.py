#ipynp -> extension 1 (works fine)
#.py -> extension 2 (runs top to bottom)

print('Python Program')
print('hell o fast')
x=5
a =5.5
b='ali'
print(f'type of x ={type(x)}')

list1 = [12, 5, 6, 2, 'b', 'AI']
print(type(list1))
print(list1[:]) #print all list
print(list1[2:5]) #print some elements from start to end
print(list1[::2]) #skips 1 element
#python supports -ve index
print(list1[::-1]) #reverse the list
# [start:end:order/step]

list1[2]='BSCS'
del list1[3]

for i in list1:
    print(i)

str1='data science'
print(len(str1))
print(range(len(str1)))

#output:
Python Program
hell o fast
type of x =<class 'int'>
<class 'list'>
[12, 5, 6, 2, 'b', 'AI']
[6, 2, 'b']
[12, 6, 'b']
['AI', 'b', 2, 6, 5, 12]
12
5
6
2
b
AI
12
range(0, 12)

#after deletion:
12
5
BSCS
b
AI
_________________________________________________________________
for i in list1:
    if i=='BSCS':
        continue
    print(i)

#IF_ELSE
batch=2024
if batch ==2024:
    print("AI Assigned")
elif batch == 2025:
    print("in next year")
else:
    print("NA")

x=0
while x<5:
    print(x)
    x+=1
#NO DO-WHILE IN PYTHON

#for loop
str2="AI"
for i in range(len(str2)):
    print(str2[i], end=' ') #now new line now

tuple1 = (1,2, 4)
print(tuple1[2]) #we can't reassign a tuple

set1 = {1, 3, 5, 7}
set2 ={3, 5}
print(set1 - set2)
print(set1 | set2)
print(set1 & set2)



ouput:
12
5
b
AI
AI Assigned
0
1
2
3
4
A I 
4
{1, 7}
{1, 3, 5, 7}
{3, 5}
______________________________________________________
dict1 ={
    "id" : "25k-0810",
    "name" : 'Dua',
    "batch" : 2025 #id, name, batch are KEYS
}

print(dict1)
print(dict1['id'])
print(dict1.values())
dict1["uni"]="FAST"
print(dict1)
del dict1["name"]
------
def display(*a):
    return a

print(display(4,5,6))

def counter(a):
    return a+5

print(counter(5))
output:
{'id': '25k-0810', 'name': 'Dua', 'batch': 2025}
25k-0810
dict_values(['25k-0810', 'Dua', 2025])
{'id': '25k-0810', 'name': 'Dua', 'batch': 2025, 'uni': 'FAST'}
(4, 5, 6)
10
