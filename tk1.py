import tkinter as tk

class Test(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.button = tk.Button(text='Hello', command=self.click)
		self.button.grid(row=1, column=3)
		self.button = tk.Button(text='Hi')
		self.button.grid(row=1, column=1)

	def click(self):
		print('Welcome to TkInter! :)')

root = Test()
root.mainloop()