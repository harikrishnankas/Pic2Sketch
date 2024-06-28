from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import cv2
import pickle

root = Tk()
root.minsize(700,700)
#root.geometry('500x500')
root.config(bg='orange')


#creating 2nd page

def sigmakey():
    root.bind('<Left>', lambda e : slider_1.set(slider_1.get()-10))
    root.bind('<Right>', lambda e : slider_1.set(slider_1.get()+10))

def sigma(a):
    global sketch
    scale_x_y = slider_1.get()
    details = slider_2.get()


    if scale_x_y % 2 ==0:
        scale_x_y +=1

    

    pic = cv2.imread(filename)
    grey_pic = cv2.cvtColor(pic , cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_pic)
    blur = cv2.GaussianBlur (invert, (scale_x_y,scale_x_y),2000)
    invt_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_pic, invt_blur , scale = details)

    cv2.imwrite('test123.png',sketch)


    #img_canva.destroy()
    img_canva = Canvas (frame )
    img_canva.place( relheight=0.5 , relwidth=0.8 , relx=0.1 , rely=0.1 )


    #determining canvas width
    #Definig function to determine canvas width
    def resizer(e):
        global canva_width,img1
        canva_width = e.height
        #resizing image
        basewidth = canva_width
        img = Image.open('test123.png')
        wpercent = (basewidth/float(img.size[1]))
        hsize = int((float(img.size[0])*float(wpercent)))
        img = img.resize((hsize,basewidth),Image.ANTIALIAS)
    
        img1 =ImageTk.PhotoImage (img)
        img_canva.create_image(250,160,image=img1)
    
    #using bind to find width
    img_canva.bind('<Configure>',resizer)


    sigmakey()


def detailskey():
    root.bind('<Left>', lambda e : slider_2.set(slider_2.get()-10))
    root.bind('<Right>', lambda e : slider_2.set(slider_2.get()+10))

def details_fun(a):
    global sketch
    scale_x_y = slider_1.get()
    details = slider_2.get()

    if scale_x_y % 2 ==0:
        scale_x_y +=1
    

    pic = cv2.imread(filename)
    grey_pic = cv2.cvtColor(pic , cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_pic)
    blur = cv2.GaussianBlur (invert, (scale_x_y,scale_x_y),2000)
    invt_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_pic, invt_blur , scale = details)

    cv2.imwrite('test123.png',sketch)


    #img_canva.destroy()
    img_canva = Canvas (frame )
    img_canva.place( relheight=0.5 , relwidth=0.8 , relx=0.1 , rely=0.1 )


    #determining canvas width
    #Definig function to determine canvas width
    def resizer(e):
        global canva_width,img1
        canva_width = e.height
        #resizing image
        basewidth = canva_width
        img = Image.open('test123.png')
        wpercent = (basewidth/float(img.size[1]))
        hsize = int((float(img.size[0])*float(wpercent)))
        img = img.resize((hsize,basewidth),Image.ANTIALIAS)
    
        img1 =ImageTk.PhotoImage (img)
        img_canva.create_image(250,160,image=img1)
    
    #using bind to find width
    img_canva.bind('<Configure>',resizer)

    detailskey()


def save_fun():
    f = filedialog.asksaveasfile(mode='w',initialfile = 'Untitled.png',defaultextension=".png",filetypes=[("PNG","*.png"),("All Files","*.*")])
    img_array = Image.fromarray(sketch)
    img_array.save(str(f.name))
    root.destroy()


def edit_fun():
    global frame,img1,slider_1,slider_2,img_canva,sketch
    frame.destroy()
    frame = Frame ( root, bg = "white" )
    frame.place( relheight=0.9 , relwidth=0.9 , relx=0.5 , rely=0.5,anchor=CENTER )
    #print(filename)


    slider1_var = IntVar()
    slider1_var.set(25) 
    slider_1 = Scale ( root, from_= 0, to_=200, orient=HORIZONTAL,variable=slider1_var,command=sigma)
    slider_1.place(in_=frame,relheight=0.1,relwidth=0.3,relx=0.65,rely=0.7,anchor=CENTER)

    slider2_var = IntVar()
    slider2_var.set(256) 
    slider_2 = Scale ( root, from_= 0, to_=500, orient=HORIZONTAL,variable=slider2_var,command= details_fun)
    slider_2.place(in_=frame,relheight=0.1,relwidth=0.3,relx=0.65,rely=0.8,anchor=CENTER)


    scale_x_y = slider_1.get()
    details = slider_2.get()

    

    pic = cv2.imread(filename)
    grey_pic = cv2.cvtColor(pic , cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_pic)
    blur = cv2.GaussianBlur (invert, (scale_x_y,scale_x_y),2000)
    invt_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_pic, invt_blur , scale = details)

    cv2.imwrite('test123.png',sketch)


    img_canva = Canvas (frame )
    img_canva.place( relheight=0.5 , relwidth=0.8 , relx=0.1 , rely=0.1 )


    #determining canvas width
    #Definig function to determine canvas width
    def resizer(e):
        global canva_width,img1
        canva_width = e.height
        #resizing image
        basewidth = canva_width
        img = Image.open('test123.png')
        wpercent = (basewidth/float(img.size[1]))
        hsize = int((float(img.size[0])*float(wpercent)))
        img = img.resize((hsize,basewidth),Image.ANTIALIAS)
    
        img1 =ImageTk.PhotoImage (img)
        img_canva.create_image(250,160,image=img1)
    
    #using bind to find width
    img_canva.bind('<Configure>',resizer)


    save_pic = Button ( frame , text = "Save pic" , fg="black" , bg="orange" , padx=10 , pady=10 , command= save_fun )
    save_pic.place(in_=frame,relheight=0.1,relwidth=0.3,relx=0.5,rely=0.9,anchor=CENTER)

    #lableing
    lable_1 = Label(frame,text='Outline')
    lable_1.place(in_=frame,relheight=0.1,relwidth=0.3,relx=0.35,rely=0.7,anchor=CENTER)
    
    lable_2 = Label(frame,text='Details')
    lable_2.place(in_=frame,relheight=0.1,relwidth=0.3,relx=0.35,rely=0.8,anchor=CENTER)






