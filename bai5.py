import re
chuoi= input("Nhap vao mot chuoi: ")

def NegativeNumberInString(str):
    so_nguyen_am= 0
    s= re.findall(r"-?\d+", str)
    for i in s:
        if int(i) < 0:
            so_nguyen_am+=1
    return so_nguyen_am

print("So nguyen am trong chuoi la: ",NegativeNumberInString(chuoi))