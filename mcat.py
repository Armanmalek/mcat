from Tkinter import * 
import csv  


class mcatGui:

	def __init__(self, master) :
		self.master = master 
		master.title("OMSAS GPA Calculator") 
		self.label = Label(master, text = "Calculate GPA")
		self.label.pack() 

		self.greet_button = Button(master, text = "Calculate", command=self.greet)
		self.greet_button.pack() 
	
		self.close_button = Button(master, text = "Exit App", command = master.quit) 
		self.close_button.pack() 
		
		self.grades = Entry(master) 
		self.grades.pack() 
		self.outcome = Label(master, text = 0.0) 
		self.outcome.pack() 
	
		self.clear = Button(master, text = "Clear", command = self.clear)	
		self.clear.pack()
		self.count = 0.00	
		self.value = 0.00 
		self.a = 0.0 	
	def greet(self):
		info = self.grades.get() 	
		j = 0 
		for i in range(len(info)) :
			if (info[i] == '.') : 
				self.temp = info[i - 5] + info[i - 4] + info[i - 3]
				self.value = info[i - 1] + info[i] + info[i + 1] + info[i + 2] 
				self.value = float(self.value)

				if 90 <= int(self.temp) <= 100 :
					self.temp = 4.00
				elif 85 <= int(self.temp) <= 89 :
					self.temp = 3.90	
				elif 80 <= int(self.temp) <= 84 :
					self.temp = 3.70	
				elif 77 <= int(self.temp) <= 79 :
					self.temp = 3.30	
				elif 73 <= int(self.temp) <= 76 :
					self.temp = 3.00	
				elif 70 <= int(self.temp) <= 72 :
					self.temp = 2.70
				elif 67 <= int(self.temp) <= 69 :
					self.temp = 2.30		
		 		elif 63 <= int(self.temp) <= 66 :
					self.temp = 2.00	
				elif 60 <= int(self.temp) <= 62 :
					self.temp = 1.70	
				elif 57 <= int(self.temp) <= 59 :
					self.temp = 1.30
				elif 53 <= int(self.temp) <= 56 :
					self.temp = 1.00	
				elif 50 <= int(self.temp) <= 52 :
					self.temp = 0.70
				else:
					self.temp = 0.00	

				self.a += (float(self.temp) * float(self.value))
				self.count += self.value
		self.outcome.config(text = "Score is: " + str(self.a / self.count))
	
	def clear(self) :
		self.grades.delete(0, END)
		self.outcome.config(text = "")			
				
	
	
root = Tk() 
mcat = mcatGui(root) 
root.mainloop() 

