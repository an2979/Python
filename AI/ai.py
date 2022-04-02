import speech_recognition  #speech_recognition: la ten thu vien nhan dang giong noi
import pyttsx3   #pyttsx3 la ten thu vien
from datetime import date, datetime

robot_mimi =speech_recognition.Recognizer()
robot_kuchi = pyttsx3.init()   #init() : initialize khoi tao mieng cho robot
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic:     #nghe xong se tu tat mic
		print("Robot: I'm Listening...")
		audio = robot_mimi.listen(mic)            # dung mic nghe am thanh roi gan vao bien audio

	print("Robot:...")
	 
	try:
	    you = robot_mimi.recognize_google(audio)

	except:
		you =""

	print("You: "+you)

	# bo nao cua may tinh la phan duoi nay; cung la phan quan trong nhat...

	if you =="":
		robot_brain = "i can't hear you, try again"
	elif "hello" in you:
		robot_brain = "Hello AnTaRo"
	elif "today" in you:
		today =date.today()
	    robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
	    robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
	    robot_brain = "Bye AnTaRo" 
	    print("Robot:" +robot_brain)
	    robot_kuchi.say(robot_brain)     #say: ham de noi ra bien o ben trong
	    robot_kuchi.runAndWait()
	    break  
	else:
		robot_brain = "I'm fine thank you"

	print("Robot:" +robot_brain)
	robot_kuchi.say(robot_brain)     #say: ham de noi ra bien o ben trong
	robot_kuchi.runAndWait()
