import tkinter as tk
from functools import partial

from lab_9.tools.calculator import Calculator


class CalculatorGUI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.variables = {}
        self.state = tk.BooleanVar(value=True)
        self.init_variables()
        self.calculator = Calculator()

        self.screen = tk.Label(self, bg='white')
        self.screen.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.bottom_pad = self.init_bottom_pad()
        self.bottom_pad.pack(side=tk.BOTTOM)

        self.keyboard_binding()

    def init_variables(self):
        self.variables['var_1'] = ''
        self.variables['var_2'] = ''
        self.variables['operator'] = ''
        self.state.set(True)

    def init_bottom_pad(self):
        bottom_pad = tk.Frame(self)

        # klawiatura pamięci
        mem_pad = tk.Frame(bottom_pad)
        mem_pad.pack(side=tk.LEFT)
        ii = 0
        tk.Button(
            mem_pad, text='MC', width=5,
            command=self.calculator.clean_memory
        ).grid(row=ii, column=0)
        ii += 1
        tk.Button(
            mem_pad, text='MR', width=5,
            command=self.replace_var
        ).grid(row=ii, column=0)
        ii += 1
        tk.Button(
            mem_pad, text='M+', width=5,
            command=self.calculator.memorize
        ).grid(row=ii, column=0)
        ii += 1
        tk.Button(
            mem_pad, text='C', width=5,
            command=self.clear
        ).grid(row=ii, column=0)

        # klawiatura numeryczna
        num_pad = tk.Frame(bottom_pad)
        num_pad.pack(side=tk.LEFT)
        ii = 0
        for ii, num in enumerate(range(9, 0, -1)):
            tk.Button(
                num_pad, text=num, width=5,
                command=partial(self.update_var, num)
            ).grid(row=ii // 3, column=(2-ii) % 3)
        ii += 1
        tk.Button(
            num_pad, text='0', width=5,
            command=partial(self.update_var, '0')
        ).grid(row=ii // 3, column=ii % 3)
        ii += 1
        tk.Button(
            num_pad, text='.', width=5,
            command=self.decimate_var
        ).grid(row=ii // 3, column=ii % 3)
        ii += 1
        tk.Button(
            num_pad, text='=', width=5,
            command=self.calculate_result
        ).grid(row=ii // 3, column=ii % 3)

        # klawiatura operacji
        operation_pad = tk.Frame(bottom_pad)
        operation_pad.pack(side=tk.RIGHT)
        for ii, operation in enumerate(self.calculator.operations.keys()):
            tk.Button(
                operation_pad, text=operation, width=5,
                command=partial(self.set_operator, operation),
            ).grid(row=ii, column=0)

        return bottom_pad

    def update_screen(self):
        text = f"{self.variables['var_1']}"
        if self.variables['operator']:
            text += f" {self.variables['operator']}"
        if self.variables['var_2']:
            text += f" {self.variables['var_2']}"
        self.screen['text'] = text

    def clear(self):
        state = self.state.get()
        if state:
            self.variables['var_1'] = ''
        else:
            self.variables['var_2'] = ''
        self.update_screen()

    def update_var(self, num, *args):
        state = self.state.get()
        if state:
            self.variables['var_1'] += str(num)
            self.variables['var_1'] = self.variables['var_1'].lstrip('0')
        else:
            self.variables['var_2'] += str(num)
            self.variables['var_2'] = self.variables['var_2'].lstrip('0')
        self.update_screen()

    def decimate_var(self):
        state = self.state.get()
        if state:
            if '.' not in self.variables['var_1']:
                self.variables['var_1'] += '.'
        else:
            if '.' not in self.variables['var_2']:
                self.variables['var_2'] += '.'
        self.update_screen()

    def replace_var(self):
        state = self.state.get()
        num = self.calculator.memory
        if state:
            self.variables['var_1'] += str(num)
        else:
            self.variables['var_2'] += str(num)
        self.update_screen()

    def get_var(self):
        if self.state:
            return self.variables['var_1']
        else:
            return self.variables['var_2']

    def set_operator(self, operator, *args):
        if self.variables['var_1']:
            self.variables['operator'] = operator
            self.state.set(not self.state.get())
            self.update_screen()

    def calculate_result(self, *args):
        if self.variables['var_1'] and self.variables['var_2']:
            var_1 = float(self.variables['var_1'])
            var_2 = float(self.variables['var_2'])
            val = self.calculator.run(
                self.variables['operator'], var_1, var_2
            )
            self.init_variables()
            self.screen['text'] = val
            # self.variables['var_1'] = str(val)

    def keyboard_binding(self):
        for num in range(10):
            self.bind(f'{num}', partial(self.update_var, num))
            self.bind(f'KP_{num}', partial(self.update_var, num))
        operators_strings = {
            'KP_Add': '+',
            'KP_Subtract': '-',
            'KP_Multiply': '*',
            'KP_Divide': '/'
        }
        # for key, val in operators_strings.items():
            # self.screen.bind(f'<{key}>', partial(self.set_operator, val))
        self.bind('<Return>', self.calculate_result)
        # self.bind('<Key>', print, add=True)
        self.focus_set()


if __name__ == '__main__':
    root = tk.Tk()
    CalculatorGUI(root).pack()
    root.mainloop()
