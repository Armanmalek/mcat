import tkinter as tk
import tkinter.messagebox as box	
from datetime import *
import csv  

#Get datetime info for csv
today = datetime.today() 
date = today.strftime('%c') 

#initialize GUI
window = tk.Tk()  
window.title('Enterprise Gas Log') 
img = tk.PhotoImage(file = 'ent.png') 
employeeEntry = tk.StringVar()
employee = tk.StringVar() 
gasPaid  =tk.DoubleVar()
carInfo = tk.StringVar() 
gasEntry = tk.Entry(window) 
carEntry= tk.Entry(window)

#Function for input verification
def win():
	var = box.askquestion('Confirmation', employeeEntry.get() + ' ' + 'did you pay' + ' ' + gasEntry.get() + '$' + ' ' +  'for' + ' ' + "'" +  carEntry.get() + "'" + '?') 
	#if user is satisfied save if not delete 
	if var == ('yes'):  
		gasPaid = gasEntry.get() 
		carInfo = carEntry.get() 
		employee = employeeEntry.get()

		with open('gaslog.csv', 'a') as gasLog: 

			gasLogWriter = csv.writer(gasLog) 
			gasLogWriter.writerow([date, employee, gasPaid, carInfo]) 
		gasEntry.delete(0, 'end') 
		carEntry.delete(0, 'end') 
		
	elif var == 'no' : 
		gasEntry.delete(0, 'end') 
		carEntry.delete(0, 'end') 


	


#GUI geometry 
whoWent = tk.Label(window, text =  'Who Went?', bg = 'green')
howMuch = tk.Label(window, text = 'Price Paid? ($)') 
description = tk.Label(window, text = 'Car Description') 
label = tk.Label(window, image = img, bg = 'black') 
#abel = label.resize(200,200) 
ali = tk.Radiobutton(window, text = 'Ali', variable = employeeEntry, value = 'Ali')
anthony = tk.Radiobutton(window, text = 'Anthony', variable = employeeEntry, value = 'Anthony') 
arman = tk.Radiobutton(window, text = 'Arman', variable = employeeEntry, value = 'Arman')
candice = tk.Radiobutton(window, text = 'Candice', variable = employeeEntry, value = 'Candice')
chelson = tk.Radiobutton(window, text = 'Chelson', variable = employeeEntry, value = 'Chelson')
dan = tk.Radiobutton(window, text = 'Dan', variable = employeeEntry, value = 'Dan')
dave = tk.Radiobutton(window, text = 'Dave', variable = employeeEntry, value = 'Dave')
derrick = tk.Radiobutton(window, text = 'Derrick', variable = employeeEntry, value = 'Derrick')
sal = tk.Radiobutton(window, text = 'Sal', variable = employeeEntry, value = 'Sal')
tony = tk.Radiobutton(window, text = 'Tony', variable = employeeEntry, value = 'Tony')
btn  = tk.Button(window, text = 'Enter', bg = 'green', command = win)
exit  = tk.Button(window, text = 'Exit', bg = 'green', command = exit)

label.place(x = 550, y = 4) 
ali.place (x = 305, y = 30)
anthony.place(x = 350, y = 30)
arman.place(x  = 430, y = 30) 
dan.place(x = 500, y = 30)
dave.place(x = 305, y = 50)
derrick.place(x = 365, y = 50) 
sal.place(x = 440, y = 50)
tony.place(x = 500, y = 50)
candice.place(x = 305, y = 70)
chelson.place(x = 400, y = 70)
howMuch.place(x = 300, y = 100) 
description.place(x = 400, y = 100) 
gasEntry.place(x = 300, y = 120)
carEntry.place(x = 400 , y = 120)
whoWent.place(x = 300, y = 4, width = 300)
btn.place(x = 325, y = 140) 
exit.place(x = 450, y = 140)

window.mainloop() 
