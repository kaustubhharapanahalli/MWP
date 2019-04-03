import tkinter as tk

class App:

	def __init__(self, master):
		frame = tk.Frame(master)
		frame.pack()

		self.button = tk.Button(frame, text='Print Msg', command=self.click)
		self.button.pack(side=tk.LEFT)

		self.quit = tk.Button(frame, text="Quit", command=frame.quit)
		self.quit.pack(side=tk.LEFT)

	def click(self):
		print("Hello there! How are you?")

root = tk.Tk()
app = App(root)
root.mainloop()