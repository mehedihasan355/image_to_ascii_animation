import tkinter
# from pywhatkit import image_to_ascii_art
from tkinter import * 
from customTkinter import CustomTitle,custom_geometry
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import pyperclip
import time

speach = "Give me a Clear Photo and I will show you a Magic"
font_style = ('Candara',13)

def convert_ascii(path):
    image_path = path
    img = Image.open(image_path)

    # resize the image
    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    # new size of image

    # convert image to greyscale format
    img = img.convert('L')

    pixels = img.getdata()

    # replace each pixel with a character from array
    chars = [":","S","#","&","@","$","%","*","!",":","."]
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    return ascii_image

def save(str):
    file = filedialog.asksaveasfile(title='Save as',
    defaultextension=".txt",initialfile='Untitled.txt',
    filetypes=[("Text files", "*.txt"),("All files", "*.*")])
    file.write(str)

def restart(shower,btn_frame):
    shower.destroy()
    btn_frame.destroy()
    title_bar._maximize_win()
    root.update()

    win_width = root.winfo_width()
    win_height = root.winfo_height()
    frame_width = 200
    frame_height = 250
    frame = Frame(root,width=300,height=300)
    frame.place(x=win_width/2 - frame_width,y=win_height/2-frame_height)

    Label(frame,text=speach,font=font_style).grid(row = 0,columnspan=7)


    open_btn = Button(frame,text='Give Photo',font = font_style,relief=GROOVE,command=getFile)
    open_btn.grid(row=1,column=3,pady=20)


def AsciiShower(ascii):
    def copy():
        pyperclip.copy(shower.get(1.0,END))
    frame.destroy()
    root.update()
    timer_list = ["Are you ready?","1","2","3","Let's Begin"]
    font = ('Candara',52)
    for timer_text in timer_list:
        timer_label = Label(root,text=timer_text,font=font)
        timer_label.pack(expand=True)
        root.update()
        time.sleep(.8)
        timer_label.destroy()
        root.update()
    title_bar._maximize_win()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+{0}+{0}")
    root.update()
    btn_frame = Frame(root,bg ="#000000" )
    btn_frame.pack(fill=X)
    shower = Text(root,font=('Consolas',9),width=win_width,height=win_height,bg="#000000",fg="#ffffff")
    shower.config(spacing1=.05)
    shower.config(spacing2=.05)
    shower.config(spacing3=.05)
    shower.pack()

    for index,car in enumerate(ascii):
        shower.insert(float(index+1), chars=car)
        shower.update()
    
    copy_button= Button(btn_frame,text='Copy',relief=GROOVE,command=copy)
    copy_button.grid(row=0,column=0,pady=12,padx=5)
    save_button= Button(btn_frame,text='Save',relief=GROOVE,command=lambda: save(shower.get(1.0,END)))
    save_button.grid(row=0,column=2,pady=12)
    restart_button= Button(btn_frame,text='Restart',relief=GROOVE,command=lambda:restart(shower,btn_frame))
    restart_button.grid(row=0,column=3,pady=12,padx=5)
        



def getFile():
    path = filedialog.askopenfilename(title="Give File")
    try:
        # ascii = image_to_ascii_art(path)
        ascii = convert_ascii(path)
        # print(ascii)
        file_name_label = Label(frame,text=path.split('/')[-1])
        file_name_label.grid(row=1,column=4,)
        start_btn = Button(frame,text='Start Magic',font = font_style,relief=GROOVE,command=lambda: AsciiShower(ascii))
        start_btn.grid(row=2,column=3,)
    except Exception as e:
        messagebox.askretrycancel(title="Error",message="Unknown File... Please Give a Image file" + e)
        path = ''
        return



root = Tk()
title_bar = CustomTitle(root,'MH - Magic with Photo',bg = '#232a2e' , fg = '#ffffff')
title_bar.resizeable = False
title_bar.packBar()
custom_geometry(root,700,700)
root.update()

win_width = root.winfo_width()
win_height = root.winfo_height()
frame_width = 200
frame_height = 250
frame = Frame(root,width=300,height=300)

frame.place(x=win_width/2 - frame_width,y=win_height/2-frame_height)

Label(frame,text=speach,font=font_style).grid(row = 0,columnspan=7)


open_btn = Button(frame,text='Give Photo',font = font_style,relief=GROOVE,command=getFile)
open_btn.grid(row=1,column=3,pady=20)


root.iconbitmap("src/m.ico")
root.mainloop()