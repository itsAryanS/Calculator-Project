from tkinter import *  # Importing necessary modules from tkinter library

first_number = second_number = operator = None  # Initializing variables

# Function to append the clicked digit to the current display on the calculator
def get_digit(digit):
    current = result_label['text']  # Getting the current text displayed
    new = current + str(digit)  # Appending the clicked digit to the current text
    result_label.config(text=new)  # Updating the display with the new text

# Function to clear the display
def clear():
    result_label.config(text='')  # Clearing the display

# Function to handle when an operator button is clicked
def get_operator(op):
    global first_number, operator

    first_number = int(result_label['text'])  # Storing the current displayed number as the first number
    operator = op  # Storing the operator clicked
    result_label.config(text='')  # Clearing the display for the next number input

# Function to calculate the result when the equal button is clicked
def get_result():
    global first_number, second_number, operator

    second_number = int(result_label['text'])  # Storing the current displayed number as the second number

    # Performing calculation based on the operator
    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text="error !")  # Handling division by zero
        else:
            result_label.config(text=str(first_number / second_number))

root = Tk()  # Creating the main window
root.title('Aryan\'s calculator')  # Setting the title of the window
root.geometry("325x250")  # Setting the size of the window
root.resizable(0, 0)  # Making the window non-resizable
root.configure(background='lightgray')  # Setting background color of the window

# Label to display the result
result_label = Label(root, text="", bg='lightgray', fg='black')
result_label.grid(row=0, column=0, columnspan=5, pady=(10, 10), sticky='w')  # Placing the label on the window
result_label.config(font=('verdana', 30, 'bold'))  # Setting font for the label

# Creating buttons for digits, operators, and other functionalities
btn7 = Button(root, text='7', bg='lightgray', fg='black', width=5, height=2, command=lambda: get_digit(7))
btn7.config(font=('verdana', 14))
btn7.grid(row=1, column=0)  # Placing the button on the window

btn8= Button(root,text='8',bg='lightgray',fg='black',width=5,height=2, command=lambda:get_digit(8))
btn8.config(font=('verdana',14))
btn8.grid(row=1,column=1)

btn9= Button(root,text='9',bg='lightgray',fg='black',width=5,height=2, command=lambda:get_digit(9))
btn9.config(font=('verdana',14))
btn9.grid(row=1,column=2)

btn_add= Button(root,text='+',bg='lightgray',fg='black',width=5,height=2, command=lambda: get_operator('+'))
btn_add.config(font=('verdana',14))
btn_add.grid(row=1,column=3)

btn4= Button(root,text='4',bg='lightgray',fg='black',width=5,height=2, command=lambda:get_digit(4))
btn4.config(font=('verdana',14))
btn4.grid(row=2,column=0)

btn5= Button(root,text='5',bg='lightgray',fg='black',width=5,height=2, command=lambda:get_digit(5))
btn5.config(font=('verdana',14))
btn5.grid(row=2,column=1)

btn6= Button(root,text='6',bg='lightgray',fg='black',width=5,height=2, command=lambda:get_digit(6))
btn6.config(font=('verdana',14))
btn6.grid(row=2,column=2)

btn_sub= Button(root,text='-',bg='lightgray',fg='black',width=5,height=2,command=lambda: get_operator('-'))
btn_sub.config(font=('verdana',14))
btn_sub.grid(row=2,column=3)

btn1= Button(root,text='1',bg='lightgray',fg='black',width=5,height=2, command=lambda:get_digit(1))
btn1.config(font=('verdana',14))
btn1.grid(row=3,column=0)

btn2= Button(root,text='2',bg='lightgray',fg='black',width=5,height=2, command=lambda:get_digit(2))
btn2.config(font=('verdana',14))
btn2.grid(row=3,column=1)

btn3= Button(root,text='3',bg='lightgray',fg='black',width=5,height=2, command=lambda:get_digit(3))
btn3.config(font=('verdana',14))
btn3.grid(row=3,column=2)

btn_mul= Button(root,text='*',bg='lightgray',fg='black',width=5,height=2,command=lambda: get_operator('*'))
btn_mul.config(font=('verdana',14))
btn_mul.grid(row=3,column=3)

btn_clr= Button(root,text='C',bg='lightgray',fg='black',width=5,height=2, command=lambda: clear())
btn_clr.config(font=('verdana',14))
btn_clr.grid(row=4,column=0)

btn0= Button(root,text='0',bg='lightgray',fg='black',width=5,height=2, command=lambda:get_digit(0))
btn0.config(font=('verdana',14))
btn0.grid(row=4,column=1)

btn_equals= Button(root,text='=',bg='lightgray',fg='black',width=5,height=2, command=lambda:get_result())
btn_equals.config(font=('verdana',14))
btn_equals.grid(row=4,column=2)

btn_div= Button(root,text='/',bg='lightgray',fg='black',width=5,height=2,command=lambda: get_operator('/'))
btn_div.config(font=('verdana',14))
btn_div.grid(row=4,column=3)



root.mainloop()