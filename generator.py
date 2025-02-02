import tkinter as tk

from tkinter import ttk 


def insert_text(text_widget: tk.Text, text: str):
    text_widget.config(state="normal")
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0", text)
    text_widget.config(state="disabled")


pass_symbol = '!@#%^-_'


root = tk.Tk()
root.title('Генератор секрета')
root.geometry('300x350')
root.resizable(False, False)
root.configure(bg='lightgray')

frame1 = ttk.Frame(root, padding=(10, 10, 10, 10), relief=tk.GROOVE)
frame2 = ttk.Frame(root, relief=tk.GROOVE)
frame3 = ttk.Frame(root, relief=tk.GROOVE)
frame4 = ttk.Frame(root, relief=tk.GROOVE)


frame1.pack(padx=4, pady=(4, 2), fill=tk.BOTH)
frame2.pack(padx=4, pady=2, fill=tk.BOTH)
frame3.pack(padx=4, pady=2, fill=tk.BOTH, expand=True)
frame4.pack(padx=4, pady=(2, 4), fill=tk.BOTH, expand=True)


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
combo.pack(pady=(5, 10))
combo['values'] = list(range(min_length, max_length + 1))
combo.set(min_length)


generated_text = tk.Text(frame3, background= 'white', font='Helvetica, 13', height=2, state="disabled")
generated_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
insert_text(generated_text, 'Ваш пароль будет здесь')

button1 = ttk.Button(frame3, text='Сгенерировать')
button1.pack(pady=(0, 10))

checks = []

var1 = tk.IntVar(value=1)
check1 = ttk.Checkbutton(frame4, text='A..Z', variable=var1)
checks.append(check1)
var2 = tk.IntVar(value=0)
check2 = ttk.Checkbutton(frame4, text='a..z', variable=var2)
checks.append(check2)
var3 = tk.IntVar(value=1)
check3 = ttk.Checkbutton(frame4, text='0..9', variable=var3)
checks.append(check3)
var4 = tk.IntVar(value=0)
check4 = ttk.Checkbutton(frame4, text=pass_symbol, variable=var4)
checks.append(check4)

for check in checks:
    check.pack(padx=10, pady=20, side=tk.LEFT)
    

root.mainloop()
