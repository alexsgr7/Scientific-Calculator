import tkinter as tk
from tkinter import ttk
import math
import functools

my_calculator = tk.Tk()
my_calculator.title("Smart Calculator")

frame = ttk.Frame(my_calculator, width=400, height=300)
frame.grid(row=0, column=0)

s = ttk.Style()
s.configure(my_calculator, background='grey', borderwidth=5, relief='raised')

label = ttk.Label(my_calculator, text='Smart Calculator')

resultsContents = tk.StringVar()
result_label = ttk.Label(my_calculator, textvariable=resultsContents)
result_label.grid(row=1, column=0, columnspan=4)  # Display the result label below the input field


class Calculator:

    def __init__(self, master):
        # Initialize the main application window
        self.master = master
        self.master.title("Calculator")

        self.frame = ttk.Frame(self.master)
        self.frame.grid(row=0, column=0)

        self.entry = ttk.Entry(self.frame)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        equal_button = ttk.Button(self.master, text='=', command=functools.partial(self.equality))
        plus_button = ttk.Button(self.master, text='+', command=functools.partial(self.addition_button))
        minus_button = ttk.Button(self.master, text='-', command=functools.partial(self.deduction_button))
        multiplication_button = ttk.Button(self.master, text='*', command=functools.partial(self.multiply))
        division_button = ttk.Button(self.master, text='/', command=functools.partial(self.divide))
        square_root_button = ttk.Button(self.master, text='√', command=functools.partial(self.square_root))
        exponentiation_button = ttk.Button(self.master, text='^', command=functools.partial(self.exponentiation))

        equal_button.grid(row=1, column=0)
        plus_button.grid(row=2, column=0)
        minus_button.grid(row=3, column=0)
        multiplication_button.grid(row=4, column=0)
        division_button.grid(row=5, column=0)
        square_root_button.grid(row=6, column=0)
        exponentiation_button.grid(row=7, column=0)

    def equality(self):
        try:
            # Get the expression from the entry widget
            expression = self.entry.get()

            # Evaluate the expression using eval
            result = eval(expression)

            # Display the result in a new window
            self.display_result(result)
        except Exception as e:
            # Handle any errors that may occur during evaluation
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def display_result(self, result):
        result_window = tk.Toplevel(self.master)
        result_window.title("Result")

        label = tk.Label(result_window, text="Result:")
        label.pack()

        result_label = tk.Label(result_window, text=result)
        result_label.pack()

    def addition_button(self):
        try:
            # Get the current content of the entry widget
            current_text = self.entry.get()

            # Split the current text into operands using the '+' operator
            operands = current_text.split('+')

            # Perform the addition
            result = 0
            for operand in operands:
                result += float(operand)

            # Update the entry widget with the result
            self.entry.delete(0, tk.END)  # Clear the entry
            self.entry.insert(0, str(result))
        except Exception as e:
            # Handle any errors that may occur during addition
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def deduction_button(self):
        try:
            # Get the current content of the entry widget
            current_text = self.entry.get()

            # Split the current text into operands using the '+' operator
            operands = current_text.split('-')

            # Perform the addition
            result = 0
            for operand in operands:
                result -= float(operand)

            # Update the entry widget with the result
            self.entry.delete(0, tk.END)  # Clear the entry
            self.entry.insert(0, str(result))
        except Exception as e:
            # Handle any errors that may occur during addition
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def multiply(self):
        try:
            # Get the current content of the entry widget
            current_text = self.entry.get()

            # Split the current text into operands using the '+' operator
            operands = current_text.split('*')

            # Perform the addition
            result = 0
            for operand in operands:
                result *= float(operand)

            # Update the entry widget with the result
            self.entry.delete(0, tk.END)  # Clear the entry
            self.entry.insert(0, str(result))
        except Exception as e:
            # Handle any errors that may occur during addition
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def divide(self):
        try:
            # Get the current content of the entry widget
            current_text = self.entry.get()

            # Split the current text into operands using the '+' operator
            operands = current_text.split('/')

            # Perform the addition
            result = 0
            for operand in operands:
                result /= float(operand)

            # Update the entry widget with the result
            self.entry.delete(0, tk.END)  # Clear the entry
            self.entry.insert(0, str(result))
        except Exception as e:
            # Handle any errors that may occur during addition
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def square_root(self):
        try:
            # Get the content of the widget
            current_text = self.entry.get()

            # Calculate the square root
            result = math.sqrt(float(current_text))

            # Update the entry widget with the result
            self.entry.delete(0, tk.END)  # Clear the entry
            self.entry.insert(0, str(result))
        except Exception as e:
            # Handle any errors that may occur during square root calculation
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def exponentiation(self):
        try:
            # Get the content of the widget
            current_text = self.entry.get()

            # Split the current text into operands using the '^' operator
            operands = current_text.split('^')

            # Ensure there are two operands for exponentiation
            if len(operands) == 2:
                base = float(operands[0])
                exponent = float(operands[1])
                result = base ** exponent

                # Update the entry widget with the result
                self.entry.delete(0, tk.END)  # Clear the entry
                self.entry.insert(0, str(result))
            else:
                # If there are not two operands, show an error
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error: Invalid input")
        except Exception as e:
            # Handle any errors that may occur during exponentiation
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")


calculator_instance = Calculator(my_calculator)

my_calculator.mainloop()
