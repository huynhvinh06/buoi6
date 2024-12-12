def chuoi_dx(s):
    if s == s[: : -1] :
        return True
    else:
        return False

while True:
    chuoi= input("Nhap vao mot chuoi: ")
    if chuoi_dx(chuoi):
        print(chuoi,"la chuoi doi xung")
    else:
        print(chuoi,"khong la chuoi doi xung")

    tt= input("Tiep tuc? y/n")
    if tt == 'n':
        break
print("Ket thuc! Xin cam on ")
