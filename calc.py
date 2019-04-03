import tkinter as tk
import os

class Calculator(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)

		self.title("Calculator")
		self.geometry('320x380')

		self.number = tk.StringVar()
		self.num = 0
		self.operator = ''

		self.textentry = tk.Entry(self, width=47, 
								bg='white', 
								justify='right',
								textvariable=self.number)

		# Creating 17 buttons for the calculator interface
		self.button1 = tk.Button(self, text='7', command=lambda:self.setText(7))
		self.button2 = tk.Button(self, text='8', command=lambda:self.setText(8))
		self.button3 = tk.Button(self, text='9', command=lambda:self.setText(9))
		self.button4 = tk.Button(self, text='/', command=lambda:self.setText('/'))

		self.button5 = tk.Button(self, text='4', command=lambda:self.setText(4))
		self.button6 = tk.Button(self, text='5', command=lambda:self.setText(5))
		self.button7 = tk.Button(self, text='6', command=lambda:self.setText(6))
		self.button8 = tk.Button(self, text='*', command=lambda:self.setText('*'))

		self.button9 = tk.Button(self, text='1', command=lambda:self.setText(1))
		self.button10 = tk.Button(self, text='2', command=lambda:self.setText(2))
		self.button11 = tk.Button(self, text='3', command=lambda:self.setText(3))
		self.button12 = tk.Button(self, text='-', command=lambda:self.setText('-'))

		self.button13 = tk.Button(self, text='C', command=self.btnClearDisplay)
		self.button14 = tk.Button(self, text='0', command=lambda:self.setText(0))
		self.button15 = tk.Button(self, text='=', command=self.btnEqualsOutput)
		self.button16 = tk.Button(self, text='+', command=lambda:self.setText('+'))

		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)
		self.columnconfigure(2, weight=1)
		self.columnconfigure(3, weight=1)
		self.columnconfigure(4, weight=1)
		self.columnconfigure(5, weight=1)
		self.columnconfigure(6, weight=1)

		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)
		self.rowconfigure(2, weight=1)
		self.rowconfigure(3, weight=1)
		self.rowconfigure(4, weight=1)
		self.rowconfigure(5, weight=1)

		self.textentry.grid(row=0, column=0, pady=20, sticky='N', columnspan=5)
		self.button1.grid(row=1, column=1, sticky='nsew')
		self.button2.grid(row=1, column=2, sticky='nsew')
		self.button3.grid(row=1, column=3, sticky='nsew')
		self.button4.grid(row=1, column=4, sticky='nsew')

		self.button5.grid(row=2, column=1, sticky='nsew')
		self.button6.grid(row=2, column=2, sticky='nsew')
		self.button7.grid(row=2, column=3, sticky='nsew')
		self.button8.grid(row=2, column=4, sticky='nsew')

		self.button9.grid(row=3, column=1, sticky='nsew')
		self.button10.grid(row=3, column=2, sticky='nsew')
		self.button11.grid(row=3, column=3, sticky='nsew')
		self.button12.grid(row=3, column=4, sticky='nsew')

		self.button13.grid(row=4, column=1, sticky='nsew')
		self.button14.grid(row=4, column=2, sticky='nsew')
		self.button15.grid(row=4, column=3, sticky='nsew')
		self.button16.grid(row=4, column=4, sticky='nsew')


	def setText(self,num):
		self.operator = self.operator + str(num)
		self.number.set(self.operator)

	def btnClearDisplay(self):
		self.operator=''
		self.number.set('')

	def btnEqualsOutput(self):
		self.sumup = str(eval(self.operator))
		self.number.set(self.sumup)
		self.operator=''


app = Calculator()
app.mainloop()