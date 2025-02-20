from tkinter import *
# from tkinter.font import Font
import pyglet
from os.path import join, dirname, normpath

from sys import path as syspath
syspath.append(normpath(join(dirname(__file__), '../')))
# from backend import user


# File paths
root = dirname(__file__)
fonts_dir = normpath(join(root, '..', 'fonts'))
images_dir = normpath(join(root, '..', 'images'))

# Font
my_font = pyglet.font.add_file(join(fonts_dir, 'Work_Sans', 'WorkSans-Italic-VariableFont_wght.ttf'))
font_size = int(15)

# Main window
root = Tk()
root.title("Basic Swedish")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# UU icon for window
# root.wm_iconbitmap('images/UU_logo.ico')  # DEBUG: Linux compatibility

# Window size
root.geometry(f"{screen_width}x{screen_height}")
root.configure(background='#F0F0F0')


def login_label():
    """Title on login page"""
    label = Label(login_frame[0], text="Basic Swedish", font=(my_font, 50, "underline"), fg='black')
    underlabel = Label(login_frame[0], text="Learn by playing", font=(my_font, 30), fg='black')
    label.place(relx=0.5, rely=0.15, anchor="center")
    underlabel.place(relx=0.5, rely=0.25, anchor="center")


def statistics_label():
    """Title on statistics page"""
    label = Label(statistics_frame[0], text="Statistics", font=(my_font, 50), fg='black')
    underlabel = Label(statistics_frame[0], text="Latest game session", font=(my_font, 30), fg='black')
    label.place(relx=0.5, rely=0.15, anchor="center")
    underlabel.place(relx=0.5, rely=0.25, anchor="center")


def main_label():
    """Title on main page"""
    label = Label(main_frame[0], text="Basic Swedish", font=(my_font, 50, "underline"), fg='black')
    underlabel = Label(main_frame[0], text="Learn by playing", font=(my_font, 30), fg='black')
    label.place(relx=0.5, rely=0.15, anchor="center")
    underlabel.place(relx=0.5, rely=0.25, anchor="center")


def start_label():
    """Title on start page"""
    label = Label(start_frame[0], text="Select a game", font=(my_font, 50), fg='black')
    label.place(relx=0.5, rely=0.25, anchor="center")


def profile_label():
    """Title on start page"""
    label = Label(profile_frame[0], text="Current user", font=(my_font, 40), fg='black')
    label.place(relx=0.5, rely=0.10, anchor="center")


def round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Round triangle buttons. This construction was taken from https://stackoverflow.com/a/44100075/15993687"""
    points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1,
              x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2,
              x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2,
              x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)


