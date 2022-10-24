import tkinter as tk
from tkinter import messagebox
import math

# === Функции ===

def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*!':
        value = value[:-1]
    if value[0] == '0' and not(len(value) == 1):
        value = value[1:]
    # elif '+' in value or '-' in value or '*' in value or '/' in value: 
    #     calculate()
    #     value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def sus_box():
    messagebox.showerror('ඞ KINDA SUS ඞ', "ඞඞඞ THERE'S IMPOSTER AMONG US ඞඞඞඞ")

def memo():
    messagebox.showinfo('Справка.',
     'Особенности Калькулятора:\nСимвол "**" - возведение в степень.\nАмогуса не трогай.\nКнопки с библиотеки math пишутся без скобки в конце, пиши пока сам.'
     '\nКнопка "," выводит запятую с пробелом впереди.'
     '\nВ тригонометрических функцях (sin, cos, tan) на место числа нужно вписывать радианы.'
     '\n')

def calculate():
    value = calc.get()
    if value[-1] in '+-*/!':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    if value[0] == 'ඞ':
        try:
            calc.insert(0, eval(value))
        except (NameError, SyntaxError):
            sus_box()   
            calc.insert(0, 'ඞ') 
    if value[0] != 'ඞ':  
        try:
            calc.insert(0, eval(value))
        except (NameError, SyntaxError):
            messagebox.showinfo('Внимание!', 'Где цифры чорт?')
            calc.insert(0, 0)  
        except ZeroDivisionError:
            window_zero = messagebox.askyesno('Внимание!', 'Совсем тупенький, да?')      
            if window_zero == messagebox.YES or window_zero == messagebox.NO:
                sus_box()    
            calc.insert(0, 0)
   
def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')

def make_clear_button(operation):
    return tk.Button(text= operation, bd= 5, font= {'Arial', 15}, fg = 'red', command= clear)   

def make_digit_button(digit):
    return tk.Button(text= digit, bd= 5, font= {'Arial', 15}, command= lambda : add_digit(digit))

def make_amogus_button(digit):
    return tk.Button(text= digit, bd= 5, font= {'Arial', 15}, fg = 'white', command= lambda : add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text= operation, bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text= operation, bd= 5, font= {'Arial', 15}, fg = 'red', command= calculate)

def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/ඞ!':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()

# def leftKey(event):
#      return tk.Button(text= '<', bd = 5, font= {'Arial', 15}, fg = 'gray', command= lambda: '<Left>')

# def rightKey(event):
#      return tk.Button(text= '>', bd = 5, font= {'Arial', 15}, fg = 'gray', command= lambda: '<Right>')

def make_memo_button():
    return tk.Button(text= 'Справка', bd = 5, font= {'Arial', 15}, fg = 'gray', command= memo)

def make_factorial_button(digit):
    return tk.Button(text= '!', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))

def make_log_button(digit):
    return tk.Button(text= 'logₓ(y)', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))

def make_comma_button(digit):
    return tk.Button(text= ',', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))    

def make_sqrt_button(digit):
    return tk.Button(text= '√', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))   

def make_pi_button(digit):
    return tk.Button(text= '𝞹', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))

def make_e_button(digit):
    return tk.Button(text= 'e', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))

def make_sin_button(digit):
    return tk.Button(text= 'sin(x)', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))    

def make_cos_button(digit):
    return tk.Button(text= 'cos(x)', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))

def make_tan_button(digit):
    return tk.Button(text= 'tan(x)', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))

def make_hypot_button(digit):
    return tk.Button(text= 'Гипотенуза П/У', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))

def make_pow_button(digit):
    return tk.Button(text= 'X^Y', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))

def make_rad_button(digit):
    return tk.Button(text= '° => rad', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))  

def make_degree_button(digit):
    return tk.Button(text= 'rad => °', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))      

def make_dot_button(digit):
    return tk.Button(text= '.', bd= 5, font= {'Arial', 15}, fg = 'red', command= lambda : add_digit(digit))

# === Работа с окном ===.

win = tk.Tk()
win.title('Калькулятор!ඞ') # <---- Сюда название
photo_title = tk.PhotoImage(file= '2116373623456.png') # <---- Сюда иконку
win.iconphoto(False, photo_title)

# win.bind('<Left>', leftKey)
# win.bind('<Right>', rightKey)

win['bg'] = 'lightslategrey'
win.geometry('900x600+500+100') # <---- Здесь менять размер
win.resizable(False, False) 

win.bind('<Key>', press_key)

# === Поле ввода === 

calc = tk.Entry(win, justify= tk.RIGHT, font= {'Arial', 20}, width= 20)
calc.insert(0, '0')
calc.grid(row= 0, column= 0, columnspan= 8, stick= 'we', padx = 5)

