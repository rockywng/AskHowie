import urllib.request,sys,time
import requests
import pandas
import tkinter as tk
import tkinter.font as tkFont
from newspaper import Article
import math
import os

# Height of frame upon which elements will be added
HEIGHT = 350

# Width of frame upon which elements will be added
WIDTH = 500

# base_folder uses os to create a path to the folder this file is in
base_folder = os.path.dirname(__file__)
# image_path searches the base folder for the blueback.gif file which
# is to be the background
image_path = os.path.join(base_folder, 'blueback.gif')

def calculate_time(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        wordcount = len(text.split())
        time = wordcount / 225
        minutes = math.floor(time)
        seconds_not_rounded = 60 * (time - minutes)
        seconds = round(seconds_not_rounded, 0)
        seconds_str = str(seconds)[:-2]
        if minutes == 1 and seconds == 1:
            statement = "This article will take 1 minute and 1 second to read. Happy reading!"
        if minutes == 1 and seconds == 0:
            statement = "This article will take 1 minute to read. Happy reading!"
        if minutes == 0 and seconds == 1:
            statement = "This article will take 1 second to read. Happy reading!"
        if minutes == 1:
            statement = "This article will take 1 minute and " + seconds_str 
            statement += " minutes to read. Happy reading!"
        if seconds == 1:
            statement = "This article will take " + str(minutes)
            statement += " minutes and 1 second to read."
        if minutes == 0:
            statement = "This article will take " + seconds_str 
            statement += " seconds to read.\nHappy reading!"
        if seconds == 0:
            statement = "This article will take " + str(minutes)
            statement += " minutes to read.\nHappy reading!"
        else:
            statement = "This article will take " + str(minutes)
            statement += " minutes\nand " + seconds_str + " seconds to read. Happy reading!"
    except:
        statement = "Sorry, you did not submit a valid link. Please try again."
    label['text'] = statement

root = tk.Tk()
# makes the window size static
root.resizable(False, False)

# produces a blank canvas upon which elements can be added and positioned
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# the font style for the text that will appear displaying the service name
titlestyle=tkFont.Font(family= "Lucida Grande", size=40)

# makes the background photo found previously an element that can be added
background_image = tk.PhotoImage(file=image_path)

# creates a label element with background_image as its image
background_label = tk.Label(root, image=background_image)

# places the background label such that it takes up the entire canvas
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# creates a frame element with a given background colour and border width 5
frame = tk.Frame(root, bg='#2575C6', bd=5)

# places the frame such that it is centred at 50% of the width of the canvas
# and 27.5% of the height of the canvas, and has a width equal to 75% of
# the width of the canvas and a height of 10% of the height of the canvas
frame.place(relx=0.5, rely=0.275, relwidth=0.75, relheight=0.1, anchor='n')

# creates a frame element that will contain the service title
upper_frame = tk.Frame(root, bg='#003366', bd=10)

# places the frame such that it is centred at 50% of the width and 7% of the height,
# and has a width equal to 60% of the canvas and 20% of the height of the canvas
upper_frame.place(relx=0.5, rely=0.07, relwidth=0.6, relheight=0.2, anchor='n')

# creates a label element containing the string "BlueChip" with font being the
# previously defined titlestyle
upper_label = tk.Label(upper_frame, fg="#ffffff", bg='#003366', text="Ask Howie", font=titlestyle)

# places the label in the upper_frame element such that it has identical width and height
# to upper_frame
upper_label.place(relwidth=1, relheight=1)

# creates a frame element that will contain details related to the creator of this 
# service (me!)a
name_frame = tk.Frame(root, bg='#003366', bd=10)

# places the frame such that it is centred at 85% of the canvas width and the highest
# point of the canvas height while having width equal to 30% of the canvas width 
# and height equal to 15% of the canvas height
name_frame.place(relx=0.85, rely=0, relwidth=0.3, relheight=0.13, anchor='n')

# creates a label element that contains details pertaining to the creator of the service
# that will exist within the name_frame frame
name_label = tk.Label(name_frame, fg="#ffffff", bg="#003366", text="Designed by Rocky Wang\nr533wang@uwaterloo.ca")

# places the label element in the name_frame frame with height and width both equal to 100%
# of the frame
name_label.place(relwidth=1, relheight=1)

# creates an entry element that will consume the user input with a given font size and colour
entry = tk.Entry(frame, fg="#16589B", font=40)

# places the entry element into the frame element with width equal to 57.5% of the frame and 
# 100% of the frame height
entry.place(relwidth=0.575, relheight=1)

# creates a button element that, when pressed will submit the user input as the entry element
# for get_stock
button = tk.Button(frame, text="Submit", font=1, fg='#FFFFFF', bg='#003366', command=lambda: calculate_time(entry.get()))

# places the button element in the frame element centred at 60% of the frame width with height 
# equal to 100% of the frame height and width equal to 40% of the frame width
button.place(relx=0.6, relheight=1, relwidth=0.4)

# creates a frame element with a given background colour and border width
lower_frame = tk.Frame(root, bg='#2575C6', bd=10)

# places the lower_frame element centered at 50% of the canvas width and 40% of the canvas height
# with width equal to 75% of the canvas width and height equal to 55% of the canvas height
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.55, anchor='n')

# creates a label element that will be used to  display the welcome message to users and 
# to display the response to user inputs to the user
label = tk.Label(lower_frame, fg="#000000", text="Welcome to Ask Howie! Just enter the link to the article\nyou'd like Howie to read and he'll tell you how long it\nwill take you to read it.")
# places the response label element in the lower_frame element with width equal to 100% of the 
# lower_frame width and height equal to 100% of the lower_frame
label.place(relwidth=1, relheight=1)

root.mainloop()



