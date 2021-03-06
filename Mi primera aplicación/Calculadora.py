from tkinter import *

#changes the widget title
root = Tk()
root.title("Mi primera aplicación")

label = Label(root, text= "Calculator", font=('Arial bold', 15))
label.grid(row=0, column=1, columnspan=1)

#columnspan tells the number of columns its gonna have
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_number = int(entry.get())
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)

def button_subtract():
    first_number = int(entry.get())
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = int(entry.get())
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = int(entry.get())
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)

def button_power():
    first_number = int(entry.get())
    global f_num
    global math
    math = "potentiation"
    f_num = int(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, int(f_num) + int(second_number))
    if math == "substraction":
        entry.insert(0, int(f_num) - int(second_number))
    if math == "multiplication":
        entry.insert(0, int(f_num) * int(second_number))
    if math == "division":
        entry.insert(0, int(f_num) // int(second_number))
    if math == "potentiation":
        entry.insert(0, int(f_num) ** int(second_number))

#define buttons
button_0 = Button(root, text=0, padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text=1, padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text=2, padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text=3, padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text=4, padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text=5, padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text=6, padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text=7, padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text=8, padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text=9, padx=40, pady=20, command=lambda: button_click(9))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=41, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)
button_power = Button(root, text="pow", padx=31, pady=20, command=button_power)
button_equal = Button(root, text="=", padx=39, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=77, pady=20, command=button_clear)

#put the button on the screen in order
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)

button_add.grid(row=5,column=1)
button_subtract.grid(row=5,column=2)
button_multiply.grid(row=6,column=0)
button_divide.grid(row=6,column=1)
button_power.grid(row=6,column=2)
button_equal.grid(row=7,column=0)
button_clear.grid(row=7,column=1, columnspan=2)

root.mainloop()