# === Кнопки ===

#    ___кнопки цифр___
make_digit_button('1').grid(row= 1, column= 0, stick = 'wens', padx= 5, pady= 5)
make_digit_button('2').grid(row= 1, column= 1, stick = 'wens', padx= 5, pady= 5)
make_digit_button('3').grid(row= 1, column= 2, stick = 'wens', padx= 5, pady= 5)
make_digit_button('4').grid(row= 2, column= 0, stick = 'wens', padx= 5, pady= 5)
make_digit_button('5').grid(row= 2, column= 1, stick = 'wens', padx= 5, pady= 5)
make_digit_button('6').grid(row= 2, column= 2, stick = 'wens', padx= 5, pady= 5)
make_digit_button('7').grid(row= 3, column= 0, stick = 'wens', padx= 5, pady= 5)
make_digit_button('8').grid(row= 3, column= 1, stick = 'wens', padx= 5, pady= 5)
make_digit_button('9').grid(row= 3, column= 2, stick = 'wens', padx= 5, pady= 5)
make_digit_button('0').grid(row= 4, column= 1, stick = 'wens', padx= 5, pady= 5)
#    ___кнопки операций___
make_operation_button('+').grid(row= 1, column= 4, stick = 'wens', padx= 5, pady= 5)
make_operation_button('-').grid(row= 2, column= 4, stick = 'wens', padx= 5, pady= 5)
make_operation_button('/').grid(row= 3, column= 4, stick = 'wens', padx= 5, pady= 5)
make_operation_button('*').grid(row= 4, column= 4, stick = 'wens', padx= 5, pady= 5)
make_operation_button('(').grid(row= 9, column= 4, stick = 'wens', padx= 5, pady= 5)
make_operation_button(')').grid(row= 9, column= 5, stick = 'wens', padx= 5, pady= 5)

#    ___специальные кнопки___
make_pow_button('math.pow(').grid(row= 5, column= 5, stick = 'wens', padx= 5, pady= 5)

make_factorial_button('math.factorial(').grid(row= 2, column= 5, stick = 'wens', padx= 5, pady= 5)
make_log_button('math.log(').grid(row= 3, column= 5, stick = 'wens', padx= 5, pady= 5)
make_comma_button(', ').grid(row= 4, column= 5, stick = 'wens', padx= 5, pady= 5)
make_sqrt_button('math.sqrt(').grid(row= 1, column= 5, stick = 'wens', padx= 5, pady= 5)
make_pi_button('math.pi').grid(row= 5, column= 4, stick = 'wens', padx= 5, pady= 5)
make_e_button('math.e').grid(row= 6, column= 4, stick = 'wens', padx= 5, pady= 5)
make_sin_button('math.sin(').grid(row= 1, column= 6, stick = 'wens', padx= 5, pady= 5)
make_cos_button('math.cos(').grid(row= 2, column= 6, stick = 'wens', padx= 5, pady= 5)
make_tan_button('math.tan(').grid(row= 3, column= 6, stick = 'wens', padx= 5, pady= 5)
make_rad_button('math.radians(').grid(row= 4, column= 6, stick = 'wens', padx= 5, pady= 5)
make_degree_button('math.degrees(').grid(row= 5, column= 6, stick = 'wens', padx= 5, pady= 5)
make_dot_button('.').grid(row= 5, column= 1, stick = 'wens', padx= 5, pady= 5)
# leftKey('<Left>').grid(row=3, column= 10, stick= 'wens', padx = 5, pady = 5)
# rightKey('<Right>').grid(row=3, column= 11, stick= 'wens', padx = 5, pady = 5)

#   ___Основа___ 
make_calc_button('=').grid(row= 4, column= 2, stick = 'wens', padx= 5, pady= 5)
make_clear_button('C').grid(row= 4, column= 0, stick = 'wens', padx= 5, pady= 5)
#   ___Справка___
make_memo_button().grid(row=0, column= 9, stick= 'wens', padx = 5, pady = 5)

# ඞඞඞඞ amogus button ඞඞඞඞ
make_amogus_button('ඞ').grid(row= 11, column= 0, stick = 'wens', padx= 15, pady= 5)

# === Расположение кнопок ===
win.grid_columnconfigure(0, minsize= 75)
win.grid_columnconfigure(1, minsize= 75)
win.grid_columnconfigure(2, minsize= 75)
win.grid_columnconfigure(3, minsize= 75)
win.grid_columnconfigure(4, minsize= 80)

win.grid_rowconfigure(1, minsize= 75)
win.grid_rowconfigure(2, minsize= 75)
win.grid_rowconfigure(3, minsize= 75)
win.grid_rowconfigure(4, minsize= 75)

win.mainloop() 
