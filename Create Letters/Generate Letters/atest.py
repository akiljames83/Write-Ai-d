
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *

width = 300
height = 300
center = height//2
white = (255, 255, 255)
green = (0,128,0)
items = []

counter = 150

letters = ['letter1', 'letter2', 'letter3', 'letter4', 'letter5', 'letter6', 'letter7', 'letter8', 'letter9', 'letter10', 'letter11', 'letter12', 'letter13', 'letter14', 'letter15', 'letter16', 'letter17', 'letter18', 'letter19', 'letter20', 'letter21', 'letter22', 'letter23', 'letter24', 'letter25', 'letter26', 'letter27', 'letter28', 'letter29', 'letter30', 'letter31', 'letter32', 'letter33', 'letter34', 'letter35', 'letter36', 'letter37', 'letter38', 'letter39', 'letter40', 'letter41', 'letter42', 'letter43', 'letter44', 'letter45', 'letter46', 'letter47', 'letter48', 'letter49', 'letter50', 'letter51', 'letter52', 'letter53', 'letter54', 'letter55', 'letter56', 'letter57', 'letter58', 'letter59', 'letter60', 'letter61', 'letter62', 'letter63', 'letter64', 'letter65', 'letter66', 'letter67', 'letter68', 'letter69', 'letter70', 'letter71', 'letter72', 'letter73', 'letter74', 'letter75', 'letter76', 'letter77', 'letter78', 'letter79', 'letter80', 'letter81', 'letter82', 'letter83', 'letter84', 'letter85', 'letter86', 'letter87', 'letter88', 'letter89', 'letter90', 'letter91', 'letter92', 'letter93', 'letter94', 'letter95', 'letter96', 'letter97', 'letter98', 'letter99', 'letter100', 'letter101', 'letter102', 'letter103', 'letter104', 'letter105', 'letter106', 'letter107', 'letter108', 'letter109', 'letter110', 'letter111', 'letter112', 'letter113', 'letter114', 'letter115', 'letter116', 'letter117', 'letter118', 'letter119', 'letter120', 'letter121', 'letter122', 'letter123', 'letter124', 'letter125', 'letter126', 'letter127', 'letter128', 'letter129', 'letter130', 'letter131', 'letter132', 'letter133', 'letter134', 'letter135', 'letter136', 'letter137', 'letter138', 'letter139', 'letter140', 'letter141', 'letter142', 'letter143', 'letter144', 'letter145', 'letter146', 'letter147', 'letter148', 'letter149', 'letter150', 'letter151', 'letter152', 'letter153', 'letter154', 'letter155', 'letter156', 'letter157', 'letter158', 'letter159', 'letter160', 'letter161', 'letter162', 'letter163', 'letter164', 'letter165', 'letter166', 'letter167', 'letter168', 'letter169', 'letter170', 'letter171', 'letter172', 'letter173', 'letter174', 'letter175', 'letter176', 'letter177', 'letter178', 'letter179', 'letter180', 'letter181', 'letter182', 'letter183', 'letter184', 'letter185', 'letter186', 'letter187', 'letter188', 'letter189', 'letter190', 'letter191', 'letter192', 'letter193', 'letter194', 'letter195', 'letter196', 'letter197', 'letter198', 'letter199', 'letter200', 'letter201', 'letter202', 'letter203', 'letter204', 'letter205', 'letter206', 'letter207', 'letter208', 'letter209', 'letter210', 'letter211', 'letter212', 'letter213', 'letter214', 'letter215', 'letter216', 'letter217', 'letter218', 'letter219', 'letter220', 'letter221', 'letter222', 'letter223', 'letter224', 'letter225', 'letter226', 'letter227', 'letter228', 'letter229', 'letter230', 'letter231', 'letter232', 'letter233', 'letter234', 'letter235', 'letter236', 'letter237', 'letter238', 'letter239', 'letter240', 'letter241', 'letter242', 'letter243', 'letter244', 'letter245', 'letter246', 'letter247', 'letter248', 'letter249', 'letter250', 'letter251', 'letter252', 'letter253', 'letter254', 'letter255', 'letter256', 'letter257', 'letter258', 'letter259', 'letter260', 'letter261', 'letter262', 'letter263', 'letter264', 'letter265', 'letter266', 'letter267', 'letter268', 'letter269', 'letter270', 'letter271', 'letter272', 'letter273', 'letter274', 'letter275', 'letter276', 'letter277', 'letter278', 'letter279', 'letter280', 'letter281', 'letter282', 'letter283', 'letter284', 'letter285', 'letter286', 'letter287', 'letter288', 'letter289', 'letter290', 'letter291', 'letter292', 'letter293', 'letter294', 'letter295', 'letter296', 'letter297', 'letter298', 'letter299', 'letter300']
def save():
    global counter, entry, inp
    if counter < 300:
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

#cv.pack(expand=YES, fill=BOTH)
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
