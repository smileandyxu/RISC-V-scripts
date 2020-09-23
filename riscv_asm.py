# !/user/bin/env Python3
# -*- coding:utf-8 -*-

import os
from tkinter import Tk
from tkinter import Button, Text, Menu
from tkinter import dialog, filedialog, messagebox
from riscv_encode import legal_riscv, asm_to_bin

class riscvasm_GUI():
    def __init__(self, window):
        self.window = window
    
    def set_init_window(self):
        self.window.title('简易RISC-V汇编工具')
        self.window.geometry('1280x720+20+20')

        self.text_asm = Text(
            self.window
        )

        self.menubar = Menu(self.window)
        self.menu_file = Menu(self.menubar, tearoff=False)
        self.menu_file.add_command(label='打开', command=self.load_file)
        self.menu_file.add_command(label='生成', command=self.trans_asm_to_coe)
        self.menu_file.add_command(label='退出', command=self.window.quit)
        self.menubar.add_cascade(label='文件', menu=self.menu_file)

        self.window.config(menu=self.menubar)
        self.window.mainloop()
    
    def load_file(self):
        self.file_path = filedialog.askopenfilename(
            title='选择文件', initialdir=('./'), 
            filetypes=[('Assembly', '.s'), ('Assembly', '.asm')]
        )
        with open(file=self.file_path, mode='r+', encoding='utf-8') as file:
            self.file_text_asm = file.read()
        self.text_asm.insert('insert', self.file_text_asm)
        self.text_asm.pack()
        self.window.update()

    def trans_asm_to_coe(self):
        index = 0
        self.text_coe = [
            'memory_initialization_radix=16', 
            'memory_initialization_vector='
        ]
        for line in self.text_asm:
            index += 1
            if not legal_riscv(line):
                messagebox.showerror('错误', '第{}行错误'.format(index))
                break
            else:
                self.text_coe.append(asm_to_bin(line))
        

if __name__ == "__main__":
    app = riscvasm_GUI(Tk())
    app.set_init_window()
    