#end
    
    


def insert():
    global img_canva,img1,filename,filename_dummy

    filename= filedialog.askopenfilename (initialdir="C:/Users/Harikrishnan/Desktop/python/tkinter/project",title = "select file", filetypes=(("Jpg","*.jpg"),("All files" , "*.*")))
    
    img_canva.destroy()
    insert_pic.destroy()
    img_canva = Canvas (frame )
    img_canva.place( relheight=0.5 , relwidth=0.8 , relx=0.1 , rely=0.1 )

    if filename:
        change_pic = Button ( frame , text = "change pic" , fg="black" , bg="orange" , padx=10 , pady=10 , command= insert )
        change_pic.place(in_=frame,relheight=0.1,relwidth=0.3,relx=0.5,rely=0.8,anchor=CENTER)
    elif filename_dummy:
        filename = filename_dummy
        change_pic = Button ( frame , text = "change pic" , fg="black" , bg="orange" , padx=10 , pady=10 , command= insert )
        change_pic.place(in_=frame,relheight=0.1,relwidth=0.3,relx=0.5,rely=0.8,anchor=CENTER)
    else:
        filename='blank-profile-picture.webp'
        insert_pic1 = Button ( frame , text = "Insert pic" , fg="black" , bg="orange" , padx=10 , pady=10 , command= insert )
        insert_pic1.place(in_=frame,relheight=0.1,relwidth=0.3,relx=0.5,rely=0.8,anchor=CENTER)



    #determining canvas width
    #Definig function to determine canvas width
    def resizer(e):
        global canva_width,img1
        canva_width = e.height
        #resizing image
        basewidth = canva_width
        img = Image.open(filename)
        wpercent = (basewidth/float(img.size[1]))
        hsize = int((float(img.size[0])*float(wpercent)))
        img = img.resize((hsize,basewidth),Image.ANTIALIAS)    

        img1 =ImageTk.PhotoImage (img)
        img_canva.create_image(250,160,image=img1)


    #using bind to find width
    img_canva.bind('<Configure>',resizer)

    filename_dummy = filename
    





frame = Frame ( root, bg = "white" )
frame.place( relheight=0.9 , relwidth=0.9 , relx=0.5 , rely=0.5,anchor=CENTER )





img_canva = Canvas (frame )
img_canva.place( relheight=0.5 , relwidth=0.8 , relx=0.1 , rely=0.1 )


#determining canvas width
#Definig function to determine canvas width
def resizer(e):
    global canva_width,img1
    canva_width = e.height
    basewidth = canva_width
    img = Image.open('blank-profile-picture.webp')
    wpercent = (basewidth/float(img.size[1]))
    hsize = int((float(img.size[0])*float(wpercent)))
    img = img.resize((hsize,basewidth),Image.ANTIALIAS)
    img1 =ImageTk.PhotoImage (img)
    img_canva.create_image(250,160,anchor=CENTER,image=img1)
    #print(canva_width)


#using bind to find width
img_canva.bind('<Configure>',resizer)


#resizing image



#img1 =ImageTk.PhotoImage (img)
#img_canva.create_image(160,100,image=img1)

#pre_img = tk.Label(frame,image=img1)
#pre_img.place(relx=0.5,rely=0.5,anchor='center')





insert_pic = Button ( frame , text = "Insert pic" , fg="black" , bg="orange" , padx=10 , pady=10 , command= insert )
insert_pic.place(in_=frame,relheight=0.1,relwidth=0.3,relx=0.5,rely=0.8,anchor=CENTER)

edit_pic = Button ( frame , text = "Edit pic" , fg="black" , bg="orange" , padx=10 , pady=10 , command= edit_fun )
edit_pic.place(in_=frame,relheight=0.1,relwidth=0.3,relx=0.5,rely=0.9,anchor=CENTER)



root.mainloop()