# importing the libraries needed for the gui
import tkinter as tk
from PIL import Image, ImageTk

# generating the gui window
root = tk.Tk()

# giving it a title
root.title("Artista - Female Art in One Place")

# configuring the size
root.geometry("453x608")

# creating a variable that stores the name of user
user_name = tk.StringVar()


def add_image(root, file_path):
    """This definition accesses the images for the gui windows."""

    # specifying global variables in order for the images to appear
    global pic, f1

    # creating the frame for the windows
    f1 = tk.Frame(root)
    # accessing the images through a file-path
    img = Image.open(file_path)
    # aligning the size of the images with the gui windows
    img = img.resize((453, 608), Image.LANCZOS)
    # viewing the image as the frame
    pic = ImageTk.PhotoImage(img)
    lab = tk.Label(f1, image=pic)
    # placing the image
    lab.pack()
    f1.pack()


def page_one():
    """This definition generates the first page and its objects."""

    # specifying the global variables of the first page
    global headline_label, description_label, description_two_label, log_in_button, name_input

    # refer to the add_image function with the file path of the first image
    add_image(root, file_path="images/first.jpg")

    # adding labels to appear on the first page
    headline_label = tk.Label(root, text="ARTISTA:",
                              font="rockwell 40",
                              relief=tk.RAISED,
                              background="pink",
                              borderwidth=8)

    # adjusting the exact position where the objects appear
    headline_label.place(x=100, y=35)

    description_label = tk.Label(root, text="the latest releases of female artists -",
                                 font="rockwell 17",
                                 relief=tk.RAISED,
                                 background="pink")
    description_label.place(x=25, y=125)

    description_two_label = tk.Label(root, text="all in one place.",
                                     font="rockwell 17",
                                     relief=tk.RAISED,
                                     background="pink")
    description_two_label.place(x=135, y=160)

    # adding a button on the first gui window that clears everything and launches the second page
    log_in_button = tk.Button(text="Log In with Your Name",
                              font="rockwell 11",
                              relief=tk.RAISED,
                              command=page_two,
                              background="pink")
    log_in_button.place(x=140, y=240)

    # creating a box which stores the name of the user
    name_input = tk.Entry(root, textvariable=user_name)
    name_input.place(x=160, y=280)


def page_two():
    """This definition destroys everything created in the first page, adds a new image as well as new labels."""

    global welcome_label, new_label, movies_button, music_button, events_button, books_button, back_button, info_button,\
        button_close

    # destroying all objects of the first page
    f1.destroy()
    log_in_button.destroy()
    headline_label.destroy()
    description_label.destroy()
    description_two_label.destroy()
    name_input.destroy()

    add_image(root, file_path="images/second.png")

    welcome_label = tk.Label(root, text=f"Welcome back {user_name.get()}!",
                             font="rockwell 15",
                             relief=tk.RAISED,
                             background="white",
                             borderwidth=6)
    welcome_label.place(x=35, y=23)

    new_label = tk.Label(root, text="What's new?",
                         font="rockwell 13",
                         relief=tk.RAISED,
                         background="white",
                         borderwidth=4)
    new_label.place(x=84, y=90)

    movies_button = tk.Button(root, text="Movies",
                              font="rockwell 16",
                              command=page_four,
                              relief=tk.RAISED,
                              background="pink")
    movies_button.place(x=295, y=187)

    music_button = tk.Button(root, text="Music",
                             font="rockwell 16",
                             command=page_five,
                             relief=tk.RAISED,
                             background="pink")
    music_button.place(x=90, y=292)

    events_button = tk.Button(root, text="Events",
                              font="rockwell 12",
                              command=page_six,
                              relief=tk.RAISED,
                              background="pink")
    events_button.place(x=300, y=345)

    books_button = tk.Button(root, text="Books",
                             font="rockwell 16",
                             command=page_seven,
                             relief=tk.RAISED,
                             background="pink")
    books_button.place(x=90, y=478)

    # adding a button that goes back to the first page
    back_button = tk.Button(text="Back",
                            font="rockwell 11",
                            command=back,
                            background="white")
    back_button.place(x=38, y=560)

    # adding a button that closes the entire gui
    button_close = tk.Button(text="Close",
                             font="rockwell 11",
                             command=root.destroy,
                             background="white")
    button_close.place(x=360, y=560)

    # adding a button that leads to the third page
    info_button = tk.Button(root, text="About Us",
                            font="rockwell 11",
                            command=page_three,
                            background="pink")
    info_button.place(x=185, y=560)


def page_three():
    """This definition deletes everything created in the second page and launches the third one."""

    global about_us_label, back_button, button_close

    f1.destroy()
    welcome_label.destroy()
    new_label.destroy()
    movies_button.destroy()
    music_button.destroy()
    events_button.destroy()
    books_button.destroy()
    info_button.destroy()

    add_image(root, file_path="images/third.jpg")

    about_us_label = tk.Label(root, text="What is Artista?",
                              font="rockwell 18",
                              relief=tk.RAISED,
                              background="white",
                              borderwidth=6)
    about_us_label.place(x=217, y=31)

    button_close = tk.Button(text="Close",
                             font="rockwell 11",
                             command=root.destroy,
                             background="white")
    button_close.place(x=180, y=560)

    back_button = tk.Button(text="Back",
                            font="rockwell 11",
                            command=back_two,
                            background="white")
    back_button.place(x=38, y=560)


