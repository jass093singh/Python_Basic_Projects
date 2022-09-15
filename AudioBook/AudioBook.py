import pyttsx3
book = open(r"book.txt")#enter your file path
book_text=book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()