def create_rounded_button(canvas, x, y, width, height, text, command, font):
    """Create round button based on the round_rectangle() feature"""
    button = round_rectangle(canvas, x, y, x + width, y + height, radius=40, fill="white", outline="#800000", width=6)
    text_item = canvas.create_text((x + x+width) // 2, (y + y+height) // 2, text=text, font=font, fill="black")

    def on_hover(mouse):
        canvas.itemconfig(button, fill="#800000")
        canvas.itemconfig(text_item, fill="white")

    def off_hover(mouse):
        canvas.itemconfig(button, fill="white")
        canvas.itemconfig(text_item, fill="black")

    canvas.tag_bind(button, "<Enter>", on_hover)
    canvas.tag_bind(text_item, "<Enter>", on_hover)
    canvas.tag_bind(button, "<Leave>", off_hover)

    # Changes page when clicking on a button (+ text in the button)
    canvas.tag_bind(button, "<Button-1>", lambda event: command())  # Command() indicate the selected page function
    canvas.tag_bind(text_item, "<Button-1>", lambda event: command())

    return button, text_item


def update_font_size(val: int):
    for _canvas in [main_frame[1], start_frame[1],
                    profile_frame[1], login_frame[1],
                    statistics_frame[1], accessibility_frame[1]]:
        for item in _canvas.find_all():
            if _canvas.type(item) == 'text':
                obj = _canvas.itemcget(item, 'font').split()
                if len(obj) == 3:
                    _canvas.itemconfig(item, font=(obj[0], val, obj[2]))
                elif len(obj) == 2:
                    _canvas.itemconfig(item, font=(obj[0], val))
                else:
                    _canvas.itemconfig(item, font=(obj[0], val))


# SWITCH BETWEEN PAGES
def on_start_click():
    """Switches to start page"""
    main_frame[0].pack_forget()
    start_frame[0].pack(fill="both", expand=True)


def go_main_page_click():
    """Switches to main page"""
    start_frame[0].pack_forget()
    profile_frame[0].pack_forget()
    statistics_frame[0].pack_forget()
    accessibility_frame[0].pack_forget()
    main_frame[0].pack(fill="both", expand=True)


def on_user_profile_click():
    main_frame[0].pack_forget()
    profile_frame[0].pack(fill="both", expand=True)


def on_statistics_click():
    main_frame[0].pack_forget()
    start_frame[0].pack_forget()
    profile_frame[0].pack_forget()
    statistics_frame[0].pack(fill="both", expand=True)


def on_accessibility_click():
    main_frame[0].pack_forget()
    start_frame[0].pack_forget()
    profile_frame[0].pack_forget()
    accessibility_frame[0].pack(fill="both", expand=True)


def on_clock_game_click():
    print("WILL BE IMPLEMENTED")


def on_placeholder_click():
    print("WILL BE IMPLEMENTED")


def on_match_the_words_click():
    print("WILL BE IMPLEMENTED")


def on_admin_control_click():
    print("WILL BE IMPLEMENTED")


def on_login_click():
    # CHANGE TO ACTUAL USER INPUT LATER
    login_frame[0].pack_forget()
    main_frame[0].pack(fill="both", expand=True)


def on_register_click():
    print("WILL BE IMPLEMENTED")


def on_log_out_click():
    main_frame[0].pack_forget()
    login_frame[0].pack(fill="both", expand=True)


def log_in_session() -> tuple[Frame, Canvas]:
    """Create main menu"""
    login_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(login_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Round buttons with exact positions
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 200, 600, 200, "Login to session", on_login_click, (my_font, 15))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 50, 600, 200, "Create a new user", on_register_click, (my_font, 15))

    return (login_frame, canvas)


def main_menu_table() -> tuple[Frame, Canvas]:
    """Create main menu"""
    menu_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(menu_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Round buttons with exact positions
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 200, 600, 75, "Start", on_start_click, (my_font, 15))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 100, 600, 75, "User Profile", on_user_profile_click, (my_font, 15))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 0, 600, 75, "Statistics", on_statistics_click, (my_font, 15))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 100, 600, 75, "Accessibility", on_accessibility_click, (my_font, 15))

    create_rounded_button(canvas, screen_width - 160, screen_height - (screen_height - 60), 100, 50, "Log out", on_log_out_click, (my_font, 10))

    return (menu_frame, canvas)


