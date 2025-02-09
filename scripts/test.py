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

def main_label():
    """Swedish class label for main frame"""
    label = Label(main_frame, text="Basic Swedish", font=("Work Sans", 50, "underline"), fg='black')
    underlabel = Label(main_frame, text="Learn by playing", font=("Work Sans", 30), fg='black')
    label.place(relx=0.5, rely=0.15, anchor="center")  
    underlabel.place(relx=0.5, rely=0.25, anchor="center")  

def start_label():
    """Select a game label for start frame"""
    label = Label(start_frame, text="Select a game", font=("Work Sans", 50), fg='black')
    label.place(relx=0.5, rely=0.15, anchor="center")  

def round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Round rectangle buttons."""
    points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1,
              x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2, 
              x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2, 
              x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

def create_rounded_button(canvas, x, y, width, height, text, command):
    """Create round button based on the round_rectangle() feature"""
    button = round_rectangle(canvas, x, y, x + width, y + height, radius=40, fill="white", outline="#800000", width=3)
    text_item = canvas.create_text((x + x+width) // 2, (y + y+height) // 2, text=text, font=("Work Sans", 15, 'bold'), fill="black")
    
    def on_hover(event):
        canvas.itemconfig(button, fill="#800000")  
        canvas.itemconfig(text_item, fill="white") 

    def off_hover(event):
        canvas.itemconfig(button, fill="white")  
        canvas.itemconfig(text_item, fill="black")  

    # Bind hover actions
    canvas.tag_bind(button, "<Enter>", on_hover)  
    canvas.tag_bind(button, "<Leave>", off_hover)  

    # Changes page when clicking on a button
    canvas.tag_bind(button, "<Button-1>", lambda event: command())
    
    return button, text_item

# SWITCH BETWEEN PAGES
def on_start_click():
    # Hide main menu and show start menu
    main_frame.pack_forget()
    start_frame.pack(fill="both", expand=True)

def go_back_click():
    start_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

def on_user_profile_click():
    print("WILL BE IMPLEMENTED")

def on_statistics_click():
    print("WILL BE IMPLEMENTED")

def on_accessibility_click():
    print("WILL BE IMPLEMENTED")

def on_clock_game_click():
    print("WILL BE IMPEMENTED")

def on_placeholder_click():
    print("WILL BE IMPLEMENTED")

def on_match_the_words_click():
    print("WILL BE IMPLEMENTED")

def main_menu_table():
    """Create the main menu."""
    menu_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(menu_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")  

    # Skapa rundade knappar med exakta positioner
    create_rounded_button(canvas, screen_width//2 - 150, screen_height//2 - 150, 300, 50, "Start", on_start_click)
    create_rounded_button(canvas, screen_width//2 - 150, screen_height//2 - 75, 300, 50, "User Profile", on_user_profile_click)
    create_rounded_button(canvas, screen_width//2 - 150, screen_height//2 - 0, 300, 50, "Statistics", on_statistics_click)
    create_rounded_button(canvas, screen_width//2 - 150, screen_height//2 + 75, 300, 50, "Accessibility", on_accessibility_click)


    return menu_frame

def start_menu_table():
    """Menu with horizontally arranged buttons."""
    start_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(start_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    #Start menu buttons
    create_rounded_button(canvas, (screen_width - 220)//2 - 250, screen_height//2 - 200, 220, 150, "Clock Game", on_clock_game_click)
    create_rounded_button(canvas, (screen_width - 220)//2, screen_height//2 - 200, 220, 150, "Placeholder", on_placeholder_click)
    create_rounded_button(canvas, (screen_width - 220)//2 + 250, screen_height//2 - 200, 220, 150, "Match the words", on_match_the_words_click)

    #Go back button
    create_rounded_button(canvas, screen_width - (screen_width-50), screen_height - (screen_height - 50), 100, 50, "Go back", go_back_click)

    return start_frame

# Create frames for different pages
main_frame = main_menu_table()  # The main menu is created first
start_frame = start_menu_table()  # The start menu is created but not packed

# Call the main label function to add labels to main_frame
main_label()

# Call the start label function to add labels to start_frame
start_label()

# Show the first frame (main menu)
main_frame.pack(fill="both", expand=True)

# Start the Tkinter main loop
root.mainloop()
