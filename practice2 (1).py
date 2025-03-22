'''mylist=["apple","banana"]
mylist.insert(1,[1,2,3])
print(mylist[1][1])'''
'''def sum_elements(lst):
    return sum(lst)

inputlist = [30,40,50]

print(sum_elements(inputlist))'''
'''n = int(input("no of elements in list: "))
lst = []
for i in range(n):
    lst.append(int(input()))

even_numbers = list(filter(lambda x: x % 2 == 0, lst))
for i in even_numbers:
    print(i, end=" ")'''
'''n = int(input("total no of elements: "))
lst = []
for i in range(n):
    lst.append(int(input()))

for i in lst:
    if i < 0:
        lst.remove(i)

print(lst)'''
'''n = int(input("enter length of list: "))
lstitem = 1
i = 1
lst = []

while i <= n:
    lstitem = int(input())
    if lstitem > 0:
        lst.append(lstitem)
    i+=1

print(lst)'''
'''def prime_number(n):
    for x in range(2,n):
        if(n%x!=0):
            return print("Prime number")
        else:
            return print("Not Prime number")

n=int(input("Enter any number: "))
prime_number(n)'''
'''list=[6,15,6]
list.reverse()
print("reverse list :",list)'''
lst=[70,60,50,80]
lst.sort(reverse = True)
print(lst)