def page_four():
    """This definition erases everything created in the second page and launches the fourth one."""

    global movies_label, most_popular_label, back_button, button_close, info_button

    f1.destroy()
    welcome_label.destroy()
    new_label.destroy()
    movies_button.destroy()
    music_button.destroy()
    events_button.destroy()
    books_button.destroy()

    add_image(root, file_path="images/fourth.png")

    movies_label = tk.Label(root, text="Movies",
                            font="rockwell 50",
                            relief=tk.RAISED,
                            background="white",
                            borderwidth=6)
    movies_label.place(x=105, y=30)

    most_popular_label = tk.Label(root, text="Most Popular:",
                                  font="rockwell 13",
                                  relief=tk.RAISED,
                                  background="pink",
                                  borderwidth=4)
    most_popular_label.place(x=70, y=200)

    back_button = tk.Button(text="Back",
                            font="rockwell 11",
                            command=back_three,
                            background="white")
    back_button.place(x=45, y=565)

    button_close = tk.Button(text="Close",
                             font="rockwell 11",
                             command=root.destroy,
                             background="white")
    button_close.place(x=355, y=565)

    info_button = tk.Button(root, text="About Us",
                            font="rockwell 13",
                            command=page_three,
                            background="pink")
    info_button.place(x=185, y=561)


def page_five():
    """This definition destroys everything created in the second page and launches the fifth one."""

    global music_label, back_button, button_close, info_button

    f1.destroy()
    welcome_label.destroy()
    new_label.destroy()
    movies_button.destroy()
    music_button.destroy()
    events_button.destroy()
    books_button.destroy()

    add_image(root, file_path="images/fifth.png")

    music_label = tk.Label(root, text="Music",
                           font="rockwell 50",
                           relief=tk.RAISED,
                           background="pink",
                           borderwidth=6)
    music_label.place(x=40, y=80)

    back_button = tk.Button(text="Back",
                            font="rockwell 11",
                            command=back_four,
                            background="white")
    back_button.place(x=45, y=565)

    button_close = tk.Button(text="Close",
                             font="rockwell 11",
                             command=root.destroy,
                             background="white")
    button_close.place(x=355, y=565)

    info_button = tk.Button(root, text="About Us",
                            font="rockwell 13",
                            command=page_three,
                            background="pink")
    info_button.place(x=185, y=561)


def page_six():
    """This definition destroys everything created in the second page and launches the sixth one."""

    global events_label, back_button, button_close, info_button

    f1.destroy()
    welcome_label.destroy()
    new_label.destroy()
    movies_button.destroy()
    music_button.destroy()
    events_button.destroy()
    books_button.destroy()

    add_image(root, file_path="images/sixth.png")

    events_label = tk.Label(root, text="Upcoming\nEvents",
                            font="rockwell 40",
                            relief=tk.RAISED,
                            background="white",
                            borderwidth=6)
    events_label.place(x=95, y=35)

    back_button = tk.Button(text="Back",
                            font="rockwell 11",
                            command=back_five,
                            background="white")
    back_button.place(x=45, y=565)

    button_close = tk.Button(text="Close",
                             font="rockwell 11",
                             command=root.destroy,
                             background="white")
    button_close.place(x=355, y=565)

    info_button = tk.Button(root, text="About Us",
                            font="rockwell 13",
                            command=page_three,
                            background="pink")
    info_button.place(x=185, y=561)


def page_seven():
    """This definition deletes everything created in the second page and launches the seventh one."""

    global books_label, popular_label, back_button, button_close, info_button

    f1.destroy()
    welcome_label.destroy()
    new_label.destroy()
    movies_button.destroy()
    music_button.destroy()
    events_button.destroy()
    books_button.destroy()

    add_image(root, file_path="images/seventh.png")

    books_label = tk.Label(root, text="Books",
                           font="rockwell 45",
                           relief=tk.RAISED,
                           background="pink",
                           borderwidth=6)
    books_label.place(x=200, y=45)

    popular_label = tk.Label(root, text="Popular this Week:",
                             font="rockwell 13",
                             relief=tk.RAISED,
                             background="white",
                             borderwidth=4)
    popular_label.place(x=280, y=400)

    back_button = tk.Button(text="Back",
                            font="rockwell 11",
                            command=back_six,
                            background="white")
    back_button.place(x=45, y=565)

    button_close = tk.Button(text="Close",
                             font="rockwell 11",
                             command=root.destroy,
                             background="white")
    button_close.place(x=355, y=565)

    info_button = tk.Button(root, text="About Us",
                            font="rockwell 13",
                            command=page_three,
                            background="pink")
    info_button.place(x=185, y=561)


def back():
    """This definition destroys every object in the second page and goes back to the first one."""

    f1.destroy()
    welcome_label.destroy()
    new_label.destroy()
    movies_button.destroy()
    music_button.destroy()
    events_button.destroy()
    books_button.destroy()
    info_button.destroy()

    # reopening the first page
    page_one()


def back_two():
    """This definition deletes all objects of the third page and goes back to the second one."""

    f1.destroy()
    about_us_label.destroy()

    page_two()


def back_three():
    """This definition destroys all objects of the fourth page and goes back to the second one."""

    f1.destroy()
    movies_label.destroy()
    most_popular_label.destroy()

    page_two()


def back_four():
    """This definition deletes all objects of the fifth page and goes back to the second one."""

    f1.destroy()
    music_label.destroy()

    page_two()


def back_five():
    """This definition erases all objects of the sixth page and goes back to the second one."""

    f1.destroy()
    events_label.destroy()

    page_two()


def back_six():
    """This definition destroys all objects of the seventh page and goes back to the second one."""

    f1.destroy()
    books_label.destroy()
    popular_label.destroy()

    page_two()


# calling the first page function which adds an image and a log-in button
page_one()

# executing the code
root.mainloop()
