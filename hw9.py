# hw9.py
# Chris Monico, 3/15/21
# A simple example to demonstrate basic usage of tkinter.
# To complete the assignment, you only need to
# modify the draw() method; you don't need to make any
# other changes anywhere else in the code.

import tkinter as tk


# Define a class for our application,
# which inherits from tk.Frame.
class MyApplication(tk.Frame):
    ##########################################
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        # self.handle_list is to remember handles
        # to some of the things we draw,
        # so that we can erase them later.
        self.handle_list = []
        # Create all the widgets we want in
        # our window at the beginning.
        self.create_widgets()

    ##########################################
    def create_widgets(self):
        # Create the widgets we want our window to have at startup.

        # First, a Canvas widget that we can draw on.
        # It will be 800 pixels wide, and 600 pixels tall.
        self.canvas = tk.Canvas(self.master, width=800, height=800, background="yellow")
        # This 'pack' method packs it into the top-level window.        
        self.canvas.pack()

        

        # Create a button with label "Draw", which calls the member
        # function self.draw() below when it's activated.
        self.draw_button = tk.Button(text="Draw", command=self.draw)
        # Pack the button into the window.
        self.draw_button.pack()

        # Create another button, with label "Clear" which calls the
        # member function self.clear() when it's activated.
        self.clear_button = tk.Button(text="Clear", command=self.clear)
        self.clear_button.pack()
        
    def draw(self):
        #############################################
        # Add your code to this method. Be sure to  #
        # store the 'handles' in the same way as    #
        # the sample code, so that the objects      #
        # will be removed when the 'clear button'   #
        # is clicked.                               #
        # You can delete all of the existing code   #
        # that's in this method right now - it is   #
        # here just as an example of drawing some   #
        # things and storing the handles.           #
        #############################################

        # The canvas methods .create_XXXXX actually return
        # an internal name (integer) corresponding to each
        # object we create, called a 'handle. 
        # We will store those handles so that when the 'clear button'
        # is clicked, we can ask the canvas to remove them.


        # Draw a rectangle on the canvas. The first two arguments,
        # (250, 150) specify the upper-left hand corner of the rectangle,
        # the next two (550, 450) specify the lower-right hand corner.
        # 'fill' is an optional argument specifying the color that
        # the interior should be filled with. TKinter knows some
        # colors by string names, like "white", "blue", "red", ...
        # but we can specify any color using HTML color coding syntax 
        # as we do here:
        #800,600
        h = self.canvas.create_rectangle(100, 100, 700, 500, fill="#0000FF")
        self.handle_list.append(h)


        # Create/draw an oval on the canvas.
        # The first four numbers describe a bounding
        # box for the oval: (250, 150) is one corner,
        # and (550, 450) is another.
        #h = self.canvas.create_oval(120,120,680,480,fill="#D2B48C")
        #self.handle_list.append(h)

        h = self.canvas.create_line(200,200,200,400,fill="grey",width="5")
        self.handle_list.append(h)

        h = self.canvas.create_line(600,200,600,400,fill="grey",width="5")
        self.handle_list.append(h)

        h = self.canvas.create_line(200,400,300,450,fill="grey",width="5")
        self.handle_list.append(h)

        h = self.canvas.create_line(600,400,500,450,fill="grey",width="5")
        self.handle_list.append(h)

        h = self.canvas.create_line(300,450,500,450,fill="grey",width="5")
        self.handle_list.append(h)


        # Draw a bunch of lines.
        '''
        for n in range(0,300,20):
            # Create a line segment from (400, n) to (400+n, 300).
            h = self.canvas.create_line(400,n,400+n,300)
            self.handle_list.append(h)
            # Create a line segment from (400+n, 300) to (400, 600-n).
            h = self.canvas.create_line(400+n,300,400,600-n)
            self.handle_list.append(h)
            h = self.canvas.create_line(400,600-n,400-n,300)
            self.handle_list.append(h)
            h = self.canvas.create_line(400-n,300,400,n)
            self.handle_list.append(h)
        '''

        h = self.canvas.create_arc(195,280,605,120,start=0,extent=180,fill="black")
        self.handle_list.append(h)

        h = self.canvas.create_oval(250,230,350,270,fill="white")
        self.handle_list.append(h)

    
        h = self.canvas.create_oval(550,230,450,270,fill="white")
        self.handle_list.append(h)

        h = self.canvas.create_oval(280,240,320,260,fill="black")
        self.handle_list.append(h)

    
        h = self.canvas.create_oval(520,240,480,260,fill="black")
        self.handle_list.append(h)

        



        #h = self.canvas.create_line(400,275,355,350,fill="grey",width="5")
        #self.handle_list.append(h)

        #h = self.canvas.create_line(355,350,390,350,fill="grey",width="5")
        #self.handle_list.append(h)

        h = self.canvas.create_oval(335,380,465,420,fill="white")
        self.handle_list.append(h)

        h = self.canvas.create_line(335,400,465,400,fill="black",width="3")
        self.handle_list.append(h)

        h = self.canvas.create_polygon(400,275,355,350,430,350,400,275,fill="grey",outline="black",width="2")
        self.handle_list.append(h)


        h = self.canvas.create_rectangle(100, 600, 400, 790, fill="#0000FF")
        self.handle_list.append(h)

        h = self.canvas.create_polygon(120,740,120,650,140,650,140,680,120,680,fill="",outline="green",width="4")
        self.handle_list.append(h)

       

        h = self.canvas.create_line(170,740,170,700,fill="black",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(170,700,190,700,fill="black",width="4")
        self.handle_list.append(h)



        h = self.canvas.create_line(230,740,230,700,fill="yellow",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(230,700,210,700,fill="yellow",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(230,720,210,720,fill="yellow",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(210,720,210,740,fill="yellow",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(210,740,230,740,fill="yellow",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(250,740,250,700,fill="white",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(250,700,270,700,fill="white",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(270,700,270,740,fill="white",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(310,780,310,700,fill="orange",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(310,780,290,780,fill="orange",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_oval(306,660,318,675,fill="white")
        self.handle_list.append(h)

        
        h = self.canvas.create_line(350,740,350,700,fill="yellow",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(350,700,330,700,fill="yellow",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(350,720,330,720,fill="yellow",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(330,720,330,740,fill="yellow",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(330,740,350,740,fill="pink",width="4")
        self.handle_list.append(h)

        h = self.canvas.create_line(370,740,370,700,fill="pink",width="4")
        self.handle_list.append(h)


        h = self.canvas.create_line(370,740,390,740,fill="pink",width="4")
        self.handle_list.append(h)









       
       



        

    ##############################################
    def clear(self):
        # To clear the things we drew in the 'draw'
        # function, we just ask the canvas to delete them,
        # one at a time, by their handles.
        # You should not need to modify anythingin this method.
        while len(self.handle_list)>0:
            h = self.handle_list.pop()
            self.canvas.delete(h)


########################################
# Do not change anything below here!   #
########################################
# Instantiate the Tk class.
# This should only ever be done once in a program.
# Think of it as 'firing up' the library, getting it ready to do stuff.
root = tk.Tk()

# Create an instance of the MyApplication class we defined above.
app = MyApplication(root)

# Pass flow control over to the Tkinter library, so it can do things
# like wait for keyboard and mouse events, redraw the window when needed,...
# One of the things it will do is watch for buttons we created and invoke
# the 'callback functions' we gave them. It will run indefinitely,
# until the operating system sends it a 'quit' command (e.g.,
# if we close the window).
app.mainloop()
