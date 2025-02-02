import tkinter as tk

from tkinter import ttk 


root = tk.Tk()
root.title('Генератор секрета')
root.geometry('300x400')
root.resizable(False, False)
root.configure(bg='lightgray')

frame1 = ttk.Frame(root, padding=(10, 10, 10, 10), relief=tk.GROOVE)
frame2 = ttk.Frame(root, relief=tk.GROOVE)
frame3 = ttk.Frame(root, relief=tk.GROOVE)
frame4 = ttk.Frame(root, relief=tk.GROOVE)


frame1.pack(padx=4, pady=(4, 2), fill=tk.BOTH, expand=True)
frame2.pack(padx=4, pady=2, fill=tk.BOTH, expand=True)
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
    

root.mainloop()
