# modules that need to be imported for the tensorflow image analyzing function to run
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from PIL import ImageTk, Image, ImageDraw # modules necesary for drawing on the screen and capturing the image
import PIL # import the entire pillow module
from tkinter import * # import the entire contents of the tkinter module
import pyperclip # import module to assist in copying and pasting
import numpy as np # import numpy is useful for data processing
import tensorflow as tf # module necesary for the creation and the use of the machine learning algorithm

# Intializing of variables necessary for the function
width = 500 # width of the image canvas PIL
height = 500 # height of the image canvas via PI
center = height//2 # ceneter of the canvas
white = (255, 255, 255) # initializing white color
green = (0,128,0) # initializing green color
items = [] # list used to store the data points created using the drawing function via pillow

text = '' # global text variable used in tracking the progress of the words analyzed via machine learning algorithm

def load_graph(model_file): # graph that was created through the training process of the machine learning algorithm (MLA)
  graph = tf.Graph() # initalizing the tensorflow graph
  graph_def = tf.GraphDef()

  with open(model_file, "rb") as f: # opening up the graph file (input of the function)
    graph_def.ParseFromString(f.read()) # rest of this function is source code from tensor flow website/documentation to initilaize/create the image recognition sesson
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph

def read_tensor_from_image_file(file_name,
                                input_height=299,
                                input_width=299,
                                input_mean=0,
                                input_std=255): # initializing many vriables ## source code with slight modifications to analyze a particular image file, JPEG in our case
  input_name = "file_reader"
  output_name = "normalized"
  file_reader = tf.read_file(file_name, input_name)
  if file_name.endswith(".png"):
    image_reader = tf.image.decode_png(
        file_reader, channels=3, name="png_reader")
  elif file_name.endswith(".gif"):
    image_reader = tf.squeeze(
        tf.image.decode_gif(file_reader, name="gif_reader"))
  elif file_name.endswith(".bmp"):
    image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
  else:
    image_reader = tf.image.decode_jpeg(
        file_reader, channels=3, name="jpeg_reader")
  float_caster = tf.cast(image_reader, tf.float32)
  dims_expander = tf.expand_dims(float_caster, 0)
  resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
  normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
  sess = tf.Session()
  result = sess.run(normalized)

  return result


def load_labels(label_file): # this function labels the various output of the MLA to specify what each image corresponds to (classes initialized when image set was trained)
  label = []
  proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
  for l in proto_as_ascii_lines:
    label.append(l.rstrip())
  return label

def analyzeImage(): # Custom function to anaylze image with set parameters, predetermined by the group to give optimal image analysis results
  input_height = 299 # height of image
  input_width = 299 # width of image
  input_mean = 128 # parameters to aid in the accuarcy of the MLA
  input_std = 128
  input_layer = "Mul"
  output_layer = "final_result"
  model_file = "output_graph.pb" # graph used for ML anaylsis generated from the retraining file
  label_file = "output_labels.txt" # labels for the outputs of the MLA
  file_name = "character.jpg" # image to be analyzed each time the algorithim/function is run

  graph = load_graph(model_file) #  load the graph using the loa_graph function defined ealier in the program
  t = read_tensor_from_image_file( # arguments of the read_tensor_from_image file are those defined above ## same setting are used on each iteration of the algorithm
      file_name,
      input_height=input_height,
      input_width=input_width,
      input_mean=input_mean,
      input_std=input_std)

  input_name = "import/" + input_layer
  output_name = "import/" + output_layer
  input_operation = graph.get_operation_by_name(input_name)
  output_operation = graph.get_operation_by_name(output_name)

  # begin tensorflow session to analyze the image
  with tf.Session(graph=graph) as sess: 
    results = sess.run(output_operation.outputs[0], {
        input_operation.outputs[0]: t
    })
  results = np.squeeze(results)

  # create the top 5 results for the MLA in order of the probability of accuaracy
  top_k = results.argsort()[-5:][::-1] 
  labels = load_labels(label_file)
  for i in top_k:
    # return the name (label) of the most probable letter as determined by the MLA
    return labels[i] 

