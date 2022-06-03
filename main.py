import tkinter as tk 
from pytube import YouTube

# https://www.youtube.com/watch?v=d8Gq-koesFU

def res_360p():
    global res_video
    res_video = str("360p")

def res_720p():
    global res_video
    res_video = str("720p")

def res_1080p():
    global res_video
    res_video = str("1080p")    

def save_video():
    global myVideoStream
    vid = entry_link.get()
    path = entry_path.get()
    myVideoStream = YouTube(vid)
    yt = myVideoStream.streams.filter(file_extension = "mp4", resolution = res_video)
    yt.first().download(path)
   
    data_title ["text"] = str("Название: " + myVideoStream.title)
    data_lenght ["text"] = str("Продолжительность: " + str(myVideoStream.length)+" сек")
    data_views ["text"] = str("Количество просмотров: " + str(myVideoStream.views))


window = tk.Tk() 
window.title("Скачивание видео с YouTube")

window.columnconfigure([0, 0], minsize=50)
window.rowconfigure([0, 10], minsize=30)

label_link = tk.Label(text="введите ссылку на видео с YouTube") 
label_link.grid(row=0 , column=0) 

entry_link = tk.Entry(text="ссылка на видео", fg="black", bg="white", width=50) 
entry_link.grid(row=1, column=0) 
link = entry_link.get() 

label_path = tk.Label(text="укажите папку для сохранения видео") 
label_path.grid(row=2, column=0) 

entry_path = tk.Entry(text="место сохранения", fg="black", bg="white", width=50) 
entry_path.grid(row=3, column=0) 
path = entry_path.get() 

frame_res = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5) 
frame_res.grid(row=4, column=0, padx=5, pady=5)

label_res = tk.Label(master=frame_res, text= "Выберите разрешение видео") 
label_res.pack() 

button_360p = tk.Button(master=frame_res, text="360p", width=7, height=1,
bg="magenta3", fg="thistle1", command = res_360p) 
button_360p.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) 

button_720p = tk.Button(master=frame_res, text="720p", width=7, height=1,
bg="magenta3", fg="thistle1", command = res_720p) 
button_720p.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) 

button_1080p = tk.Button(master=frame_res, text="1080p", width=7, height=1,
bg="magenta3", fg="thistle1", command = res_1080p) 
button_1080p.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) 

label_data_video = tk.Label(text="Данные о видео") 
label_data_video.grid(row=5, column=0) 

info_data = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5) 
info_data.grid(row=6 , column=0, padx=5, pady=5) 

data_title = tk.Label(master=info_data, width=60, height=1, fg="black", bg="grey") 
data_title.grid(row=7, column=0) 

data_lenght = tk.Label(master=info_data, width=60, height=1, fg="black", bg="grey") 
data_lenght.grid(row=8, column=0) 

data_views = tk.Label(master=info_data, width=60, height=1, fg="black", bg="grey") 
data_views.grid(row=9, column=0) 

button_save = tk.Button(text="скачать видео", width=12, height=2,
bg="magenta3", fg="thistle1", command = save_video) 
button_save.grid(padx=5, pady=5) 

window.mainloop() 



