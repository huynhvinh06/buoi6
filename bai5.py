import re

chuoi= input("Nhap vao 1 chuoi: ")

def NegativeNumberInStrings(str):
    so_nguyen_am= re.findall(r"\b-[0-9]+", str)
    return so_nguyen_am

danh_sach= NegativeNumberInStrings(chuoi)

print("Cac so nguyen am la: ")

for i in danh_sach:
    print(i, end="\t")
