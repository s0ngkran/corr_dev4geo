from utm import to_latlon,from_latlon
from csv import writer
from tkinter import messagebox, END, Tk,LabelFrame,Label,W,StringVar,Scrollbar,VERTICAL,RIGHT,Y,BOTH,E,Text,LEFT,Button
from tkinter import filedialog as fdu
from time import sleep
def csva():
    disp.set('ตั้งค่าการบันทึก...')
    la2.configure(background='#f7ce93')
    try:
        dir_ = fd.asksaveasfilename(initialfile="พิกัด.csv",defaultextension=".csv",\
            title='บันทึกข้อมูล',filetypes=[("csv", ".csv")])
        datt_ = T2.get('1.0', END).split('\n')
        datt = []
        for i in datt_:
            datt.append([i])
        with open(dir_, 'w', newline='') as csvfile:
            spamwriter = writer(csvfile)
            spamwriter.writerows(datt)
        disp.set('บันทึกสำเร็จ กำลังออกจากโปรแกรม')
        la2.configure(background='#72f79b')
        la2.update()
        sleep(2)
        top.destroy()
    except :
        disp.set('บันทึกไม่สำเร็จ')
        la2.configure(background='#f78383')
            
def copy():
    datt = T2.get('1.0', END)
    top.clipboard_clear()
    top.clipboard_append(datt)
    disp.set('คัดลอกสำเร็จ')
    la2.configure(background='#78f799')

def ex1():
    T.delete('1.0',END)
    T2.delete('1.0',END)
    with open('ex1.txt','r') as f:
        ex1_ = f.read()
    T.insert(END, ex1_)
    disp.set('ลองคลิ๊กแปลงพิกัด')
    la2.configure(background='#fff3c2')

def ex2():
    T.delete('1.0',END)
    T2.delete('1.0',END)
    with open('ex2.txt','r') as f:
        ex2_ = f.read()
    T.insert(END, ex2_)
    disp.set('ลองคลิ๊กแปลงพิกัด')
    la2.configure(background='#fff3c2')
    
def convert():
    T2.delete('1.0',END)
    datt = (T.get('1.0', END)+str('\n')).split('\n')
    if len(datt[0].split()) >2:
        c = 1
        for dat_ in datt:
            a=dat_.split()
            an = len(a)
            if an > 0:
                try:
                    bn = len(a[1])
                    x = 0 if an<bn else 1
                    y = 1 if an<bn else 0
                    res=to_latlon(float(a[x]), float(a[y]), int(a[2][:-1]), str(a[2][-1:]))
                    T2.insert(END,str(res[0])+' '+str(res[1])+'\n')
                except :pass
    else :
        c = 2
        for dat_ in datt:
            a = dat_.split()
            an = len(a)
            if an > 0:      
                try:
                    res=from_latlon(float(a[0]), float(a[1]))
                    T2.insert(END,str(res[0])+' '+str(res[1])+' '+str(res[2])+str(res[3])+'\n')
                except :pass
        
        #print(a[0], a[1], a[2][:-1], a[2][-1:])
    check = len(datt) if c==2 else len(datt)-1
    if abs(check-len(T2.get('1.0', END).split('\n')))>=3:
        disp.set('บางข้อมูลผิดพลาด')
        la2.configure(background='#ef7676')
    elif len(T2.get('1.0', END).split('\n'))-2==0:
        disp.set('โปรดกรอกข้อมูล')
        la2.configure(background='#fff3c2')
    elif len(datt[0].split()) <=2:
        disp.set('แปลงจาก lat เป็น utm สำเร็จ '+str(len(T2.get('1.0', END).split('\n'))-2)+' รายการ')
        la2.configure(background='#78f799')
    else:
        disp.set('แปลงจาก utm เป็น lat สำเร็จ '+str(len(T2.get('1.0', END).split('\n'))-2)+' รายการ')
        la2.configure(background='#78f799')
