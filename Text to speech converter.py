import gtts as g
import playsound as ps

text = input("Enter something here : ")
sound = g.gTTS(text , lang = "hi")
sound.save("welcome.mp3")
ps.playsound("welcome.mp3")


