import speech_recognition  #speech_recognition: la ten thu vien nhan dang giong noi

robot_mimi =speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:     #nghe xong se tu tat mic
	print("Robot: I'm Listening...")
	audio = robot_mimi.listen(mic)            # dung mic nghe am thanh roi gan vao bien audio
 
you = robot_mimi.recognize_google(audio)

print(you)
