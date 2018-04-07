
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *

width = 300
height = 300
center = height//2
white = (255, 255, 255)
green = (0,128,0)
items = []

counter = 50

letters = ['letter1', 'letter2', 'letter3', 'letter4', 'letter5', 'letter6', 'letter7', 'letter8', 'letter9', 'letter10', 'letter11', 'letter12', 'letter13', 'letter14', 'letter15', 'letter16', 'letter17', 'letter18', 'letter19', 'letter20', 'letter21', 'letter22', 'letter23', 'letter24', 'letter25', 'letter26', 'letter27', 'letter28', 'letter29', 'letter30', 'letter31', 'letter32', 'letter33', 'letter34', 'letter35', 'letter36', 'letter37', 'letter38', 'letter39', 'letter40', 'letter41', 'letter42', 'letter43', 'letter44', 'letter45', 'letter46', 'letter47', 'letter48', 'letter49', 'letter50', 'letter51', 'letter52', 'letter53', 'letter54', 'letter55', 'letter56', 'letter57', 'letter58', 'letter59', 'letter60', 'letter61', 'letter62', 'letter63', 'letter64', 'letter65', 'letter66', 'letter67', 'letter68', 'letter69', 'letter70', 'letter71', 'letter72', 'letter73', 'letter74', 'letter75', 'letter76', 'letter77', 'letter78', 'letter79', 'letter80', 'letter81', 'letter82', 'letter83', 'letter84', 'letter85', 'letter86', 'letter87', 'letter88', 'letter89', 'letter90', 'letter91', 'letter92', 'letter93', 'letter94', 'letter95', 'letter96', 'letter97', 'letter98', 'letter99', 'letter100', 'letter101', 'letter102', 'letter103', 'letter104', 'letter105', 'letter106', 'letter107', 'letter108', 'letter109', 'letter110', 'letter111', 'letter112', 'letter113', 'letter114', 'letter115', 'letter116', 'letter117', 'letter118', 'letter119', 'letter120', 'letter121', 'letter122', 'letter123', 'letter124', 'letter125', 'letter126', 'letter127', 'letter128', 'letter129', 'letter130', 'letter131', 'letter132', 'letter133', 'letter134', 'letter135', 'letter136', 'letter137', 'letter138', 'letter139', 'letter140', 'letter141', 'letter142', 'letter143', 'letter144', 'letter145', 'letter146', 'letter147', 'letter148', 'letter149', 'letter150']

def save():
    global counter, entry, inp
    if counter < 150:
        filename = letters[counter] + '.jpg'
        #filename = "image.png"
        image1.save(filename)
        counter +=1
        # Update label
        inp.set(entry + str(counter))
        delete()
    else:
        inp.set('Done!')
        root.quit()


def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    a = cv.create_oval(x1, y1, x2, y2, fill="black",width=5)
    draw.line([x1, y1, x2, y2],fill="black",width=5)
    items.append(a)
    

def delete():
	#cv.create_rectangle(0, 0, 300, 300, fill="white",width=0)
	#draw.line([50, 50, 100, 100],fill="white",width=0)
    run = len(items)
    for i in range(run):
        cv.delete(items[i])
    global image1,draw
    image1 = PIL.Image.new("RGB", (width, height), white)
    draw = ImageDraw.Draw(image1)

root = Tk()
root.resizable(width=False, height=False)
# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

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
inp.set(entry + str(counter))
button.pack()
#button2.pack()
e.pack(pady=5)
root.mainloop()
