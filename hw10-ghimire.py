# hw10.py
# Chris Monico, 3/19/21
# Graphical illustration of Newton's Method for functions
# from C to C.

'''
Structured coding process
i)
Let pixel coordinate be (0,0)
Let top left coordinates be 1+12i
Let pixel width and height be 0.4 and 0.3 

To find the center of coordinate (3,1)
Width is 0.4, 
So, (3-0)*0.4=1.2 added in real direction

Height is 0.3
So, (1-0)*0.3=0.3 subtracted in imaginary direction
Since, y-direction is opposite

S0, final coordiantes
=1+12i+1.2-.3i
=2.2+11.7i

ii)
Get the input coordinates of initial value
For x coordinate,
Extract the real value of given intital coordinate
Add That to the width of each pixel times the value of real value of new coordinate


For y coordinate,
Extract the imaginary value of given intital coordinate
Subtract that to the width of each pixel times the value of imaginary value of new coordinate

Finally the answer is real plus the imaginary value


iii)
Let pixel coordinate be (0,0)
Let top left coordinates be 2+5i
Let pixel width and height be 0.3 and 0.6 

To find the center of coordinate (5,3)

Width is 0.3, 
So, 
2 is real value
2+width(5)
2+0.3(5)
3.5


Height is 0.6
So,
5i is imaginary value
5-height(3)
5-0.6*3
3.2


So final answer is 3.5+3.2i


 add the input real value to the resulting coordinate real value









'''


import tkinter as tk
import cmath
import math



def Newton(Function, Derivative, z0, epsilon):
    x_curr=z0
    for i in range(0,20):
            
            fun=Function(x_curr)
            dev=Derivative(x_curr)
            
            #if y-value is near 0
            if epsilon>abs(fun):
                return x_curr
            
            #if value is close to 0 slope
            if epsilon>abs(dev):
                print("Error really close to zero slope") 
                return
            
            x_next=x_curr-(fun/dev)
            x_curr=x_next
        
    print("Failture to converge") 
    return


def colorFromRGB(r, g, b):
    # R, G, B are floating point numbers between 0 and 1 describing
    # the intensity level of the Red, Green and Blue components.
    X = [int(r*255), int(g*255), int(b*255)]
    for i in range(3):
        X[i] = min(max(X[i],0), 255)
    color = "#%02x%02x%02x"%(X[0],X[1],X[2])
    return color

def color_from_comp(z):
    x = z.real*2.7
    y = z.imag*2.7
    r = 0.5*(1.0 + math.tanh(x))
    g = 0.5*(1.0 + math.sin(x*y))
    b = 0.5*(1.0 + math.cos(x+y))
    return colorFromRGB(r, g, b)

def F(z):
    return z**5-1

def dF(z):
    return 5*z**4

#############################################################
class MyApplication(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.screen_width = 800
        self.screen_height = 600
        self.set_region(0+0j, 4)
        self.create_widgets()
        
    def set_region(self, center, region_width):
        # This sets the region of the complex plane to be displayed
        # on the canvas, by specifying the center and width of that region.
        # The height is then determined from the aspect ratio of the canvas.
        # Using those, we set the attributes:
        # self.pixel_width : complex width of each pixel,
        # self.pixel_height: complex height of each pixel
        # self.top_left : complex number at the center of the top-left pixel.
        self.pixel_width = region_width/(self.screen_width-1)
        region_height = self.screen_height * region_width/self.screen_width
        self.pixel_height = region_height / (self.screen_height - 1)
        x = center.real - self.pixel_width*(self.screen_width/2)
        y = center.imag + self.pixel_height*(self.screen_height/2)
        self.top_left = x + 1j*y

    def update_screen(self):
        self.master.update_idletasks()
        self.master.update()

    def create_widgets(self):
        # First, a Canvas widget that we can draw on. It will be 800 pixels wide,
        # and 600 pixels tall.
        self.canvas = tk.Canvas(self.master, width=self.screen_width, height=self.screen_height, background="white")
        # This 'pack' method packs it into the top-level window.        
        self.canvas.pack()

    def pixel_center(self, x, y) :
        # Return the complex number corresponding to the center of the
        # given pixel.
        # This is problem 2; delete the 'pass' statement and write this method.

        ans=self.top_left.real+self.pixel_width*x+(self.top_left.imag-self.pixel_height*y)*1j
        return ans
        


    def draw_pixel(self, x, y, C):
        self.canvas.create_rectangle(x-0.5, y-0.5, x+0.5, y+0.5, fill=C, outline="")

    def draw_newton_plot(self):
        for i in range(self.screen_width):
            for j in range(self.screen_height):
                z = self.pixel_center(i, j)
                root = Newton(F, dF, z, 0.00001)
                if type(root) is complex:
                    color = color_from_comp(root)
                else:
                    color="black"
                self.draw_pixel(i, j, color)
            if i%20 == 0:
                self.update_screen()



root = tk.Tk()
app = MyApplication(master=root)
app.draw_newton_plot()
app.mainloop()

