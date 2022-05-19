import speech_recognition as sr
from datetime import datetime
# Global List Declaration
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

# Global Variable Declaration
hear = sr.Recognizer()
lang = "en"
i = 0

date_string = datetime.now().strftime("%d%m%Y%H%M%S")
filename = "voice"+date_string

