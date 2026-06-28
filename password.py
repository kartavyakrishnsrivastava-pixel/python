print("this is a password validator")
has_upper = False
has_lower = False
has_number = False
has_special = False

passkey = input("enter your password : ")
for ch in passkey:
    if ch.isdigit():
        has_number = True
    elif ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    else:
        has_special = True
z = ( has_lower and has_number) and (has_upper and has_special)

if len(passkey)>=8  and z :
    print("you have a strongpassword")
    
