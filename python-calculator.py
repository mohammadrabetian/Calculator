import tkinter
from tkinter import messagebox, Menu
import math

# creating main window
window= tkinter.Tk()
window.geometry("254x354") # size of main window
window.resizable(0, 0) # for prevention to resize window
window.title("Calculator")


# definition of input text as string 
input_text = tkinter.StringVar()

# creating input_text frame
input_frame = tkinter.Frame(window, width=255, height=58, bg= 'white')
input_frame.pack(side= 'top')

# creating radio_button frame
radio_frame = tkinter.Frame(window, width=255, height=50, bg= 'RosyBrown1')
radio_frame.pack(side= 'top')

# creating num_button frame
num_frame = tkinter.Frame(window, width=255, height=240, bg= 'blue')
num_frame.pack(side= 'top')

# creating a input field inside the input_frame
input_entry = tkinter.Entry(input_frame, font= ("Helvetica",20,"bold"), textvariable= input_text, width=255, bg= 'white', justify= 'right', bd=0)
input_entry.pack(ipady=15)

# creating menu in top frame

menubar = Menu(window)

message1= lambda: messagebox.showinfo(title="About", message= "A GUI Calculator coded in Python 3 by tkinter module")
message2= lambda: messagebox.showinfo(title="Help", message= "default mode for trigonometric calculations is set on radiant mode")

menubar.add_command(label= "About", command= message1)
menubar.add_command(label= "Help", command= message2)

window.config(menu=menubar) # display the menu

# creating radio-button for deg or rad

var = tkinter.IntVar()
index = int()

def degree():
    global index
    index = var.get()
    return

deg = tkinter.Radiobutton(radio_frame, text="deg",width=4, height=1, font=("Helvetica",11), variable=var, value=1, command=lambda: degree())
deg.grid(row=0 ,column=0)
rad = tkinter.Radiobutton(radio_frame, text="rad",width=4, height=1, font=("Helvetica",11), variable=var, value=2, command=lambda: degree())
rad.grid(row=0 ,column=1)

################## functions ##################

output = ""
answer = ""

def click_btn(item):
    global output, answer
    if answer == "":
        output += str(item)
        input_text.set(output)
    else:
        output = str(answer) 
        output += str(item)
        input_text.set(output)
        answer = output
    return

def clear_btn():
    global output, answer
    output = ""
    answer = ""
    input_text.set(output)
    return

def equal_btn():
    global output, answer
    result = str(eval(output))
    input_text.set(result)
    answer = result
    output = ""
    return

def delete():
    global output, answer
    c = output[0:len(output)-1]
    input_text.set(c)
    answer = c
    output = c
    return

def sin_x():
    global output, answer
    if index==1:
        s = math.sin(math.radians(float(output)))
    else:
        s = math.sin(float(output))
    input_text.set(s)
    answer = s
    output = ""
    return

def cos_x():
    global output, answer
    if index==1:
        co = math.cos(math.radians(float(output)))
    else:
        co = math.cos(float(output))
    input_text.set(co)
    answer = co
    output = ""
    return

def tan_x():
    global output, answer
    if index==1:
        t = math.tan(math.radians(float(output)))
    else:
        t = math.tan(float(output))
    input_text.set(t)
    answer = t
    output = ""
    return

def square_x():
    global output, answer
    squared = float(output)**2
    input_text.set(squared)
    answer = squared
    output = ""
    return

def root_x():
    global output, answer
    rooted = math.sqrt(float(output))
    input_text.set(rooted)
    answer = rooted
    output = ""
    return


# creating buttons

sin = tkinter.Button(num_frame, text="sin" ,width=3 , height=1, font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: sin_x())

cos = tkinter.Button(num_frame, text="cos", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: cos_x())

tan = tkinter.Button(num_frame, text="tan", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: tan_x())

DEL = tkinter.Button(num_frame, text="Del", width=7 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: delete())

clear = tkinter.Button(num_frame, text="CE", width=7 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: clear_btn())

seven = tkinter.Button(num_frame, text="7", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("7"))

eight = tkinter.Button(num_frame, text="8", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("8"))

nine = tkinter.Button(num_frame, text="9", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("9"))

multiple = tkinter.Button(num_frame, text="x", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("*"))

divide = tkinter.Button(num_frame, text="÷", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("/"))

four = tkinter.Button(num_frame, text="4", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("4"))

five = tkinter.Button(num_frame, text="5", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("5"))

six = tkinter.Button(num_frame, text="6", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("6"))

plus = tkinter.Button(num_frame, text="+", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("+"))

minus = tkinter.Button(num_frame, text="-", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("-"))

one = tkinter.Button(num_frame, text="1", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("1"))

two = tkinter.Button(num_frame, text="2", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("2"))

three = tkinter.Button(num_frame, text="3", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("3"))

root = tkinter.Button(num_frame, text="√", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: root_x())

square = tkinter.Button(num_frame, text="x²", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: square_x())

point = tkinter.Button(num_frame, text=".", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("."))

zero = tkinter.Button(num_frame, text="0", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("0"))

pi = tkinter.Button(num_frame, text="π", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("3.141592653"))

equal = tkinter.Button(num_frame, text="=", width=11 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: equal_btn())

left_pr = tkinter.Button(num_frame, text="(", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn("("))

rigt_pr = tkinter.Button(num_frame, text=")", width=3 , height=1 , font=("Helvetica",16,"bold") , bg="grey" , fg="white" , command=lambda: click_btn(")"))

# griding buttons

sin.grid(row = 0, column = 0, padx = 1, pady = 1)
cos.grid(row = 0, column = 1, padx = 1, pady = 1)
tan.grid(row = 0, column = 2, padx = 1, pady = 1)
clear.grid(row = 0, column = 3, columnspan=2, padx = 0, pady = 1)
seven.grid(row = 2, column = 0, padx = 1, pady = 1)
eight.grid(row = 2, column = 1, padx = 1, pady = 1)
nine.grid(row = 2, column = 2, padx = 1, pady = 1)
DEL.grid(row = 1, column = 3, columnspan=2, padx = 0, pady = 1)
four.grid(row = 3, column = 0, padx = 1, pady = 1)
five.grid(row = 3, column = 1, padx = 1, pady = 1)
six.grid(row = 3, column = 2, padx = 1, pady = 1)
multiple.grid(row = 2, column = 3, padx = 1, pady = 1)
divide.grid(row = 2, column = 4, padx = 1, pady = 1)
one.grid(row = 4, column = 0, padx = 1, pady = 1)
two.grid(row = 4, column = 1, padx = 1, pady = 1)
three.grid(row = 4, column = 2, padx = 1, pady = 1)
plus.grid(row = 3, column = 3, padx = 1, pady = 1)
minus.grid(row = 3, column = 4, padx = 1, pady = 1)
point.grid(row = 5, column = 0, padx = 1, pady = 1)
zero.grid(row = 5, column = 1, padx = 1, pady = 1)
pi.grid(row = 1, column = 2, padx = 1, pady = 1)
root.grid(row = 1, column = 0, padx = 1, pady = 1)
square.grid(row = 1, column = 1, padx = 1, pady = 1)
equal.grid(row = 5, column = 2, columnspan=3, padx = 0, pady = 1)
left_pr.grid(row = 4, column = 3, padx = 1, pady = 1)
rigt_pr.grid(row = 4, column = 4, padx = 1, pady = 1)


window.mainloop()