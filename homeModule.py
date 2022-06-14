#Module imports
    #bookingModule
import bookingModule as booking
import varModule as var
import roomInfoModule as room
import roomServiceModule as roomServe
import paymentModule as payment
import recordModule as record
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from datetime import datetime
import function as fun
def Home():
	#Intro section
	print("\t\t\t\t\t\t WELCOME TO HOTEL GARRISON\n")
	date_string = datetime.now().strftime("%d%m%Y%H%M%S")
	filename = "voice"+date_string
	fun.tts("Welcome to Garrison",filename+"welcome")
	# playsound("welcome.mp3")
	#INtro section end

	#how can we help
	print("\t\t\t 1 Booking\n")
	print("\t\t\t 2 Rooms Info\n")
	print("\t\t\t 3 Room Service(Menu Card)\n")
	print("\t\t\t 4 Payment\n")
	print("\t\t\t 5 Record\n")
	print("\t\t\t 0 Exit\n")

	date_string = datetime.now().strftime("%d%m%Y%H%M%S")
	filename = "voice"+date_string
	fun.tts("Please tell from above what you want to do",filename+"help")
	
	ch = str(fun.record()).lower()
	# ch=int(input("->"))
	
	if ch == "booking":

		print(" ")
		booking.Booking()
	
	elif ch == "roomsinfo" or "rooms info":
		print(" ")
		room.Rooms_Info()
	
	elif ch == "room service":
		print(" ")
		roomServe.restaurant()
	
	elif ch == "payment" or "payments":
		print(" ")
		payment.Payment()
	
	elif ch == "record" or "records":
		print(" ")
		record.Record()
	
	else:
		exit()
