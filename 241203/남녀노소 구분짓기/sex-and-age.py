sex = int(input())
age = int(input())

if sex == 0:
    if age < 19:
        print("BOY")
    else:
        print("MAN")
        
if sex == 1:
    if age < 19:
        print("GIRL")
    else:
        print("WOMAN")