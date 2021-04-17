# hw12.py
# Chris Monico, 4/6/2021
# Reminder: do NOT delete any of the comments and do NOT
# modify any code except in the methods neighbor_count() and next_gen()

import tkinter as tk
import math
import hashlib


"""
****************** Problem 1 ***********************

    00001101
    00001100
    00000000
    00100000
    00100000
    00000000
    00000000
    10001000

SCP Step I:
    Put your SCP Step I work for Problem 1 here.

    Cell  alive?  neighbours    

    0,0     0       2
    0,1     0       1
    0,2     0       0   
    0,3     0       3
    0,4     1       4


SCP Step II:
    Put your SCP Step II work for Problem 1 here.

    For every value of row and column, find the other 8 sorrounding neighbours
    To solve each row and column value,
    We must use formula:
    Rowindex starting from 0 % number of rows
    Columnindex starting from 0 % number of columns

    For eight neighbouring values, 
    find row+1 column+1 value    
    find row+1 column-1 value  
    find row column+1 value  
    find row column-1 value  
    find row-1 column+1 value  
    find row-1 column-1 value  
    find row-1 column value  
    find row+1 column value

    If the value is 1 increase the count of the number of neighbours starting from 0
  

SCP Step III:
    Put your SCP Step III work for Problem 1 here.

    Let the initial value be row 0 column 7
    Finding neighbouring values,

    find row+1 column+1 value   (1%8,8%8)   (1,0)   0         
    find row+1 column-1 value   (1%8,6%8)   (1,6)   0         
    find row column+1 value     (0%8,8%8)   (0,0)   0 
    find row column-1 value     (1%8,6%8)   (1,6)   0 
    find row-1 column+1 value   (-1%8,8%8)   (7,0)   1 
    find row-1 column-1 value   (-1%8,6%8)   (7,6)   0 
    find row-1 column value     (-1%8,7%8)   (7,7)   0 
    find row+1 column value     (1%8,7%8)   (1,7)   0 

    Therefore the number of neighbours is one




***************** Problem 2 ************************
SCP Step I:
    Put your SCP Step I work for Problem 2 here.


    Cell  alive?  neighbours    Condition if alive      Condition if dead      Result after t+1

    0,0     0       2              2 or 3                   Not 3                   0
    0,1     0       1              0 or 1                   Not 3                   0
    0,2     0       0              0 or 1                   Not 3                   0
    0,3     0       3              2 or 3                   Exactly 3               1
    0,4     1       4              4 or more                Not 3                   0

    

SCP Step II:
    Put your SCP Step II work for Problem 2 here.

    Initialize empty 2d array with total no of rows and columns starting from 0

    Go through the initial board over each cell and check following condition based on no of neighbours:
    
    If cell is alive
        dead at time t + 1 if it has 0 or 1 live neighbors
        alive at time t + 1 if it has 2 or 3 live neighbors
        dead at time t + 1 if it has 4 or more live neighbors
    
    If cell is dead
        alive at time t + 1 if it has exactly 3 live neighbors
        dead otherwise

    Based on results update the new 2d array and save it to the empty 2d array
    After finishing the matrix update board to it


SCP Step III:
    Put your SCP Step III work for Problem 2 here.
    Let inital board be
    0000
    1000
    0001
    0000

    Initilize empty array
    0000
    0000
    0000

    At (0,0) 1 neighbour and dead so result is dead
    At (0,1) 1 neighbour and dead so result is dead
    At (0,2) 0 neighbour and dead so result is dead
    At (0,3) 1 neighbour and dead so result is dead

    
    At (1,0) 1 neighbour and alive so result is dead
    At (1,1) 1 neighbour and dead so result is dead
    At (1,2) 1 neighbour and dead so result is dead
    At (1,3) 2 neighbour and dead so result is dead

    At (2,0) 2 neighbour and dead so result is dead
    At (2,1) 1 neighbour and dead so result is dead
    At (2,2) 1 neighbour and dead so result is dead
    At (2,3) 1 neighbour and alive so result is dead

    At (3,0) 1 neighbour and dead so result is dead
    At (3,1) 0 neighbour and dead so result is dead
    At (3,2) 1 neighbour and dead so result is dead
    At (3,3) 1 neighbour and alive so result is dead

    Therefore the new updated board is
    
    0000
    0000
    0000
    0000



"""



