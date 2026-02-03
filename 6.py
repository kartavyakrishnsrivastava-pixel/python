a = int(input("Enter a marks in subject 1: "))
b = int(input("Enter a marks in subject 2: "))
c = int(input("Enter a marks in subject 3: "))
z = ((a+b+c)*100)/300
print(f"Your percentage is {z}%")
if z>=90:
    print("Your grade is A.")
elif z>=80:
    print("Your grade is B.")
elif z>=70:
    print("Your grade is C.")
elif z>=60:
    print("Your grade is D.")
elif z>=40:
    print("Your grade is E.")
else:
    print("Your grade is F. AND YOU FUCKING IDIOT.")