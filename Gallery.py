from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

#mga images
images = []
current_index = 0
def load_folder():
    global images, current_index

    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    images.clear()

    for file in os.listdir(folder_path):
        if file.lower().endswith((".png",".jpg",".jpeg",".gif")):
            full_path = os.path.join(folder_path, file)
            images.append(full_path)

    current_index = 0
    openfile()
def openfile():
    #filepath = filedialog.askopenfilename()

    if not images:
        return
    img = Image.open(images[current_index])

    img.thumbnail((label_width,label_height))

    img_tk = ImageTk.PhotoImage(img)

    Gl.config(image=img_tk)

    Gl.image = img_tk
def next_image():
    global current_index

    if images:
        current_index += 1 

        if current_index >= len(images):
            current_index = 0
             
        openfile()      
def prev_image():
    global current_index

    if images:
        current_index -= 1 

        if current_index < 0:
            current_index = len(images) - 1
             
        openfile()
        
label_height = 700
label_width = 800
gallery = Tk()
#main window
gallery.title("Gallery")
gallery.geometry("900x700")
gallery.config(bg="grey")


#button for opening the file

buttonF = Button(gallery, text=("choose files"))
buttonF.pack()
buttonF.config(font=('Ink Free', 14, 'bold'), command=load_folder)
#next button
galerybtn = Button(gallery, text=(">"))
galerybtn.pack(side="right", pady= 10, padx= 10)
galerybtn.config(font=('Ink Free', 14, 'bold'), command=next_image)

#previous button
gallerybtn2 = Button(gallery, text=("<"))
gallerybtn2.pack(side="left", pady= 10, padx= 10)
gallerybtn2.config(font=('Ink Free', 14, 'bold'),command=prev_image)

#image lalagyan
Gl = Label(gallery, bg= "black")
Gl.place(x=50, y=80,width=label_width, height=label_height)


gallery.mainloop()