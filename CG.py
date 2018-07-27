from tkinter import *
from math import pi
from random import randint
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
def calc(x,y):
 c=pow((x-600)*400,2)+pow((y-350)*200,2)-pow(200*400,2)
 return c
def rot(earth,x,y):
 C.move(earth,x,y)
 root.after(20)
 C.update()
def slope(x,y):
 m=(200/400)
 sl=-1*(pow(m,2)*(x/y))
 return sl

def drawell2(earth,x,y,z):
 a.append(x)
 b.append(z)
 if z==350:
  for i in range(len(a),1,-1):
   ma=a[i-2]-a[i-1]
   mb=b[i-2]-b[i-1]
   C.move(earth,ma,mb)
   root.after(20)
   C.update()
 
def drawell3(earth,x,y,z):
 c.append(x)
 d.append(y)
 if z==350:
  for i in range(len(c)):
   if i!=len(c)-1:
    ma=c[i+1]-c[i]
    mb=d[i+1]-d[i]
    C.move(earth,ma,mb)
    root.after(20)
    C.update()
   
def drawell4(earth,x,y,z):
 e.append(x)
 f.append(y)
 if z==350:
  for i in range(len(e),1,-1):
    ma=e[i-2]-e[i-1]
    mb=f[i-2]-f[i-1]
    C.move(earth,ma,mb)
    root.after(20)
    C.update()

def drawell1(earth,x,y):
 sl=slope(x,y)
 
 while sl<=-1: 
  x=x+1
  xx=x
  val=calc(x,y+0.5)
  if val>0:
     y=y+1
     rot(earth,1,1)
     sl=slope(x,y)
     z=350+(350-y)
     xp=600-(x-600)
     yp=550-(y-150)
     ypp=150+(y-150)
     drawell2(earth,xx,y,z)
     drawell3(earth,xp,yp,z)
     drawell4(earth,xp,ypp,z)
  elif val<0:
     y=y
     rot(earth,1,0)
     sl=slope(x,y)
     z=350+(350-y)
     xp=600-(x-600)
     yp=550-(y-150)
     ypp=150+(y-150)
     drawell2(earth,xx,y,z)
     drawell3(earth,xp,yp,z)
     drawell4(earth,xp,ypp,z)
 while y!=350:
  y=y+1
  valu=calc(x+0.5,y)
  if valu<0:
     x=x
     xx=x
     y=y
     rot(earth,0,1)
     sl=slope(x,y)
     z=350+(350-y)
     xp=600-(x-600)
     yp=550-(y-150)
     ypp=150+(y-150)
     drawell2(earth,xx,y,z)
     drawell3(earth,xp,yp,z)
     drawell4(earth,xp,ypp,z)
  elif valu>0:
     x=x+1
     xx=x
     y=y
     rot(earth,1,1)
     sl=slope(x,y)
     z=350+(350-y)
     xp=600-(x-600)
     yp=550-(y-150)
     ypp=150+(y-150)
     drawell2(earth,xx,y,z)
     drawell3(earth,xp,yp,z)
     drawell4(earth,xp,ypp,z)
root=Tk()
root.title("Earth's Rotation")
root.minsize(300,300)
root.geometry("1200x700")
x=int(1200/2)
y=int(700/2)
C = Canvas(root, bg="black", height=120, width=120)
C.pack(expand=YES, fill=BOTH)
C.create_oval((x-60), (y-60), (x+60), (y+60),fill="yellow")
C.pack(expand=YES, fill=BOTH)
earth=C.create_oval((x-40), (y-240), (x+40), (y-160),fill="green")
drawell1(earth,x,y-200)
mainloop()
