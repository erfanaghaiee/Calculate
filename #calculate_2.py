#calculate_2

from tkinter import *
machin=Tk()
machin.title('Calculate')
machin.config(border=10,background='#1c1c1c')
machin.resizable(False,False)
entry=Entry(machin,font=['Tahoma',24],justify='right',bd=0)
entry.config(border=15,background='#1c1c1c',fg='white',insertbackground='white')

entry.grid(row=0,column=0,columnspan=4,pady=20,padx=10)



def Add(value):
    entry.insert(END,value)

def delete():
    entry.delete(0,END)
    
def backspace():
    current = entry.get()
    entry.delete(len(current)-1, END) # حذف مستقیم کاراکتر آخر

def calculate():
        try:
            expression = entry.get().replace('%', '/100').replace('×', '*').replace('÷', '/')
            result=eval(expression)
            entry.delete(0,END)
            entry.insert(0,str(result))
        except:
            entry.delete(0,END)
            entry.insert(0,'error')
            
Buttons=[
    ('C',delete),('⌫',backspace),('%',lambda:Add('%')),('÷',lambda:Add('÷')),
    ('7',lambda:Add('7')),('8',lambda:Add('8')),('9',lambda:Add('9')),('×',lambda:Add('×')),
    ('4',lambda:Add('4')),('5',lambda:Add('5')),('6',lambda:Add('6')),('-',lambda:Add('-')),
    ('1',lambda:Add('1')),('2',lambda:Add('2')),('3',lambda:Add('3')),('+',lambda:Add('+')),
    ('0',lambda:Add('0')),('.',lambda:Add('.')), ('=',calculate) 
            ]

row=1
col=0

for button , cmd in Buttons:
    if button == 'C':
        bg_color = '#ff5555' # قرمز
    elif button == '=':
        bg_color = '#50fa7b' # سبز
    elif button in ['÷', '×', '-', '+', '%', '⌫']:
        bg_color = '#ffb86c' # نارنجی برای عملگرها
    else:
        bg_color = '#ffffff' # سفید شیری برای اعداد
    
    
    btn=Button(machin,text=button,width=5,height=2,border=8,font=('Tahoma',12),command=cmd,bg=bg_color,fg='black', relief='flat', activebackground='#6272a4')
    
    if button=='=':
        btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=4, pady=4)
        
    else:
        btn.grid(row=row , column=col , padx=4 ,pady=4)
    
    col+=1
    if col>3:
        col=0
        row+=1

    

machin.mainloop()