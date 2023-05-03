import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk
import clip
import gpt2

root = tk.Tk()

root.title("Caption Generator")

root.geometry("1000x500")

def gen_cap(path,x):
    cations=[]
    if x==1:
        clip.c(cations,path)
        pass
    elif x>=1:
        # return 0
        clip.c(cations,path)
        y=x-1
        d=0
        p=1
        topp=1
        topk=50
        temp=1
        for i in range(y):
            gpt2.predict_step(cations,path,d,p,temp,topp,topk)
            d+=0.25
            p-=0.2
            temp-=0.2
            topp+=0.5
            topk+=20
    return cations



def upload_image():
    global path
    global x
    path = filedialog.askopenfilename()
    fp.insert(tk.END,path)

def captions():
    x=t.get("1.0","end-1c")
    path=fp.get("1.0","end-1c")
    x=int(x)
    cations=gen_cap(path,x)
    for i in cations:
        hi.insert(tk.END,i)

def display():
    path=fp.get("1.0","end-1c")
    im = Image.open(path) 
    im.show() 
    


def delet():
    fp.delete("1.0","end")
    hi.delete("1.0","end")
    t.delete("1.0","end")



    
    

welcome= tk.Label(root, text="Welcome.\n\nImage Caption Generator.",font=('Helevetica',24))
welcome.pack()

browse_button = tk.Button(root, text="Browse For Image", command=upload_image,fg="white",bg="black",activebackground="white",activeforeground="black")
browse_button.pack()

fp=tk.Text(root,height=1,width=10)
fp.pack()

n= tk.Label(root, text="Enter number of captions to be generated.",font=('Helevetica',24))
n.pack()

t=tk.Text(root,height=1,width=10)
t.pack()

button = tk.Button(root, text="Display Image", command=display,fg="white",bg="black",activebackground="white",activeforeground="black")
button.pack()

cap_button = tk.Button(root, text="Captions", command=captions,fg="white",bg="black",activebackground="white",activeforeground="black")
cap_button.pack()


del_button = tk.Button(root, text="Clear", command=delet,fg="white",bg="black",activebackground="white",activeforeground="black")
del_button.pack()

hi=tk.Text(root,height=10,width=80)
hi.pack()



root.mainloop()
