a = input("enter your name:")
print("good afternoon",a,"!") # using normal print statement

print(f"good afternoon {a} !") # using f string print statement


# Task 2
letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''
name = input("enter your name:")
date = input("enter date:")
print(letter.replace("<|NAME|>",name).replace("<|DATE|>",date)) 
#print(letter.replace("<|NAME|>",kartavya.replace("<|DATE|>",27/06/2024))) this will also work

# Task 3
st = "This is a  string with double  spaces"
print(st.find("  "))  # to find double spaces