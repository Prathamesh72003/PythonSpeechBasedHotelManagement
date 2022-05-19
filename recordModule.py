
import varModule as var
import homeModule as home
import function as fun
from datetime import datetime

# RECORD FUNCTION
def Record():
	
	# checks if any record exists or not
	if var.phno!=[]:
		date_string = datetime.now().strftime("%d%m%Y%H%M%S")
		filename = "voice"+date_string
		fun.tts("Here are the records of all customers",filename+"records")
		print("	 *** HOTEL RECORD ***\n")
		print("| Id \t | Name | Phone No. | Address	 | Check-In | Check-Out	 | Room Type	 | Price	 |")
		print("----------------------------------------------------------------------------------------------------------------------")
		
		for n in range(0,var.i):
			print("|",var.custid[n],"\t|",var.name[n],"\t |",var.phno[n],"\t|",var.add[n],"\t|",var.checkin[n],"\t|",var.checkout[n],"\t|",var.room[n],"\t|",var.price[n])
		
		print("----------------------------------------------------------------------------------------------------------------------")
	
	else:
		date_string = datetime.now().strftime("%d%m%Y%H%M%S")
		filename = "voice"+date_string
		fun.tts("No records found in the book",filename+"norecords")
		print("No Records Found")
	
	date_string = datetime.now().strftime("%d%m%Y%H%M%S")
	filename = "voice"+date_string
	fun.tts("Say menu to go back to main menu",filename+"backtomenu")
	print("Say menu to go back to main menu")
	# n = int(input("0-BACK\n ->"))
	n = str(fun.record()).lower()
	if n == "menu":
		home.Home()
	else:
		exit()