#task1
# Write a Python program to store seven fruit names in a list entered by the user and print them in the following format: 
a =input("enter fruit 1:")
b=input("enter fruit 2:")
c=input("enter fruit 3:")
d=input("enter fruit 4:")
e=input("enter fruit 5:")
f=input("enter fruit 6:")
g=input("enter fruit 7:")
z = [a,b,c,d,e,f,g]
print(f'The fruit names are:\n1.{a}\n2.{b}\n3.{c}\n4.{d}\n5.{e}\n6.{f}\n7.{g}')
print(z)

#task2
student1 = int(input("enter the marks of student 1:"))
student2 = int(input("enter the marks of student 2:"))
student3 = int(input("enter the marks of student 3:"))
student4 = int(input("enter the marks of student 4:"))
student5 = int(input("enter the marks of student 5:"))
marks = [student1, student2, student3, student4, student5]
marks.sort()
print("The sorted marks are:",marks)
#task3
a =(7,0,8,0,0,9)
print(a.count(0))
print(a.index(9))
#task4
a = [1,2,3,4,5]
print(sum(a))

fruits = []

for i in range(1, 8):
    fruit = input(f"Enter fruit {i}: ")
    fruits.append(fruit)

print("The fruit names are:")
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}.{fruit}")

print(fruits)
