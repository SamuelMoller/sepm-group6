from tkinter import *
from tkinter import PhotoImage

# Main window
root = Tk()
root.title("Basic Swedish")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# UU icon for window
root.wm_iconbitmap('images/UU_logo.ico')

# Window size
root.geometry(f"{screen_width}x{screen_height}")
root.configure(background='#F0F0F0')

# Swedish class label
label = Label(root, text="Basic Swedish", font=("Work Sans", 50, "underline"), fg='black')
underlabel = Label(root, text="Learn by playing", font=("Work Sans", 30), fg='black')
label.place(relx=0.5, rely=0.15, anchor="center")  
underlabel.place(relx=0.5, rely=0.25, anchor="center")  

def round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Round triangle buttons. Inspiration from https://stackoverflow.com/a/44100075/15993687"""
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

def create_rounded_button(canvas, x, y, width, height, text):
    """CREATE ROUND BUTTON"""
    button = round_rectangle(canvas, x, y, x + width, y + height, radius=40, fill="white", outline="#800000", width=3)
    text_item = canvas.create_text((x + x+width) // 2, (y + y+height) // 2, text=text, font=("Work Sans", 15, 'bold'), fill="black")
    return button, text_item

def menu_table():
    """"
    Inspo taken from: 
    https://www.geeksforgeeks.org/python-tkinter-frame-widget/ 
    https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
    https://www.tutorialspoint.com/python/tk_button.htm
    https://www.geeksforgeeks.org/python-creating-a-button-in-tkinter/
    https://www.geeksforgeeks.org/how-do-you-create-a-button-on-a-tkinter-canvas/
    
    ROUND BUTTON INSPO: https://stackoverflow.com/questions/42579927/how-to-make-a-rounded-button-tkinter
    https://www.youtube.com/watch?v=czaqpo_yZwk
    """
    menu_frame = Frame(root, bg='#F0F0F0')
    menu_frame.pack()

    canvas = Canvas(menu_frame, width=400, height=300, bg='#F0F0F0', highlightthickness=0)
    canvas.pack()

    #Create our round buttons
    create_rounded_button(canvas, 50, 20, 300, 50, "Start")
    create_rounded_button(canvas, 50, 80, 300, 50, "User Profile")
    create_rounded_button(canvas, 50, 140, 300, 50, "Statistics")
    create_rounded_button(canvas, 50, 200, 300, 50, "Accessibility")

    return menu_frame

# Lägg till meny i mitten av fönstret
table = menu_table().place(relx=0.5, rely=0.5, anchor="center")

# Uppsala University logo
image = PhotoImage(file="images/uupsala-400-height-1.png")

# Skala ner bilden
width = int(image.width() * 0.5)
height = int(image.height() * 0.5)
image = image.subsample(int(image.width() / width), int(image.height() / height))

#Add image to window - CHANGE WHEN TEACHER PROVIDES A BETTER ONE
image_label = Label(root, image=image)
image_label.place(relx=1, rely=1, anchor="se")

root.mainloop()