def paint(event): # Function used to draw on the screen (canvas); essentially create ovals of diameter 5 
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    a = cv.create_oval(x1, y1, x2, y2, fill="black",width=5)
    draw.line([x1, y1, x2, y2],fill="black",width=5)
    items.append(a) # the values are appended to the list 'items' so they can be deleted at a later time

def check(): 
    '''
    This function has 3 parts:
    - firstly it saves the image drawing on the canvas
    - it deletes the image from the screen and initializes a new drawing event to begin
    - finally it uses the MLA (analayzeImage) to deterime which character was displayed
    '''
    global text, displayText, image1,draw # initialize various global variables
    filename = 'character.jpg' # save image to a constant name, this means that images drawn by individual are overwritten upon each iteration of this function
    image1.save(filename) # save the image to this name ^ as a jpg
    
    run = len(items)
    for i in range(run): # using the items list, delete the contents of the canvas drawing one by one
        cv.delete(items[i])
    image1 = PIL.Image.new("RGB", (width, height), white) # initialize a new drawing on the canvas
    draw = ImageDraw.Draw(image1)

    # Call Machine Learning Function on the New Image
    ans = analyzeImage() # analyze the image that was recently created
    text += ans # add this character to the global variable text
    displayText.set(text) # use string variable (part of tkinter) to display this updated phrase

# Defining the Functions for the Push Buttons on the Tkinter window to provide functionality to the users writing

def delete(): # function to delete the contents of the canvas window // explained above
    run = len(items)
    for i in range(run):
        cv.delete(items[i])
    global image1,draw
    image1 = PIL.Image.new("RGB", (width, height), white)
    draw = ImageDraw.Draw(image1)
    
def space(): # function to add a space to the string variable using the text and displayText global vraiables
    global text, displayText
    text += ' '
    displayText.set(text)
    
def back():
    global text, displayText
    text = text[:-1] # remove last indicie of the text gv and update string variable
    displayText.set(text)
    
def clear2(): # function to reinitialize the text variable to an empty string
    global text, displayText
    text = ''
    displayText.set(text)
    
def copy(): # using the 'pyperclip' module, copy the gv text's contents to the user clipboard
    global text, displayText
    displayText.set(text)
    pyperclip.copy(text)

# Defining the Tkiner window 
root = Tk() # initiallization of the tkinter window (Graphical User Interface)
root.title("Letter Checker")
root.resizable(width=False,height=False)
displayText = StringVar()
cv = Canvas(root, width=width, height=height, bg='white')

check = Button(text="Check", command=check)
clear = Button(text="Clear", command=delete)
space = Button(text="Space", command=space)
delete = Button(text="Backspace", command=back)

label1 = Label(text="Your Text", font=" none 11 underline bold")
label2 = Label(textvariable =displayText)

clearSecond = Button(text="Clear Textbox", command=clear2)
copy = Button(text="Copy Text", command=copy)
label = Label()

# Specifying the placement of the Tkinter window
cv.grid(row=1, column=0, columnspan=4,padx=2)
check.grid(row=2, column=0, sticky=E+W+S+N)
clear.grid(row=2, column=1, sticky=E+W+S+N)
space.grid(row=2, column=2, sticky=E+W+S+N)
delete.grid(row=2, column=3, sticky=E+W+S+N)
label1.grid(row=3, column=0)
label2.grid(row=4, column=0, columnspan = 4)
clearSecond.grid(row=5, column=1,sticky=E+W,pady=2)
copy.grid(row=5, column=2,sticky=E+W,pady=2)
label.grid(row=6)
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)
cv.bind("<B1-Motion>", paint)

root.geometry("510x620+300+20") # initalize geometry and placement of the gui window
root.mainloop() # infinite loop to display gui window
