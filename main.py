# Watermarking Project

# imports
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk



LOGO_DIRECTORY = ''


#---------------------------------- FUNCTIONS SETUP ----------------------------------#
# Create function for adding text
def add_text():
    coordinate_x = coordinates_x.get()
    coordinate_y = coordinates_y.get()
    new_text = text_entry.get()
    canvas.create_text(coordinate_x, coordinate_y, text=new_text, tag='text')


# Delete Text
def delete_text():
    canvas.delete('text')


# Creating variables to hold the logos
image_logo = ''
logo_x = ''


# Adding logo
def add_logo():
    # Get hold of global variables
    global image_logo, logo_x
    logo_x = askopenfilename(initialdir=LOGO_DIRECTORY, title="Select a img for logo", filetype=(('jpeg files', '*.jpg'),
                                                                                               ("all files", "*.*")))
    print(logo_x)
    # Open logo images
    if logo_x:
        image_open = Image.open(logo_x)
        image_resized = image_open.resize((28, 28))
        image_logo = ImageTk.PhotoImage(image_resized)
        coordinate_x_logo = coordinates_x_logo.get()
        coordinate_y_logo = coordinates_y_logo.get()

    # Create onto canvas logo image
        logo_image = canvas.create_image(coordinate_x_logo, coordinate_y_logo, image=image_logo, anchor=NW)


# Delete logo
def delete_logo():
    canvas.delete('logo_image')


# Background image searcher
base_image = ''


def load_image():
    global base_image
    base_image = askopenfilename(initialdir=LOGO_DIRECTORY, title="Select a img for logo", filetype=(('jpeg files', '*.jpg'),
                                                                                               ("all files", "*.*")))
    if base_image:
        image_open = Image.open(base_image)
        image_resized = image_open.resize((724, 500))
        base_image_resized = ImageTk.PhotoImage(image_resized)
        background_image = canvas.create_image(0, 0, image=base_image_resized, anchor=NW)


# Delete background image
def delete_image():
    canvas.delete('background_image')


# Save image -> Employ changes made in canvas onto image copy using pillow
def save_image():
    get_bg = Image.open('Foto.png')
    bg_resized = get_bg.resize((724, 500))
    bg_resized.convert('RGBA')
    if logo_x:
        get_logo = Image.open(logo_x)
        get_logo_resized = get_logo.resize((28, 28))
        coordinate_x_logo = int(coordinates_x_logo.get())
        coordinate_y_logo = int(coordinates_y_logo.get())
        bg_resized.paste(get_logo_resized, (coordinate_x_logo, coordinate_y_logo))

    name = f'{logo_x[:-4]} WM.jpg'
    finished_img = bg_resized.convert("RGB")
    finished_img.save(name)


#---------------------------------- WINDOW SETUP ----------------------------------#

# Window setup
window = Tk()
window.title('WaterMarking by Sandro')
window.geometry("800x750")
window.config(bg='white')
window.config(padx=30)
window.wm_attributes('-transparentcolor', 'grey')

# Upload image
im = Image.open('Foto.png')
resized_img = im.resize((724, 500))
logo_image = ImageTk.PhotoImage(resized_img)
canvas = Canvas(height=logo_image.height(), width=logo_image.width())
main_img = canvas.create_image(0, 0, image=logo_image, anchor=NW)
canvas.grid(column=1, row=0, columnspan=4, sticky=NW)


# Entry - TEXT
text_entry = Entry(width=10, bg="white")
text_entry.grid(column=3, row=6, sticky=NW)
text_entry.focus()
text_entry.insert(0, '@Sandro')
coordinates_x = Entry(width=10, bg="white")
coordinates_x.grid(column=3, row=7, sticky=NW)
coordinates_x.focus()
coordinates_x.insert(END, '700')
coordinates_y = Entry(width=10, bg="white")
coordinates_y.grid(column=3, row=8, sticky=NW)
coordinates_y.focus()
coordinates_y.insert(END, '200')

# Entry - LOGO
coordinates_x_logo = Entry(width=10, bg="white")
coordinates_x_logo.grid(column=4, row=7, sticky=NW)
coordinates_x_logo.focus()
coordinates_x_logo.insert(END, '100')
coordinates_y_logo = Entry(width=10, bg="white")
coordinates_y_logo.grid(column=4, row=8, sticky=NW)
coordinates_y_logo.focus()
coordinates_y_logo.insert(END, '100')

# Labels - TEXT
text = Label(text='Text configs', font=('Arial',15), bg="white")
text.grid(column=2, row=4, sticky=NE)
text_label = Label(text='Tag text',font=('Arial', 10), bg="white")
text_label.grid(column=2, row=5, sticky=NE)
x_label = Label(text='X coordinate', font=('Arial', 10), bg="white")
x_label.grid(column=2, row=7, sticky=NE)
y_label = Label(text='Y coordinate', font=('Arial', 10), bg="white")
y_label.grid(column=2, row=8, sticky=NE)


# Labels - LOGO
logo = Label(text='Logo configs', font=('Arial',15), bg="white")
logo.grid(column=3, row=4, sticky=NE)
x_label_logo = Label(text='X coordinate', font=('Arial', 10), bg="white")
x_label_logo.grid(column=3, row=7, sticky=NE)
y_label_logo = Label(text='Y coordinate', font=('Arial', 10), bg="white")
y_label_logo.grid(column=3, row=8, sticky=NE)

# Buttons - TEXT
text_button = Button(text="Add text", highlightthickness=0, command=add_text, width=10)
text_button.grid(column=3, row=9, sticky=NW)
delete_text_button = Button(text="Delete text", highlightthickness=0, command=delete_text, width=10)
delete_text_button.grid(column=3, row=10, sticky=NW)

# Buttons - LOGO
add_logo_button = Button(text="Add Logo", highlightthickness=0, command=add_logo, width=10)
add_logo_button.grid(column=4, row=9, sticky=NW)
delete_logo_button = Button(text="Delete Logo", highlightthickness=0, command=delete_logo, width=10)
delete_logo_button.grid(column=4, row=10, sticky=NW)


# Image buttons
add_background_button = Button(text="Add image", font=('Arial', 15), width= 15, highlightthickness=0, command=load_image)
add_background_button.grid(column=1, row=4, columnspan=3, sticky=NW)
delete_background_button = Button(text="Delete image", font=('Arial', 15),width= 15, highlightthickness=0, command=delete_image)
delete_background_button.grid(column=1, row=5, columnspan=3,sticky=NW)
save_canvas_image = Button(text="Save image", font=('Arial', 15), width= 15, highlightthickness=0, command=save_image)
save_canvas_image.grid(column=1, row=6, columnspan=3, sticky=NW)


window.mainloop()