def start_menu_table() -> tuple[Frame, Canvas]:
    """Create start menu"""
    start_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(start_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    # Start menu buttons
    create_rounded_button(canvas, (screen_width - 250)//2 - 300, screen_height//2 - 200, 250, 250, "Clock Game", on_clock_game_click, (my_font, 15))
    create_rounded_button(canvas, (screen_width - 250)//2, screen_height//2 - 200, 250, 250, "Placeholder", on_placeholder_click, (my_font, 15))
    create_rounded_button(canvas, (screen_width - 250)//2 + 300, screen_height//2 - 200, 250, 250, "Match the words", on_match_the_words_click, (my_font, 15))

    # Go back button
    create_rounded_button(canvas, screen_width - (screen_width-60), screen_height - (screen_height - 60), 100, 50, "Go back", go_main_page_click, (my_font, 10))

    return (start_frame, canvas)


def profile_menu_table() -> tuple[Frame, Canvas]:
    """Profile page"""
    profile_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(profile_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Rectangle for user info
    round_rectangle(canvas, (screen_width - 500) // 2 - 200, (screen_height // 2) - 350, (screen_width - 500) // 2 + 700, (screen_height // 2) - 50, 20, fill="white", outline="darkred", width=4)

    # Add user icon - this can be replaced by the actual user image later
    user_icon_img = PhotoImage(file=join(images_dir, 'profile_logo.png'))
    # Resize image
    width = int(user_icon_img.width() * 0.4)
    height = int(user_icon_img.height() * 0.4)
    user_icon_img = user_icon_img.subsample(int(user_icon_img.width() / width), int(user_icon_img.height() / height))
    profile_frame.user_icon_img = user_icon_img
    canvas.create_image((screen_width - 600) // 2 - 25, (screen_height // 2) - 205, image=user_icon_img, anchor="center")

    # User information
    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 300,
                       text="Name: Your name", font=(my_font, 16, "bold"), anchor="w", fill="black")
    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 250,
                       text="Age: 25", font=(my_font, 16, "bold"), anchor="w", fill="black")
    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 200,
                       text="Country: Sweden", font=(my_font, 16, "bold"), anchor="w", fill="black")
    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 140,
                       text="Type of User: Exchange Student", font=(my_font, 16, "bold"), anchor="w", fill="black")

    # Statistics and admin button
    create_rounded_button(canvas, (screen_width - 500) // 2 - 200, screen_height // 2, 900, 75, "My Statistics", on_statistics_click, (my_font, 15))
    create_rounded_button(canvas, (screen_width - 500) // 2 - 200, screen_height // 2 + 100, 900, 75, "Admin Controls", on_admin_control_click, (my_font, 15))

    # Go back button
    create_rounded_button(canvas, screen_width - (screen_width-100), screen_height - (screen_height - 100), 100, 50, "Go back", go_main_page_click, (my_font, 10))

    return (profile_frame, canvas)


def statistics_menu_table() -> tuple[Frame, Canvas]:
    """Create statistics page"""
    statistics_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(statistics_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    # Statistics for first game
    round_rectangle(canvas, (screen_width - 1000) // 2, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 300, (screen_height - 500) // 2 + 250, 20, fill="white", outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 - 50, text="Time played:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 + 50, text="Correct answers:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 + 150, text="Clock game", font=(my_font, 14, "bold"), anchor="center", fill="black")

    # Statistics for second game
    round_rectangle(canvas, (screen_width - 1000) // 2 + 350, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 650, (screen_height - 500) // 2 + 250, 20, fill="white", outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 - 50, text="Time played:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 + 50, text="Matched items:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 + 150, text="Furniture game", font=(my_font, 14, "bold"), anchor="center", fill="black")

    # Statistics for third game
    round_rectangle(canvas, (screen_width - 1000) // 2 + 700, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 1000, (screen_height - 500) // 2 + 250, 20, fill="white", outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 - 50, text="Time played:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 + 50, text="Puzzle solved:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 + 150, text="Puzzle game", font=(my_font, 14, "bold"), anchor="center", fill="black")

    # General statistics
    round_rectangle(canvas, (screen_width - 1000) // 2, (screen_height - 500) // 2 + 370, (screen_width - 1000) // 2 + 1000, (screen_height - 500) // 2 + 620, 20, fill="white", outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 420, text="Lifetime statistics:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 470, text="Total time spent learning:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 520, text="Words learned:", font=(my_font, 16, "bold"), anchor="center", fill="black")

    # Go back button
    create_rounded_button(canvas, screen_width - (screen_width - 60), screen_height - (screen_height - 60), 100, 50, "Go back", go_main_page_click, (my_font, 10))

    return (statistics_frame, canvas)


def accessibility_menu_table() -> tuple[Frame, Canvas]:
    """Accessibility page"""
    accessibility_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(accessibility_frame,
                    width=screen_width, height=screen_height,
                    bg='#F0F0F0', highlightthickness=0)
    canvas.place(relx=0.5,
                 rely=0.5,
                 anchor="center")

    # Settings
    center = {'x': screen_width // 2,
              'y': screen_height // 2}

    # Change language
    # - List of languages
    # - Button functionality
    round_rectangle(canvas,
                    center['x'] - 700, center['y'] - 350,
                    center['x'] + 700, center['y'] - 50,
                    20, fill="white", outline="darkred", width=4)
    canvas.create_text(center['x'], center['y'] - 300,
                       text="Change Language", font=(my_font, int(font_size * 1.6), "bold"),
                       anchor="center", fill="black")
    create_rounded_button(canvas,
                          center['x'] - 350, center['y'] - 250,
                          width=330, height=75,
                          text="Swedish", command="",
                          font=(my_font, font_size))
    create_rounded_button(canvas,
                          center['x'] + 20, center['y'] - 250,
                          width=330, height=75,
                          text="Danish", command="",
                          font=(my_font, font_size))
    create_rounded_button(canvas,
                          center['x'] - 350, center['y'] - 150,
                          width=330, height=75,
                          text="English", command="",
                          font=(my_font, font_size))
    create_rounded_button(canvas,
                          center['x'] + 20, center['y'] - 150,
                          width=330, height=75,
                          text="Norwegian", command="",
                          font=(my_font, font_size))

    # Resize font
    round_rectangle(canvas,
                    center['x'] - 700, center['y'] + 50,
                    center['x'] - 50, center['y'] + 350,
                    20, fill="white", outline="darkred", width=4)
    canvas.create_text(center['x'] - 380, center['y'] + 100,
                       text="Resize Font", font=(my_font, int(font_size * 1.6), "bold"),
                       anchor="center", fill="black")
    font_size_slider = Scale(canvas,
                             from_=12, to=42,
                             orient=HORIZONTAL,
                             width=35,
                             length=450, label="",
                             font=(my_font, 24, "bold"),
                             background='white',
                             highlightbackground='white',
                             troughcolor='#F0F0F0',
                             command=lambda val: update_font_size(val))
    font_size_slider.set(font_size)
    font_size_slider.place(x=center['x'] - 600,
                           y=center['y'] + 150)

    # Contrast
    # - Slider
    round_rectangle(canvas,
                    center['x'] + 50, center['y'] + 50,
                    center['x'] + 700, center['y'] + 350,
                    20, fill="white", outline="darkred", width=4)
    canvas.create_text(center['x'] + 380, center['y'] + 100,
                       text="Contrast", font=(my_font, int(font_size * 1.6), "bold"),
                       anchor="center", fill="black")
    contrast_slider = Scale(canvas,
                            from_=0, to=100,
                            orient=HORIZONTAL,
                            width=35,
                            length=450, label="",
                            font=(my_font, int(font_size * 1.6), "bold"),
                            background='white',
                            highlightbackground='white',
                            troughcolor='#F0F0F0',
                            command=lambda val: print('contrast:', val))
    contrast_slider.set(50)
    contrast_slider.place(x=center['x'] + 150,
                          y=center['y'] + 150)

    # Backwards navigation
    create_rounded_button(canvas,
                          screen_width - (screen_width - 60), screen_height - (screen_height - 60),
                          width=100, height=50,
                          text="Go back", command=go_main_page_click,
                          font=(my_font, 10))

    # DEBUG: CenterX, CenterY
    round_rectangle(canvas,
                    center['x'] - 1, 0,
                    center['x'] + 1, screen_height,
                    1, fill='red', outline='red', width=1)
    round_rectangle(canvas,
                    0, center['y'] - 1,
                    screen_width, center['y'] + 1,
                    1, fill='red', outline='red', width=1)

    return (accessibility_frame, canvas)


# Create frames for different pages
main_frame = main_menu_table()
start_frame = start_menu_table()
profile_frame = profile_menu_table()
login_frame = log_in_session()
statistics_frame = statistics_menu_table()
accessibility_frame = accessibility_menu_table()

# Call the titles for the different pages
main_label()
start_label()
profile_label()
login_label()
statistics_label()

# Show the main menu as default
login_frame[0].pack(fill="both", expand=True)
# main_frame[0].pack(fill="both", expand=True)

# Uppsala university logo
image = PhotoImage(file=join(images_dir, 'uupsala-400-height-1.png'))

# Scale image
width = int(image.width() * 0.5)
height = int(image.height() * 0.5)
image = image.subsample(int(image.width() / width), int(image.height() / height))

# Add image to window - CHANGE WHEN TEACHER PROVIDES A BETTER ONE
image_label = Label(root, image=image)
image_label.place(relx=1, rely=1, anchor="se")

root.mainloop()
