s= input("Nhap vao chuoi: ")
#In hoa
def in_hoa(s):
    so_ky_tu= 0
    for i in s:
        if i.isupper():
            so_ky_tu+=1
    return so_ky_tu
#In thuong
def in_thuong(s):
    so_ky_tu= 0
    for i in s:
        if i.islower():
            so_ky_tu+=1
    return so_ky_tu
#Chu so
def chu_so(s):
    so_ky_tu= 0
    for i in s:
        if i.isdigit():
            so_ky_tu+=1
    return so_ky_tu
#Ky tu dac biet
def ky_tu_dac_biet(s):
    so_ky_tu= 0
    for i in s:
        if not i.isalnum() and not i.isspace():
            so_ky_tu+=1
    return so_ky_tu
#Khoang trang
def khoang_trang(s):
    so_ky_tu= 0
    for i in s:
        if i.isspace():
            so_ky_tu+=1
    return so_ky_tu
#Nguyen am
def nguyen_am(s):
    so_ky_tu= 0
    for i in s:
        if i in "aeiouAEIOU":
            so_ky_tu+=1
    return so_ky_tu
#Phu am
def phu_am(s):
    so_ky_tu= 0
    for i in s:
        if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            so_ky_tu+=1
    return so_ky_tu
print("So ky tu in hoa trong chuoi la: ",in_hoa(s))
print("So ky tu in thuong trong chuoi la: ",in_thuong(s))
print("So ky tu chu so trong chuoi la: ",chu_so(s))
print("So ky tu dac biet trong chuoi la: ",ky_tu_dac_biet(s))
print("So ky tu khoang trang trong chuoi la: ",khoang_trang(s))
print("So ky tu nguyen am trong chuoi la: ",nguyen_am(s))
print("So ky tu phu am trong chuoi la: ",phu_am(s))