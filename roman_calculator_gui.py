import tkinter as tk

# Mapping of Roman numerals to integers
roman_to_int_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

# Ordered list for converting integers to Roman numerals
int_to_roman_list = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

def roman_to_int(roman: str) -> int:
    """Convert a Roman numeral string to an integer."""
    i = 0
    total = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman_to_int_map[roman[i]] < roman_to_int_map[roman[i+1]]:
            total += roman_to_int_map[roman[i+1]] - roman_to_int_map[roman[i]]
            i += 2
        else:
            total += roman_to_int_map[roman[i]]
            i += 1
    return total

def int_to_roman(num: int) -> str:
    """Convert an integer to a Roman numeral string."""
    result = []
    for value, numeral in int_to_roman_list:
        while num >= value:
            result.append(numeral)
            num -= value
    return ''.join(result)

def calculate(roman1: str, roman2: str, op: str) -> str:
    """Perform arithmetic using Roman numerals."""
    a = roman_to_int(roman1)
    b = roman_to_int(roman2)
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a // b
    else:
        raise ValueError('Unsupported operator')
    if result <= 0:
        raise ValueError('Result cannot be represented as a Roman numeral')
    return int_to_roman(result)

class RomanCalculatorGUI:
    def __init__(self, master: tk.Tk):
        self.master = master
        master.title('Roman Calculator')
        self.display = tk.Entry(master, width=20, justify='right', font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.first_operand = ''
        self.operator = None
        self.create_buttons()

    def append_numeral(self, numeral: str) -> None:
        self.display.insert(tk.END, numeral)

    def set_operator(self, op: str) -> None:
        self.first_operand = self.display.get()
        self.operator = op
        self.display.delete(0, tk.END)

    def clear(self) -> None:
        self.display.delete(0, tk.END)
        self.first_operand = ''
        self.operator = None

    def equal(self) -> None:
        if not self.operator:
            return
        second_operand = self.display.get()
        try:
            result = calculate(self.first_operand, second_operand, self.operator)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, 'Error')
        finally:
            self.first_operand = ''
            self.operator = None

    def create_buttons(self) -> None:
        numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        for idx, numeral in enumerate(numerals):
            row = 1 + idx // 4
            col = idx % 4
            tk.Button(self.master, text=numeral, width=5, height=2,
                      command=lambda n=numeral: self.append_numeral(n)).grid(row=row, column=col, padx=2, pady=2)

        ops = ['+', '-', '*', '/']
        for idx, op in enumerate(ops):
            tk.Button(self.master, text=op, width=5, height=2,
                      command=lambda o=op: self.set_operator(o)).grid(row=3 + idx // 2, column=idx % 2 + 2, padx=2, pady=2)

        tk.Button(self.master, text='=', width=5, height=2, command=self.equal).grid(row=5, column=2, padx=2, pady=2)
        tk.Button(self.master, text='C', width=5, height=2, command=self.clear).grid(row=5, column=3, padx=2, pady=2)

if __name__ == '__main__':
    root = tk.Tk()
    calc = RomanCalculatorGUI(root)
    root.mainloop()