###########################################################
class GOL:
    #######################################################
    # This assignment is copyright (c) 2021, Chris Monico.
    # You may NOT redistribute this code or any derivative works thereof,
    # except for the purposes of regular assignment submission in this course.
    # In particular, you may NOT upload it to any external websites,
    # including Stackexchange, Chegg, or any external websites whatsoever.
    #######################################################
    def __init__(self, filename):
        self.board = None
        self.rows = 0
        self.cols = 0
        self.i = hashlib.md5(b'This Assignment is copyrighted and may NOT be redistributed!')
        if self.load_board(filename) == False:
            print("Failed to load board from file '{0}'...bailing.".format(filename))
            exit(-1)

    #######################################################
    def load_board(self, filename):
        try:
            infile = open(filename, "r")
        except:
            print("Could not open file '%s' for reading!" % (filename))
            return False
        i = 0 # This will be the index of the row we're currently reading from file.
        # We will first read the board into a dictionary, then convert it
        # to a list of lists.
        h = self.i
        board_dict = {}
              
        for line in infile:
            thisRow = line.strip() # Removing trailing newline character.
            N = len(thisRow)
            # Bookkeeping: the grid size will be the minimum necessary
            # to accomodate all of the nonempty lines.
            if N>self.cols:
                self.cols = N
            if N>0:
                self.rows = i+1
            for j in range(N):
                board_dict[i,j] = int(thisRow[j])
            i += 1

        infile.close()
        # Check that the board_dict contains all necessary entries; set any missing
        # entries to zero.
        for i in range(self.rows):
            for j in range(self.cols):
                if not( (i,j) in board_dict):
                    board_dict[i,j] = 0
        self.generation = 1
        self.j = h.hexdigest()
        # Now convert it to a list of lists:
        self.board = [[board_dict[i,j] for j in range(self.cols)] for i in range(self.rows)]
        return True

    ###############################################################
    def neighbor_count(self, i, j):
        count=0
        if self.board[(i+1)%self.numRows()][j]==1:
            count+=1
        if self.board[(i-1)%self.numRows()][j]==1:
            count+=1

        if self.board[i][(j+1)%self.numCols()]==1:
            count+=1
        
        if self.board[i][(j-1)%self.numCols()]==1:
            count+=1
        
        if self.board[(i-1)%self.numRows()][(j+1)%self.numCols()]==1:
            count+=1
        
        if self.board[(i-1)%self.numRows()][(j-1)%self.numCols()]==1:
            count+=1
        
        if self.board[(i+1)%self.numRows()][(j+1)%self.numCols()]==1:
            count+=1
        
        if self.board[(i+1)%self.numRows()][(j-1)%self.numCols()]==1:
            count+=1
        
        return count

    ###############################################################
    def next_gen(self):
            newBoard = [[0 for j in range(self.numCols())] for i in range(self.numRows())]
            for i in range(self.numRows()): 
                for j in range(self.numCols()):
                    if self.board[i][j]==1:
                        if self.neighbor_count(i,j)==0 or self.neighbor_count(i,j)==1:
                            newBoard[i][j]=0
                        elif self.neighbor_count(i,j)==2 or self.neighbor_count(i,j)==3:
                            newBoard[i][j]=1
                        else:
                            newBoard[i][j]=0
                    else:
                        if self.neighbor_count(i,j)==3:
                            newBoard[i][j]=1
                        else:
                            newBoard[i][j]=0
       

            self.board=newBoard

    ###############################################################
    def numRows(self):
        return self.rows

    ###############################################################
    def numCols(self):
        return self.cols

    ###############################################################
    def isAlive(self, row, col):
        if (row>=0) and (row<self.rows) and (col>=0) and (col<self.cols):
            if self.board[row][col]==1:
                return True
        return False

    ###############################################################
    def generation(self):
        return self.generation

   
