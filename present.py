from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter.ttk import Treeview
import mysql.connector as mysql



form=Tk()
form.title('combobox')
form.state('zoomed')
form.configure(bg='skyblue')
form.resizable(height=False,width=False)

headline_lbl=Label(form,text='PROJECT',font=('Arial',60,'underline','bold'),fg='white',bg='skyblue')
headline_lbl.pack()

roll_lbl=Label(form,text='ROLL NUMBER',font=('Arial',18,'bold'),bg='skyblue')
roll_lbl.place(x=150,y=140)
roll_ent=Entry(form,width=15,font=('Arial',14,''))
roll_ent.place(x=350,y=140)
roll_ent.focus()

name_lbl=Label(form,text='NAME',font=('Arial',18,'bold'),bg='skyblue')
name_lbl.place(x=150,y=230)
name_ent=Entry(form,width=15,font=('Arial',14,''))
name_ent.place(x=350,y=230)

address_lbl=Label(form,text='ADDRESS',font=('Arial',18,'bold'),bg='skyblue')
address_lbl.place(x=150,y=320)
address_ent=Entry(form,width=15,font=('Arial',15,''))
address_ent.place(x=350,y=320)

    
gen_lbl=Label(form,text='GENDER',font=('Arial',18,'bold'),bg='skyblue')
gen_lbl.place(x=150,y=390)
gen_ent=Combobox(form,width=20,font=('',10,'bold'),values=['MALE','FEMALE','OTHER'])
gen_ent.place(x=350,y=390)
gen_ent.set('Select Option') 
     
save_btn=Button(form,command=lambda:reg(),width=10,text='SAVE',font=('',22,'bold','underline'),bd=15,bg='skyblue')
save_btn.place(x=300,y=470)

frm=Frame(form,bg='Skyblue')
frm.place(relx=.40,rely=.15,width=800,height=500)
scroll_y=Scrollbar(frm,orient=VERTICAL)
regtable=Treeview(frm,columns=('Roll','Name','Address','Gender'),yscrollcommand=scroll_y.set)

scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=regtable.yview)
regtable.heading('Roll',text='Roll')
regtable.heading('Name',text='Name')
regtable.heading('Address',text='Address')
regtable.heading('Gender',text='Gender')
regtable['show']='headings'
regtable.pack(fill=BOTH,expand=1)

def reg():
    
    mycon=mysql.connect(host="localhost",user="root",password="amankumar",database="project")
    cur=mycon.cursor()
    roll=roll_ent.get()
    name=name_ent.get()
    address=address_ent.get()
    gen=gen_ent.get()
    try:
       query="insert into register values(%s,%s,%s,%s)"
       cur.execute(query,(roll,name,address,gen))
       mycon.commit()
       mycon.close()
       res=messagebox.askyesno("success","Add Information save.. and must to be clear the form")
       if res==True:
           roll_ent.delete(0,END)
           name_ent.delete(0,END)
           address_ent.delete(0,END)
           gen_ent.delete(0,END)
           roll_ent.focus()
           
    except:
          messagebox.showerror("error","Roll already exist")
         
   

          
def share():
          mycon=mysql.connect(host="localhost",user="root",password="amankumar",database="project")
          cur=mycon.cursor()
          strr='select * from register'
          cur.execute(strr)
          data=cur.fetchall()
          regtable.delete(*regtable.get_children())
          for i in data:
             vv=[i[0],i[1],i[2],i[3]]
             regtable.insert('',END,values=vv)
          
         
save_btn=Button(form,command=lambda:share(),width=10,text='ShowData',font=('',22,'bold','underline'),bd=15,bg='skyblue')
save_btn.place(x=840,y=620)


       
    

form.mainloop()    
    




