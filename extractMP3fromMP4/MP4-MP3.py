import moviepy
import moviepy.editor

def vid_aud(file_path, file_name):

    video=moviepy.editor.VideoFileClip(file_path)
    audio=video.audio
    audio.write_audiofile(f"{file_name}.mp3")

if __name__ == '__main__':
    filepath = input("Enter the video file path here :- \n")#put your file path here
    filename = input("Enter the audio file name here :- \n")#put your file name here

    vid_aud(filepath,filename)
