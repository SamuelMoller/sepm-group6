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

# Define the LARGEFONT variable used across pages
LARGEFONT = ("Work Sans", 50, "underline")

# Container frame to hold the pages
class tkinterApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Store frames
        self.frames = {}

        # Iterate through the page classes to create frames
        for F in (StartPage, UserProfilePage, StatisticsPage, AccessibilityPage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# Define pages (StartPage, UserProfilePage, etc.)

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Basic Swedish", font=LARGEFONT, fg='black')
        label.place(relx=0.5, rely=0.2, anchor="center")
        
        # Create menu buttons
        menu_frame = Frame(self, bg='#F0F0F0')
        menu_frame.pack()

        canvas = Canvas(menu_frame, width=400, height=300, bg='#F0F0F0', highlightthickness=0)
        canvas.pack()

        # Create round buttons with references to the click commands
        create_rounded_button(canvas, 50, 20, 300, 50, "Start", lambda: controller.show_frame("StartPage"))
        create_rounded_button(canvas, 50, 80, 300, 50, "User Profile", lambda: controller.show_frame("UserProfilePage"))
        create_rounded_button(canvas, 50, 140, 300, 50, "Statistics", lambda: controller.show_frame("StatisticsPage"))
        create_rounded_button(canvas, 50, 200, 300, 50, "Accessibility", lambda: controller.show_frame("AccessibilityPage"))


class UserProfilePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="User Profile", font=LARGEFONT, fg='black')
        label.place(relx=0.5, rely=0.2, anchor="center")
        
        back_button = Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        back_button.place(relx=0.5, rely=0.7, anchor="center")


class StatisticsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Statistics", font=LARGEFONT, fg='black')
        label.place(relx=0.5, rely=0.2, anchor="center")
        
        back_button = Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        back_button.place(relx=0.5, rely=0.7, anchor="center")


class AccessibilityPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Accessibility", font=LARGEFONT, fg='black')
        label.place(relx=0.5, rely=0.2, anchor="center")
        
        back_button = Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        back_button.place(relx=0.5, rely=0.7, anchor="center")


# Round button code (unchanged)
def round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
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

def create_rounded_button(canvas, x, y, width, height, text, command):
    button = round_rectangle(canvas, x, y, x + width, y + height, radius=40, fill="white", outline="#800000", width=3)
    text_item = canvas.create_text((x + x+width) // 2, (y + y+height) // 2, text=text, font=("Work Sans", 15, 'bold'), fill="black")
    
    def on_hover(event):
        canvas.itemconfig(button, fill="#800000")
        canvas.itemconfig(text_item, fill="white")

    def off_hover(event):
        canvas.itemconfig(button, fill="white")
        canvas.itemconfig(text_item, fill="black")

    canvas.tag_bind(button, "<Enter>", on_hover)
    canvas.tag_bind(button, "<Leave>", off_hover)

    canvas.tag_bind(button, "<Button-1>", lambda event: command())
    
    return button, text_item


# Initialize the main app
app = tkinterApp()
app.mainloop()
