
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
import pyperclip

width = 300
height = 300
center = height//2
white = (255, 255, 255)
green = (0,128,0)
items = []


def save():
    global counter, entry, inp
    filename = 'Character.jpg'
    image1.save(filename)
    counter +=1
    # Update label
    inp.set(entry + str(counter))
    delete()
    
def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    a = cv.create_oval(x1, y1, x2, y2, fill="black",width=5)
    draw.line([x1, y1, x2, y2],fill="black",width=5)
    items.append(a)
    
def delete():
    run = len(items)
    for i in range(run):
        cv.delete(items[i])
    global image1,draw
    image1 = PIL.Image.new("RGB", (width, height), white)
    draw = ImageDraw.Draw(image1)

root = Tk()
root.title("Akil")
root.resizable(width=False, height=False)
# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)

# do the PIL image/draw (in memory) drawings
# draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
# filename = "my_drawing.png"
# image1.save(filename)

button=Button(text="save",command=save)
button2 = Button(text="delete",command=delete)


entry = 'Number of letters completed: '


inp = StringVar()
e = Label(width=50, textvariable=inp)
inp.set(entry + '1')
button.pack()
#button2.pack()
e.pack(pady=5)

root.mainloop()
