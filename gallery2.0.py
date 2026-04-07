from customtkinter import *
from PIL import Image

class main_window():
    def __init__(self):
        
        self.main = CTk()
        
        self.image1 = CTkImage(Image.open("project.py\menu.png"), size= (30,30))
        self.image2 = CTkImage(Image.open(r"project.py\folder.png"), size=(30,30))
        self.image3 = CTkImage(Image.open("project.py\home.png"),size=(30,30))
        self.image4 = CTkImage(Image.open("project.py\exit.png"),size=(30,30))
        self.main.title("GALLERY2.0")
        self.main.geometry("850x450+200+150")
        self.main_frame = CTkFrame(self.main, width= 850, height= 450, fg_color= "#4F3C38",corner_radius=0)
        self.main_frame.place(x=0,y=0)

        self.menubar = CTkFrame(self.main_frame, width= 40, height=450, fg_color= "#292322",corner_radius=0)
        self.menubar.place(x=0,y=0)
        

        self.menu = CTkButton(self.menubar, width=40,height=35,image=self.image1, fg_color= "#292322", corner_radius=0, hover_color= "grey",text="")
        self.menu.place(x=0,y=0)

        self.home = CTkButton(self.menubar, width=40,height=35,image=self.image3, fg_color= "#292322", corner_radius=0, hover_color= "grey",text="")
        self.home.place(x=0,y=40)

        self.folder1 = CTkButton(self.menubar, width=40,height=35,image=self.image2, fg_color= "#292322", corner_radius=0, hover_color= "grey",text="")
        self.folder1.place(x=0,y=80)

        self.exit = CTkButton(self.menubar, width=40,height=35,image=self.image4, fg_color= "#292322", corner_radius=0, hover_color= "grey",text="", command=self.close)
        self.exit.place(x=0,y=413)

        self.main.mainloop()
    def close(self):
        self.main.destroy()
    
        
        

gallery = main_window()