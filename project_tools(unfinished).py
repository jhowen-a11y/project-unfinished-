from tkinter import *


def pdf_converter():
    window.withdraw()
    pdf = Toplevel()
   

    
    pdf.title("PDF FILE CONVERTER")
    pdf_button = Button(pdf,text="choose a file to convert" )
    pdf_button.pack()
    pdf_button.config(font=('Ink Free', 50, 'bold'))
    pdf_button.config(bg=("grey"),fg=("pink"))
    
    

    window.mainloop()
def calculator():
    pass
def bg_remover():
    window.withdraw()
    bgmerover = Toplevel()

    bgmerover.title("BACKGROUND REMOVER")
    bgremover_button = Button(bgmerover, text="choose a file to convert" )
    bgremover_button.pack()
    bgremover_button.config(font=('Ink Free', 50, 'bold'))
    bgremover_button.config(fg=("black"),bg=("red"))

    window.mainloop()
def uncolorizers():

    pass
def text_counter():
    pass
window = Tk()
window.geometry("600x400")
window.title("Tools")

pdfconverter = Button(window, text="word to pdf", width= 10, height= 6)
bgremover = Button(window, text="background remover",width= 10, wraplength=150,  height= 6)
calc = Button(window, text = "Calculator",width= 10, wraplength=150,  height= 6 )
uncolor = Button(window,text = "uncolorizer",width= 10, wraplength=150,  height= 6)
counter = Button(window,text = "counter",width= 10, wraplength=150,  height= 6)

pdfconverter.config(font=('Ink Free', 14, 'bold'))
pdfconverter.config(bg=("green"))

calc.config(font=('Ink Free', 14, 'bold'))
calc.config(bg=("grey"),fg=("black"))

uncolor.config(font=('Ink Free', 14, 'bold'))
uncolor.config(bg=("grey"),fg=("black"))

counter.config(font=('Ink Free', 14, 'bold'))
counter.config(bg=("green"))

bgremover.config(font=('Ink Free', 14, 'bold'))
bgremover.config(bg="white")

pdfconverter.grid(row= 1, column= 1)
bgremover.grid(row= 1, column= 2)
calc.grid(row= 1, column= 3)
uncolor.grid(row=1, column=4)
counter.grid(row=1,column=5)

bgremover.config(command=bg_remover)
pdfconverter.config(command = pdf_converter)
calc.config(command=calculator)
uncolor.config(command=uncolorizers)

window.mainloop()