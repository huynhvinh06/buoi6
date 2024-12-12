def chuoi_toi_uu(s):
#    Ham strip xoa khoang trang o dau va cuoi chuoi
#    s= s.strip()

#    while "  " in s:
#       s= s.replace("  "," ")
#    Ham nay giup xoa khoang trang dau va cuoi chuoi va xoa khoang trang du thua
    s = ' '.join(s.split())
#    Ham title viet hoa chu cai dau
    s= s.title()
    return s

chuoi= input("Nhap vao chuoi: ")
print("Chuoi vua nhap la: ",chuoi)
chuoi_moi= chuoi_toi_uu(chuoi)
print("Chuoi sau khi toi uu: ",chuoi_moi)