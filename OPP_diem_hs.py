def nhap():
    for i in range(n):
        a[i]=hocsinh(0,0,0,0)
        print('nhap hoc sinh thu', i+1)
        a[i].ten=input('Nhap ten:')
        a[i].lop=input('Nhap lop:')
        a[i].diem=float(input('Nhap diem:'))
        a[i].truong=input('Nhap truong:')

def xuat():
    for i in range(n):
        a[i].show()

def diemmax():
    dmax=a[0].diem
    imax=0
    for i in range(n):
        if a[i].diem>dmax:
            dmax=a[i].diem
            imax=i
    a[imax].show()

def sxtang():
    for i in range(n):
        for j in range(i):
            if a[i].diem<a[j].diem:
                a[i].diem,a[j].diem=a[j].diem,a[i].diem
                a[i].ten,a[j].ten=a[j].ten,a[i].ten
                a[i].lop,a[j].lop=a[j].lop,a[i].lop
                a[i].truong,a[j].truong=a[j].truong,a[i].truong

    xuat()

def sxgiam():
    for i in range(n):
        for j in range(i):
            if a[i].diem>a[j].diem:
                a[i].diem,a[j].diem=a[j].diem,a[i].diem
                a[i].ten,a[j].ten=a[j].ten,a[i].ten
                a[i].lop,a[j].lop=a[j].lop,a[i].lop
                a[i].truong,a[j].truong=a[j].truong,a[i].truong

    xuat()

def diem9():
    for i in range(n):
        if a[i].diem>=9:
            a[i].show()

class hocsinh: 

    def __init__(self,ten,lop,diem,truong):
        self.ten=ten
        self.lop=lop
        self.diem=diem
        self.truong=truong

    def show(self):
        print("ten:",self.ten)
        print("lop:",self.lop)
        print("lop:",self.diem)
        print("lop:",self.truong)
        print("_ _ _ _ __  _")

while True:
    print('''***********************************
1. Nhap danh sach hoc sinh 
2. In danh sach hoc sinh
3. tim hoc sinh co diem cao nhat 
4. sap xep hoc sinh tang dan theo diem 
5. sap xep hoc sinh giam dan theo diem 
6. Liet ke cac hoc sinh co diem tu 9 tro len 
0. Thoat
**************''')
    chon=int(input('moi ban cho chuc nang:'))
    if chon==1: 
        n=int(input('nhap so hoc sinh can quan ly '))
        a=[0]*n
        nhap()
    if chon==2: 
        xuat()
    if chon==3:
        diemmax()
    if chon==4:
        sxtang()
    if chon==5:
        sxgiam()
    if chon==6:
        diem9()
    if chon==0:
        break 




