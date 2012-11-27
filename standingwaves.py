# Justin Svegliato
from Tkinter import *
from math import sin, cos, degrees, radians, pi
import time

def drange(start, stop, step):
  r = start
  while r < stop:
    yield r
    r += step

class Application(Frame):
  animation = False
  loop = True
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.createWidgets()
    
  def createWidgets(self):
    self.simulation = Frame(self, bg = 'lightgray')
 
    self.controls = LabelFrame(self.simulation, text = 'Controls',
                               bg = 'lightgray')
    self.controls.grid(column = 1)
    
    self.quantum_number_label = Label(self.controls, text = 'Quantum Number', 
                                      anchor = W,  justify = LEFT, bg = 'lightgray')
    self.quantum_number_label.grid(row = 1, column = 1)

    self.quantum_number_input = Entry(self.controls, highlightbackground = 'lightgray')
    self.quantum_number_input.insert(0, "12")
    self.quantum_number_input.grid(row = 1, column = 2)
    self.quantum_number_input.bind("<Button-1>", self.stopAnimation)
    self.quantum_number_input.bind("<Key>", self.stopAnimation)

    #self.precision_label = Label(self.controls, text = 'Precision', 
                                 #anchor = W, justify = LEFT, bg = 'lightgray')
    #self.precision_label.grid(row = 1, column = 3) 

    #self.precision_input = Entry(self.controls, highlightbackground = 'lightgray')
    #self.precision_input.grid(row = 1, column = 4)
    #self.precision_input.insert(0, '.01')
    #self.precision_input.bind("<Button-1>", self.stopAnimation)

    self.shift = IntVar()
    self.shift_button = Checkbutton(self.controls, text="Shift", variable=self.shift,
                                    bg='lightgray')
    self.shift_button.grid(row = 1, column = 5)
    self.shift_button.bind("<Button-1>", self.stopAnimation)

    self.calculate_button = Button(self.controls, text = 'Simulate',
                                   command = self.execute, 
                                   highlightbackground = 'lightgray')
    self.calculate_button.grid(row = 1, column = 6)

    self.canvas = Canvas(self.simulation, width = 550, height = 550, 
                         highlightbackground = 'lightgray', bg = 'lightgray')
    self.canvas.grid(row = 2, column = 1)

    self.simulation.pack(side = 'left')
  
  def stopAnimation(self, event):
    self.animation = False
    self.loop = True

  def execute(self):
    quantum_number = int(self.quantum_number_input.get())
    if quantum_number > 0 and quantum_number < 21:
      self.animation = True
      self.calculate()  

  def calculate(self):
    quantum_number = int(self.quantum_number_input.get())
    #step = float(self.precision_input.get()) 
    for amplitude in range(-50, 50, 3) + range(50, -50, -3):
      for theta in drange(0, 2, .008):### step):
        r = amplitude * sin(quantum_number * pi * theta) + 200
        y = sin(pi * theta) * r
        x = cos(pi * theta) * r
        self.canvas.create_line(280 + x, 280 + y, 282 + x, 282 + y, fill='red')
      self.simulation.update_idletasks()
      self.canvas.delete(ALL)
    
def main():
  app = Application()
  app.master.title("Electron Orbital Simulator")
  def render():
    if app.animation and app.loop:
      app.loop = False
      app.calculate()
      app.loop = True
    app.after(1, render)
  app.after(2000, render()) 
  app.mainloop()
  
if __name__ == "__main__":
  main()
