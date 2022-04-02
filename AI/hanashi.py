import pyttsx3   #pyttsx3 la ten thu vien

robot_brain = "Hello"

robot_kuchi = pyttsx3.init()   #init() : initialize khoi tao
robot_kuchi.say(robot_brain)     #say: ham de noi ra bien o ben trong
robot_kuchi.runAndWait()
