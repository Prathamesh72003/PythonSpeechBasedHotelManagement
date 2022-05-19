from cgi import print_arguments
import datetime
import random
import time

import gtts
from recordModule import Record
import varModule as var
import DateModule as datem
import homeModule as home
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import function as fun

#globals
"""this module will conatin the bookings section"""

# Booking function
def Booking():
		fun.tts("Lets book a room for you",var.filename+"booking")
		# used global keyword to
		# use global variable 'i'
		global i
		print(" BOOKING ROOMS")
		print(" ")
		
		while 1:
			fun.tts("What is your name", var.filename+"wname")
			n = fun.record()
			print("name: "+n)
			# n = str(input("Name: "))

			fun.tts("Hello"+n+"Please tell your phone number",  var.filename+"wphone")
			p1 = str(fun.record())
			print("Phone No: "+p1.replace(" ", ""))
			# p1 = str(input("Phone No.: "))

			fun.tts("Please provide your address",  var.filename+"waddr")
			a = str(fun.record())
			print("Address: "+a)
			# a = str(input("Address: "))
			
			# checks if any field is not empty
			if n!="" and p1!="" and a!="":
				var.name.append(n)
				var.add.append(a)
				break
				
			else:
				print("\tName, Phone no. & Address cannot be empty..!!")
		
		#date section
		fun.tts("Please provide your check-in date",  var.filename+"wcheckIn")
		# ciidate = str(fun.record())
		# ciimonth = str(fun.record())
		# ciiyear = str(fun.record())
		# print("check-in: "+str(ciidate+"/"+ciimonth+"/"+ciiyear))
		# cii=str(ciidate+"/"+ciimonth+"/"+ciiyear)
		cii = str(input('check-in: '))
		var.checkin.append(cii)
		cii=cii.split('/')
		ci=cii
		ci[0]=int(ci[0])
		ci[1]=int(ci[1])
		ci[2]=int(ci[2])
        #to be changes later
		datem.date(ci)
		fun.tts("Please provide your check-out date",  var.filename+"wcheckOut")
		# coodate = str(fun.record())
		# coomonth = str(fun.record())
		# cooyear = str(fun.record())
		# print("check-out: "+str(coodate+"/"+coomonth+"/"+cooyear))
		# coo=str(coodate+"/"+coomonth+"/"+cooyear)
		coo = str(input("check-out: "))
		var.checkout.append(coo)
		coo=coo.split('/')
		co=coo
		co[0]=int(co[0])
		co[1]=int(co[1])
		co[2]=int(co[2])
		
		# checks if check-out date falls after
		# check-in date
		if co[1]<ci[1] and co[2]<ci[2]:
			
			print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
			var.name.pop(i)
			var.add.pop(i)
			var.checkin.pop(i)
			var.checkout.pop(i)
			Booking()
		elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
			
			print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
			var.name.pop(i)
			var.add.pop(i)
			var.checkin.pop(i)
			var.checkout.pop(i)
			Booking()
		else:
			pass
		#to be changed later
		datem.date(co)
		d1 = datetime.datetime(ci[2],ci[1],ci[0])
		d2 = datetime.datetime(co[2],co[1],co[0])
		d = (d2-d1).days
		var.day.append(d)
		
		
		fun.tts("Selet room type",  var.filename+"roomType")
		print("----SELECT ROOM TYPE----")
		print(" 1. Standard Non-AC")
		print(" 2. Standard AC")
		print(" 3. Double bed Non-AC")
		print(" 4. Double bed AC")
		#print(("\t\tPress 0 for Room Prices"))
		fun.tts("Say Details to check out the Prices", var.filename+"detail")
		ch = str(fun.record()).lower().replace(" ", "")
		#ch=int(input("->"))
		
		# if-conditions to display alloted room
		# type and it's price
		if ch=="details" or ch=="detail":
			fun.tts("Here are the room Details",  var.filename+"roomDetail")
			print(" 1. Standard Non-AC - Rs. 3500")
			print(" 2. Standard AC - Rs. 4000")
			print(" 3. Double Bed Non-AC - Rs. 4500")
			print(" 4. Double bed AC - Rs. 5000")
			time.sleep(5)
			fun.tts("Selet room type",  var.filename+"roomType1")
			ch = str(fun.record()).lower().replace(" ", "")
			#ch=int(input("->"))
		if ch== "standardnonac":
			var.room.append('Standard Non-AC')
			print("Room Type- Standard Non-AC")
			var.price.append(3500)
			print("Price- 3500")
		elif ch=="standarac":
			var.room.append('Standard AC')
			print("Room Type- Standard AC")
			var.price.append(4000)
			print("Price- 4000")
		elif ch== "doublebednonac":
			var.room.append('Double bed Non-AC')
			print("Room Type- Double bed Non-AC")
			var.price.append(4500)
			print("Price- 4500")
		elif ch== "doublebedac":
			var.room.append('Double bed AC')
			print("Room Type- Double bed AC")
			var.price.append(5000)
			print("Price- 5000")
		else:
			print(" Wrong choice..!!")


		# randomly generating room no. and customer
		# id for customer
		rn = random.randrange(40)+300
		cid = random.randrange(40)+10
		
		
		# checks if alloted room no. & customer
		# id already not alloted
		while rn in var.roomno or cid in var.custid:
			rn = random.randrange(60)+300
			cid = random.randrange(60)+10
			
		var.rc.append(0)
		var.p.append(0)
			
		if p1 not in var.phno:
			var.phno.append(p1)
		elif p1 in var.phno:
			for n in range(0,i):
				if p1== var.phno[n]:
					if var.p[n]==1:
						var.phno.append(p1)
		elif p1 in var.phno:
			for n in range(0,i):
				if p1== var.phno[n]:
					if var.p[n]==0:
						print("\tPhone no. already exists and payment yet not done..!!")
						var.name.pop(i)
						var.add.pop(i)
						var.checkin.pop(i)
						var.checkout.pop(i)
						Booking()
		print("")
		fun.tts("Congratulation, your room was booked",  var.filename+"roomBookCongrats")
		print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
		roomno = str(rn)
		fun.tts("Your room number is "+roomno,  var.filename+"RoomNo")
		print("Room No. - ",rn)
		custid = str(cid)
		fun.tts("Your customer ID is "+custid,  var.filename+"custId")
		print("Customer Id - ",cid)
		var.roomno.append(rn)
		var.custid.append(cid)
		var.i=var.i+1

		fun.tts("Say menu to go back to main menu",var.filename+"backtomenu")
		print("Say menu to go back to main menu")
		# n = int(input("0-BACK\n ->"))
		n = str(fun.record()).lower()
		if n == "menu":
			home.Home()
		else:
            #to be changes later
			var.exit()
