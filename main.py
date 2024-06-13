import tkinter
import customtkinter
from pytube import YouTube

def startdownload():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink,on_progress_callback= on_progress)
        video = ytobject.streams.get_highest_resolution()
        title.configure(text = ytobject.title, text_color = "white")
        finishlabel.configure(text = "")
        video.download()
        finishlabel.configure(text = "Downloaded")
        
    except:
        finishlabel.configure(text = "Download Error",text_color = "red")

def on_progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    bytes_downloaded = size - bytes_remaining
    percentage_completion = bytes_downloaded / size *100
    per = str(int(percentage_completion))
    percentage.configure(text = per + "%")
    percentage.update()

    #update progress bar
    bar.set(float(percentage_completion) / 100)

#System settings
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloader")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text = "Insert a youtube link")
title.pack(padx=10, pady=10)

#Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40,textvariable=url_var)
link.pack()

#Finished Downloading
finishlabel = customtkinter.CTkLabel(app, text = "")
finishlabel.pack()

#Progress percentage
percentage = customtkinter.CTkLabel(app, text = "0%")
percentage.pack()

bar = customtkinter.CTkProgressBar(app, width = 400)
bar.set(0)
bar.pack(padx=10,pady=10)

#Download button
download = customtkinter.CTkButton(app, text = "Download", command = startdownload, hover_color="darkblue")
download.pack(padx=10,pady=10)


#Run app
app.mainloop()