def sup():
    messagebox.showinfo('ช่องทางสนับสนุน','ติดต่อผู้พัฒนา\nline ID: s0ngkr4n\njinnawat8@gmail.com')
def dell():
    T.delete('1.0',END)
    T2.delete('1.0',END)
    disp.set('กรอกข้อมูล')
    la2.configure(background='#fff3c2')
    T.focus()

 
top = Tk()

top.title('โปรแกรมแปลงพิกัด v0.1 from KKU')
top.wm_iconbitmap('icon.ico')
top.geometry("1000x350+200+100")

f0 = LabelFrame(top, width=200, height=50)
f02 = LabelFrame(top, width=200, height=50)
f1 = LabelFrame(top, width=450, height=200)
f12 = LabelFrame(top, width=450, height=200)
f2 = LabelFrame(top, width=50, height=50 ,borderwidth = 0)
f3 = LabelFrame(top, width=50, height=50 ,borderwidth = 0)

#head label
fontT=("Helvetica", "15","bold")
font2=("Helvetica", "15")
la1 = Label(f0, text="utm_x   utm_y   zone  (หรือ lat  lon)",font=fontT,bg='#efc9bb')
la1.grid(row=0, column=0, sticky=W)

disp = StringVar(top)
disp.set('กรอกข้อมูล')
la2 = Label(f02, textvariable=disp,font=fontT,bg='#fff3c2')
la2.grid(row=0, column=0, sticky=W)

#text box1
yScroll = Scrollbar(f1, orient = VERTICAL, width=20)
yScroll.pack(side=RIGHT, fill=Y)
T = Text(f1, height=10, width=40,font=font2,yscrollcommand=yScroll.set,bg='#efc9bb')
T.pack(side = LEFT, fill = BOTH)
yScroll["command"] = T.yview

#text box2
yScroll2 = Scrollbar(f12, orient = VERTICAL, width=20)
yScroll2.pack(side=RIGHT, fill=Y)
T2 = Text(f12, height=10, width=40,font=font2,yscrollcommand=yScroll2.set,bg='#fff3c2')
T2.pack( side = LEFT, fill = BOTH )
yScroll2["command"] = T2.yview

#button
b011 = Button(f2, text = 'ตัวอย่าง utm',bg='#efc9bb',\
                font=('Helvetica', '15'),  height = 1,\
                width = 10, command = ex1)
b011.grid(row=0,column=0)
b022 = Button(f2, text = 'ตัวอย่าง lat',bg='#efc9bb',\
                font=('Helvetica', '15'),  height = 1,\
                width = 10, command = ex2)
b022.grid(row=0,column=1)
b0 = Button(f2, text = 'สนับสนุน',bg='#efc9bb',\
                font=('Helvetica', '15'),  height = 1,\
                width = 8, command = sup)
b0.grid(row=0,column=2)
b1 = Button(f2, text = 'แปลงพิกัด',bg='#fff3c2',\
                font=('Helvetica', '15'),  height = 1,\
                width = 8, command = convert)
b1.grid(row=0,column=3)

b112 = Button(f3, text = 'บันทึกเป็น csv',bg='#fff3c2',\
                font=('Helvetica', '15'),  height = 1,\
                width = 12, command = csva)
b112.grid(row=0,column=0)
b11 = Button(f3, text = 'คัดลอก',bg='#fff3c2',\
                font=('Helvetica', '15'),  height = 1,\
                width = 8, command = copy)
b11.grid(row=0,column=1)
b0 = Button(f3, text = 'ล้างข้อมูล',bg='#fff3c2',\
                font=('Helvetica', '15'),  height = 1,\
                width = 8, command = dell)
b0.grid(row=0,column=2)

#pack
f0.grid(row = 0, column = 0, sticky=W )
f02.grid(row = 0, column = 1, sticky=E )
f1.grid(row = 1, column = 0)
f12.grid(row = 1, column = 1)
f2.grid(row = 2, column = 0, sticky=E)
f3.grid(row = 2, column = 1, sticky=E)
top.mainloop()


