import tkinter as tk
from tkinter import ttk
import string
import random


class GeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__configure()
        self.__place_frame()

    def __configure(self):
        self.title('Генератор секрета')
        self.geometry('300x380')
        self.resizable(False, False)
        self.configure(bg='lightgray')

    def __place_frame(self):
       PasswordFrame(parent=self)   


class PasswordFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pass_symbol = '!@#%^-_'
        self.password_text = 'Your password'


        self.__set_styles()

        self.__init_frames()
        self.__compose_frame1(self.__frame1)
        self.__compose_frame2(self.__frame2)
        self.__compose_frame3(self.__frame3)
        self.__compose_frame4(self.__frame4)
        self.__place_frames()

        self.pack()

    def __init_frames(self):
        self.__frame1 = ttk.Frame(self, padding=(10, 10, 10, 10), relief=tk.GROOVE)
        self.__frame2 = ttk.Frame(self, relief=tk.GROOVE)
        self.__frame3 = ttk.Frame(self, relief=tk.GROOVE)
        self.__frame4 = ttk.Frame(self, padding=(0, 0, 5, 5), relief=tk.GROOVE)

    def __place_frames(self):
        self.__frame1.pack(padx=4, pady=(4, 2), fill=tk.BOTH)
        self.__frame2.pack(padx=4, pady=2, fill=tk.BOTH)
        self.__frame3.pack(padx=4, pady=2, fill=tk.BOTH, expand=True)
        self.__frame4.pack(padx=4, pady=(2, 2), fill=tk.BOTH, expand=True)

    def __set_styles(self):
        label_style = ttk.Style()
        label_style.configure('TLabel', font=("Arial", 12))

        check_style = ttk.Style()
        check_style.configure('TCheckbutton', font=("Arial", 12))

        button_style = ttk.Style()
        button_style.configure('TButton', font=("Arial", 12))

        radio_style = ttk.Style()
        radio_style.configure('TRadiobutton', font=("Arial", 12))

    def __compose_frame1(self, frame):
        radios = []

        self.radio_var = tk.IntVar(value=1) 
        radio1 = ttk.Radiobutton(frame, text='Пароль', variable=self.radio_var, value=1)
        radios.append(radio1)
        radio2 = ttk.Radiobutton(frame, text='Парольная фраза', variable=self.radio_var, value=2, command=self.destroy3)
        radios.append(radio2)
        radio3 = ttk.Radiobutton(frame, text='Никнейм', variable=self.radio_var, value=3, state=tk.DISABLED)
        radios.append(radio3)

        for radio in radios:
            radio.pack(pady=2, anchor='w')

    def __compose_frame2(self, frame):
        self.label1 = ttk.Label(frame, text='Длина пароля')
        self.label1.pack(pady=5)
        self.min_length = 8
        self.max_length = 15
        self.combo = ttk.Combobox(frame, state='readonly')
        self.combo.pack(pady=(5, 15))
        self.combo['values'] = list(range(self.min_length, self.max_length + 1))
        self.combo.set(self.min_length)
        
    def __compose_frame3(self, frame):
        self.generated_text = tk.Text(
            self.__frame3, background= 'white', font='Helvetica, 13', height=2, state="disabled"
        )
        self.generated_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.generated_text.tag_configure("center", justify="center")
        self.insert_text(self.generated_text, self.password_text)


        self.icon_file = tk.PhotoImage(file="copy.png") # type: ignore

        self.copy_button = tk.Button(frame, image=self.icon_file, command=self.copy_to_clipboard, state='disabled')
        self.copy_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor='e')

        generate_button = ttk.Button(
            self.__frame3, text='Сгенерировать', command=lambda: self.generate_password( 
                length=self.combo.get(), 
                upper=self.var1.get(), 
                numbers=self.var2.get(), 
                symbols=self.var3.get()
            )
        )
        generate_button.pack(side=tk.LEFT, expand=True, padx=(50, 0), pady=(0, 10))

    def __compose_frame4(self, frame):

        label2 = ttk.Label(frame, text='Добавить символы')
        label2.pack(pady=(10, 0))

        checks = []

        self.var1 = tk.IntVar(value=1)
        check1 = ttk.Checkbutton(frame, text='A..Z', variable=self.var1)
        checks.append(check1)
        self.var2 = tk.IntVar(value=1)
        check2 = ttk.Checkbutton(frame, text='0..9', variable=self.var2)
        checks.append(check2)
        self.var3 = tk.IntVar(value=1)
        check3 = ttk.Checkbutton(frame, text=self.pass_symbol, variable=self.var3)
        checks.append(check3)

        for check in checks:
            check.pack(padx=15, pady=10, side=tk.LEFT)

    def insert_text(self, text_widget: tk.Text, text: str):
        text_widget.config(state="normal")
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", text, "center")
        text_widget.config(state="disabled")

    def generate_password(self, length: str, upper: bool = True , numbers: bool = False, symbols: bool = False):
        all_letters = string.ascii_uppercase * upper \
        + string.digits * numbers \
        + self.pass_symbol * symbols \
        + string.ascii_lowercase
        password = random.choice(string.ascii_lowercase) \
        + random.choice(string.ascii_uppercase) * upper \
        + random.choice(string.digits) * numbers \
        + random.choice(self.pass_symbol) * symbols
        self.password_text = password + ''.join(random.sample(all_letters, int(length) - len(password)))

        password_list = list(self.password_text)
        random.shuffle(password_list)     
        shuffled_password_text = ''.join(password_list) 
        self.insert_text(self.generated_text, shuffled_password_text)
        self.copy_button.config(state='active')

    def copy_to_clipboard(self):
        text_to_copy = self.generated_text.get("1.0", tk.END).replace('\n', '') 
        self.parent.clipboard_clear() 
        self.parent.clipboard_append(text_to_copy)
        self.copy_button.config(state='disabled')        

    def destroy3(self):
        self.destroy()
        PhraseFrame(parent=self.parent)

class PhraseFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent        
        label2 = ttk.Label(self, text='Добавить символы')
        label2.pack(pady=(10, 0))

        self.pack(fill=tk.BOTH, expand=True)
        self.pack()
