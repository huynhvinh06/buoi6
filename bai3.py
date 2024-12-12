#Chuoi "5;7;8;-2;8;11;13;9;10"
#Xuat cac so trong chuoi tren cac dong rieng biet
def chuoi(s):
    s = s.split(";")
    print("Cac so trong chuoi la:")
    for i in s:
        print(i)
#So chan
def so_chan(s):
    chan= 0
    s= s.split(";")
    for i in s:
        if int(i)%2==0:
            chan+=1
    return chan
#So am
def so_am(s):
    am= 0
    s= s.split(";")
    for i in s:
        if int(i)<0:
            am+=1
    return am
#So nguyen to
def so_nguyen_to(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
   
def xuat_so_nguyen_to(s):
    so_nt= 0
    s= s.split(";")
    for i in s:
        if so_nguyen_to(int(i)):
            so_nt+=1
    return so_nt
#Trung binh
def trung_binh(s):
    s= s.split(";")
    s= [int(i) for i in s]
    return sum(s)/len(s)



chuoi_s=("5;7;8;-2;8;11;13;9;10")
chuoi(chuoi_s)
print("So chan trong chuoi la:",so_chan(chuoi_s))
print("So am trong chuoi la:",so_am(chuoi_s))
print("So nguyen to trong chuoi la:",xuat_so_nguyen_to(chuoi_s))
print("Trung binh cong cac so trong chuoi la:",trung_binh(chuoi_s))