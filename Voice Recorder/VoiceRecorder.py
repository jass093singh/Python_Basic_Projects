import sounddevice
from scipy.io.wavfile import write

fs=44100 #sample rate
second=int(input("Enter the time duration in second: "))#enter your required time.....


print("Recording....")
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()
file_name = input("Please enter file name = ")
write(file_name+".wav", fs, record_voice)
print("Finished...\nPlease check it")