##################################################################
class MyApplication(tk.Frame):
    def __init__(self, master, centerX, centerY, width, height):
        super().__init__(master)
        self.master = master
        self.G = GOL("input.txt")
        self.create_widgets()

        

    ###############################################################
    def create_widgets(self):
        self.canvasW = 800
        self.canvasH = 600
        self.h = int(self.G.j,base=16) % self.canvasW 
        self.w = tk.Canvas(self.master, width=self.canvasW, height=self.canvasH)
        self.w.pack()
        
        tk.Button(text="Advance 1 generation", command=lambda:self.drawScreen(1)).pack()
        tk.Button(text="Advance 10 generations", command=lambda:self.drawScreen(10)).pack()
        self.drawScreen(0) # Draw the first generation


    ###############################################################
    def update_screen(self):
        self.master.update_idletasks()
        self.master.update()

    ###############################################################
    def clear_screen(self, color):
        # First destroy the previous canvas widget to free up the
        # associated memory.
        self.w.destroy()
        self.w = tk.Canvas(self.master, width=self.canvasW, height=self.canvasH)
        self.w.pack()
        # Now fill the entire screen with a solid color
        self.w.create_rectangle(0,0,self.canvasW-1,self.canvasH-1,fill=color)

    ###############################################################
    def draw_grid(self, rowHeights, columnWidths, color):
        W = self.canvasW
        H = self.canvasH
        # First draw the vertical lines
        c=1
        while (c < W):
            self.w.create_line(c,0,c,H-1,fill=color)
            c += columnWidths
        # Now the horizontal
        r=0
        while (r<H):
            self.w.create_line(0,r,W-1,r,fill=color)
            r += rowHeights

    ###############################################################
    def label_screen(self, color, label):
        self.w.create_text(0, 0, text=label,anchor="nw",fill=color) 
        
    ###############################################################
    def plotPoint(self,x, y, color):
        self.w.create_rectangle(x-0.5, y-0.5, x+0.5, y+0.5, fill=color,outline=color)

    ###############################################################
    def plotCell(self, r, c, height, width,color):
        padW = 0.1*width
        padH = 0.1*height
        self.w.create_oval(c*width+padW, r*height+padH, (c+1)*width-padW, (r+1)*height-padH, fill=color,outline=color)

    ###############################################################
    def pixelW(self):
        # Gives the width of each pixel in Cartesian coordinates.
        return (self.BR_x - self.TL_x)/float(self.cavasW)

    ###############################################################
    def pixelH(self):
        # Gives the height of each pixel in Cartesian coordinates.
        return (self.TR_y - self.BL_y)/float(self.canvasH)

    ###############################################################
    def canvas_width(self):
        return self.canvasW

    ###############################################################
    def canvas_height(self):
        return self.canvasH

    ###############################################################
    def drawScreen(self, n):
        # This function redraws the Game of Life screen. If n=0,
        # the screen is just drawn once. But if n > 0, we will
        #      (1) update the GOL once,
        #      (2) redraw the screen,
        # and repeat these steps n-1 more times (e.g., n times total).

        w = self.canvas_width()
        h = self.canvas_height()
        self.ar = self.ag = self.ab = int(self.h==0x24d)
        
        r = self.G.numRows()
        c = self.G.numCols()
        if (r <=0) or (c <=0):
            return # There's nothing to draw!

        # Figure out how wide each row and column should be to
        # fit nicely in the window.
        rowheight = h/r
        colwidth  = w/c
        aliveColor = colorFromRGB(self.ar, self.ag, self.ab)
        deadColor = colorFromRGB(0.0, 0.0, 0.0)
        gridColor = colorFromRGB(0,0,1.0)

        done = False
        updates = 0
        while not(done):
            if (updates < n):
                self.G.next_gen()
                self.G.generation += 1
                updates += 1
            self.clear_screen(deadColor)
            self.draw_grid(rowheight, colwidth, gridColor)
            for j in range(c):
                for i in range(r):
                    if self.G.isAlive(i,j):
                        self.plotCell(i, j, rowheight, colwidth, aliveColor)
            self.update_screen()
        
            # Draw the generation label on the screen.
            genColor = colorFromRGB(1.0, 0.5, 0.5)
            self.label_screen(genColor, "Generation: "+str(self.G.generation))
            if updates >= n:
                done = True
 
########################################################
def colorFromRGB(r, g, b):
    # R, G, B are floating point numbers between 0 and 1 describing
    # the intensity level of the Red, Green and Blue components.
    X = [int(r*255), int(g*255), int(b*255)]
    for i in range(3):
        if X[i]<0:
            X[i] = 0
        if X[i]>255:
            X[i]=255
    color = "#%02x%02x%02x"%(X[0],X[1],X[2])
    return color



####################
#      Main        #
####################
root = tk.Tk()
app = MyApplication(root,0,0,4,3)
app.mainloop()
