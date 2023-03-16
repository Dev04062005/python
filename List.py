# User input in List:

l = []
num = int(input("enter list size : "))

for i in range(0,num):

    tem = int(input())
    l.append(tem)
print(l)

# List Operation :

li = [3,4,7,"g",5.12,[12,34]]

#Update elements in list : 

a=[1000]
li.append(3+4j)
print(li)
li.insert(3,"shyam")
print(li)
li.extend(a)
print(li)
li.pop()
print(li)
li.remove("g")
print(li)
li[0]="34"
print(li)

# List slicing
print(li[2:4])
print(li[ :2])
print(li[ 0: ])

#List op : 
List = [56,5,34,78,2,4,7,4]

print("Min and Max value in list : ")
print(min(List))
print(max(List))
print("Accending sort : ")
List.sort()
print(List)
print("Decending sort :")
List.sort(reverse=True)
print(List)
print("Count of 4 in List : ")
print(List.count(4))
print("Sum of List : ")
print(sum(List))
print("Clear Function on List : ")
print(List.clear())
del List

