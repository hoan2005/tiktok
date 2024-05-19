from tkinter import*
from PIL import ImageTk,Image
from time import*
try:
    #tạo của sổ
    a=Tk()
    a.title("máy tính casio phiên bản đang tập code")
    a.geometry("600x600")
    a.attributes('-topmost',True)
    # tạo nền trắng khi máy tính chưa được bật
    #tạo ô to nền máy tính
    b=Label(a,text='',font=('Times New Roman',20),width=30,height=20,fg='black',bg='grey')
    b.place(x=550,y=70)
    # chèn ảnh lấy bản quyền trên máy  tính
    img=Image.open(r'C:\Users\LENOVO\Downloads\f22460d81381bddfe490 (1).jpg')
    img1=img.resize((50,50),Image.BILINEAR)
    img2=ImageTk.PhotoImage(img1)
    x=Label(a,text=' ',image=img2)
    x.place(x=950,y=70)
    #tạo tên bản quyền trên khung máy tính
    truong=Label(a,text='NGUYỄN VĂN HOÀN',font=('Times New Roman',25),fg='black',bg='grey')
    truong.place(x=550,y=70)
    class so():
        def tao(self):
            #hàm tạo màn hình máy tính
            self.lis=[]
            self.e=Entry(a,font=('Times New Roman',38),width=17,borderwidth=8)
            self.e.place(x=550,y=170)
            self.e.focus()
        def so0(self):
            self.e.insert(END,0)
            self.lis.append(0) 
        def so1(self):
            self.e.insert(END,1)
            self.lis.append(1)
        def so2(self):
            self.e.insert(END,2)
            self.lis.append(2)
        def so3(self):
            self.e.insert(END,3)
            self.lis.append(3)          
        def so4(self):
            self.e.insert(END,4)
            self.lis.append(4)
        def so5(self):
            self.e.insert(END,5)
            self.lis.append(5)
        def so6(self):
            self.e.insert(END,6)
            self.lis.append(6)
        def so7(self):
            self.e.insert(END,7)
            self.lis.append(7)
        def so8(self):
            self.e.insert(END,8)
            self.lis.append(8)
        def so9(self):
            self.e.insert(END,9)
            self.lis.append(9)
        def cong(self):
            self.e.insert(END,'+')
            self.lis.append('+')
            #xử lý hai dấu cộng và dấu cộng với dấu trừ
            if self.lis[0]!='+' or len(self.lis)!=1:
                if self.lis[len(self.lis)-2]=='+':
                    self.lis[len(self.lis)-2:]='+'
                elif self.lis[len(self.lis)-2]=='-':
                    self.lis[len(self.lis)-2:]='-'
        def tru(self):
            self.e.insert(END,'-')
            self.lis.append('-')
            #xử lí 2 dấu trừ và dấu cộng và dấu trừ
            if self.lis[0]!='-' or len(self.lis)!=1:
                if self.lis[len(self.lis)-2]=='+':
                    self.lis[len(self.lis)-2:]='-'
                elif self.lis[len(self.lis)-2]=='-':
                    self.lis[len(self.lis)-2:]='+'
        def dau3(self):
            self.e.insert(END,'*')
            self.lis.append('*')
        def dau4(self):
            self.e.insert(END,'/')
            self.lis.append('/')
        def cham(self):
            self.e.insert(END,'.')
            self.lis.append('.')
        def bang(self):
            try:
                # các câu lệnh trong hàm bằng này luôn xủa lí
                # theo thứ tự trên về đã đặt sẵn đó
                if (self.lis[0]=='-' or self.lis[0]=='+'):
                    self.lis[0:2]=[int(str(self.lis[0])+str(self.lis[1]))]
                elif(self.lis[0]=='/' or self.lis[0]=='*' or self.lis[0]=='.'):
                    self.lis=[]
                lis4=len(self.lis)
                d3=0
                while(d3<lis4-1):
                    o=self.lis[d3]
                    o1=self.lis[d3+1]
                    # hàm xử lí nếu thấy 2 số hay nhiều số gần nhau thì gộp lại thành 1
                    if((o!='*' and o!= '/' and o != '+' and  o!= '-' and o != '.') and (o1!='*' and  o1!= '/' and o1 != '+' and o1 != '-' and o1 != '.')):
                        n=str(self.lis[d3])+str(self.lis[d3+1])
                        self.lis[(d3):(d3+2)]=[int(n)]
                        lis4=len(self.lis)
                    else:
                        d3+=1
                lis1=len(self.lis)
                d=0
                while(d<lis1):
                    # xử lí nếu là dấu chấm thì gộp lại thành số thập phân
                    if(self.lis[d]=='.'):
                        n=float(str(self.lis[d-1])+self.lis[d]+str(self.lis[d+1]))
                        self.lis[(d-1):(d+2)]=[n]
                        lis1=len(self.lis)
                    else:
                        d+=1   
                lis2=len(self.lis)
                d1=0
                while(d1<lis2):
                    # nếu là dấu nhân chia thì dùng nhân chia trước
                    if(self.lis[d1]=='*'):
                        # hàm dùng để biét nêu  cộng hoặc trừ đi với nhân(đi sau) thì báo lỗi
                        # hàm dùng để biết nếu nhân(trước) đi với cộng trừ nhân chia thì bao lỗi
                        if (self.lis[d1+1]=='+' or self.lis[d1+1]=='-'  ):
                            self.lis[(d1+1):(d1+3)]=[int(str(self.lis[d1+1])+str(self.lis[d1+2]))]
                        elif(self.lis[d1+1]=='/' or self.lis[d1+1]=='*' or self.lis[d1-1]=='+' or self.lis[d1-1]=='-'):
                            self.lis=[]
                            break
                        n=self.lis[d1-1]*self.lis[d1+1]
                        self.lis[(d1-1):(d1+2)]=[n]
                        lis2=len(self.lis)

                    elif(self.lis[d1]=='/'):
                            m=self.lis[d1-1]/self.lis[d1+1]
                            self.lis[(d1-1):(d1+2)]=[m]
                            lis2=len(self.lis)   
                    else:
                        d1+=1
                        continue
                lis3=len(self.lis)
                d2=0
                # đên đây hàm chỉ còn cộng và trừ
                # nhiệm cụ xử lí cộng với trừ là xoong
                while(d2<lis3):
                    if(self.lis[d2]=='+'):
                        n=self.lis[d2-1]+self.lis[d2+1]
                        self.lis[(d2-1):(d2+2)]=[n]
                        lis3=len(self.lis)
                    elif(self.lis[d2]=='-'):
                        m=self.lis[d2-1]-self.lis[d2+1]
                        self.lis[(d2-1):(d2+2)]=[m]
                        lis3=len(self.lis)
                    else:
                        d2+=1
                # lis chỉ còn lại 1 giá trị
                if(self.lis[0]-int(self.lis[0])==0):
                    # kiểm tra xem để in ra dưới dạng thập phân hay dạng int
                    self.e.delete(0,END)
                    self.e.insert(END,int(self.lis[0]))
                else:
                    self.e.delete(0,END)
                    self.e.insert(END,self.lis[0])
            except Exception as error:
                        # nếu trong try có lỗi thì hiện lên màn hìn lỗi
                        self.e.delete(0,END)
                        self.e.insert(END,("LỖI CÚ PHÁP"))               
        def follow(self):
            self.e.delete(0,END)
            self.e.insert(END,"Follow mình nhé")
            a.update()
            sleep(3)
            s.xoa()
        def xoa(self):
            self.e.delete(0,END)
            self.lis=[]
        def xoa1(self):
            self.e.delete((len(self.lis)-1),END)
            self.lis.__delitem__(-1)
        def off(self):
            self.e.destroy()
    s=so()
    ok = Button(a, text='ON', padx=20, pady=20,command=s.tao,bg='black',fg='white',width=1,height=1,borderwidth=3)
    ok.place(x=950,y=380)
    # tạo nút lệnh chuyển đổi đến follow kênh
    i3=Image.open(r'C:\Users\LENOVO\Pictures\cach-chup-anh-tren-tiktok-didongviet-5.jpg')
    i4=i3.resize((200,200),Image.BILINEAR)
    i5=ImageTk.PhotoImage(i4)
    i6=Button(a,text=' ',image=i5,command=s.follow,activebackground='red')
    i6.place(x=0,y=590)
    banphim = [
        ('7', 380, 560,s.so7), ('8', 380, 630,s.so8), ('9', 380, 700,s.so9), ('/', 380, 770,s.dau4),
        ('4', 460, 560,s.so4),('5', 460, 630,s.so5), ('6', 460, 700,s.so6), ('*', 460, 770,s.dau3),
        ('1', 540, 560,s.so1), ('2', 540, 630,s.so2), ('3', 540, 700,s.so3), ('-', 540, 770,s.tru),
        ('0', 620, 560,s.so0), ('.', 620, 630,s.cham), ('=', 620, 700,s.bang), ('+', 620, 770,s.cong)
    ]
    for (ten,dong,cot,ham) in banphim:
        button = Button(a, text=ten, padx=20, pady=20,command=ham,fg='black',bg='white',font=("Times New Roman",15),width=1,height=1)
        button.place(x=cot, y=dong)
    ok = Button(a, text='AC', padx=20, pady=20,command=s.xoa,bg='black',fg='white',width=1,height=1,borderwidth=3)
    ok.place(x=950,y=460)
    ok = Button(a, text='DEL', padx=20, pady=20,command=s.xoa1,bg='black',fg='white',width=1,height=1,borderwidth=3)
    ok.place(x=890,y=460)
    ok = Button(a, text='OFF', padx=20, pady=20,command=s.off,bg='black',fg='white',width=1,height=1,borderwidth=3)
    ok.place(x=890,y=380)
    mainloop()
except Exception as error:
    print('lỗi ở đây :',error)