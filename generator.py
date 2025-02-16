import random
import tkinter as tk
import string
from tkinter import IntVar, ttk 

password_text = 'Ваш пароль будет здесь'
pass_symbol = '!@#%^-_'


def insert_text(text_widget: tk.Text, text: str):
    text_widget.config(state="normal")
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0", "\n")
    text_widget.insert("2.0", text, "center")
    text_widget.config(state="disabled")


def button_click(length: str, upper: bool = True , numbers: bool = False, symbols: bool = False):
    all_letters = string.ascii_uppercase * upper \
    + string.digits * numbers \
    + pass_symbol * symbols \
    + string.ascii_lowercase
    password = random.choice(string.ascii_lowercase) \
    + random.choice(string.ascii_uppercase) * upper \
    + random.choice(string.digits) * numbers \
    + random.choice(pass_symbol) * symbols
    password_text = password + ''.join(random.sample(all_letters, int(length) - len(password)))

    password_list = list(password_text)  # Convert to a list of characters
    random.shuffle(password_list)        # Shuffle the list in place
    shuffled_password_text = ''.join(password_list)  # Convert back to a string
    insert_text(generated_text, shuffled_password_text)


root = tk.Tk()
root.title('Генератор секрета')
root.geometry('300x400')
root.resizable(False, False)
root.configure(bg='lightgray')

frame1 = ttk.Frame(root, padding=(10, 10, 10, 10), relief=tk.GROOVE)
frame2 = ttk.Frame(root, relief=tk.GROOVE)
frame3 = ttk.Frame(root, relief=tk.GROOVE)
frame4 = ttk.Frame(root, relief=tk.GROOVE)


frame1.pack(padx=4, pady=(4, 2), fill=tk.BOTH)
frame2.pack(padx=4, pady=2, fill=tk.BOTH)
frame3.pack(padx=4, pady=2, fill=tk.BOTH, expand=True)
frame4.pack(padx=4, pady=(2, 2), fill=tk.BOTH, expand=True)


label_style = ttk.Style()
label_style.configure('TLabel', font=("Arial", 12))

check_style = ttk.Style()
check_style.configure('TCheckbutton', font=("Arial", 12))

button_style = ttk.Style()
button_style.configure('TButton', font=("Arial", 12))

radio_style = ttk.Style()
radio_style.configure('TRadiobutton', font=("Arial", 12))

radios = []

radio_var = tk.IntVar(value=1) 
radio1 = ttk.Radiobutton(frame1, text='Пароль', variable=radio_var, value=1)
radios.append(radio1)
radio2 = ttk.Radiobutton(frame1, text='Парольная фраза', variable=radio_var, value=2, state=tk.DISABLED)
radios.append(radio2)
radio3 = ttk.Radiobutton(frame1, text='Никнейм', variable=radio_var, value=3, state=tk.DISABLED)
radios.append(radio3)

for radio in radios:
    radio.pack(pady=2, anchor='w')



label1 = ttk.Label(frame2, text='Длина пароля')
label1.pack(pady=5)

min_length = 8
max_length = 15
combo = ttk.Combobox(frame2, state='readonly')
combo.pack(pady=(5, 15))
combo['values'] = list(range(min_length, max_length + 1))
combo.set(min_length)


generated_text = tk.Text(
    frame3, background= 'white', font='Helvetica, 13', height=2, state="disabled"
)
generated_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
generated_text.tag_configure("center", justify="center")
insert_text(generated_text, password_text)

button1 = ttk.Button(
    frame3, text='Сгенерировать', command=lambda: button_click(
        length=combo.get(), 
        upper=var1.get(), 
        numbers=var2.get(), 
        symbols=var3.get()
    )
)
button1.pack(pady=(0, 10))

label2 = ttk.Label(frame4, text='Добавить символы')
label2.pack(pady=(10, 0))

checks = []

var1 = tk.IntVar(value=1)
check1 = ttk.Checkbutton(frame4, text='A..Z', variable=var1)
checks.append(check1)
var2 = tk.IntVar(value=1)
check2 = ttk.Checkbutton(frame4, text='0..9', variable=var2)
checks.append(check2)
var3 = tk.IntVar(value=1)
check3 = ttk.Checkbutton(frame4, text=pass_symbol, variable=var3)
checks.append(check3)


for check in checks:
    check.pack(padx=15, pady=0, side=tk.LEFT)
    

root.mainloop()
