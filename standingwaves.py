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
    self.quantum_number_input = Entry(self.controls, highlightbackground = 'lightgray')
    self.quantum_number_label.grid(row = 1, column = 1)
    self.quantum_number_input.grid(row = 1, column = 2)

    self.precision_label = Label(self.controls, text = 'Precision', 
                                 anchor = W, justify = LEFT, bg = 'lightgray')
    self.precision_input = Entry(self.controls, highlightbackground = 'lightgray')
    self.precision_label.grid(row = 1, column = 3) 
    self.precision_input.grid(row = 1, column = 4)
    self.precision_input.insert(0, '.001')

    self.calculate_button = Button(self.controls, text = 'Create',
                                   command = self.calculate, 
                                   highlightbackground = 'lightgray')
    self.calculate_button.grid(row = 1, column = 5)

    self.precision_label = Label(self.controls, text = 'Precision', 
                                 anchor = W, justify = LEFT, bg = 'lightgray')
    self.precision_input = Entry(self.controls, highlightbackground = 'lightgray')
    self.precision_label.grid(row = 1, column = 3) 
    self.precision_input.grid(row = 1, column = 4)
    self.precision_input.insert(0, '.001')

    self.calculate_button = Button(self.controls, text = 'Create',
                                   command = self.calculate, 
                                   highlightbackground = 'lightgray')
    self.calculate_button.grid(row = 1, column = 5)

    self.canvas = Canvas(self.simulation, width = 550, height = 550, 
                         highlightbackground = 'lightgray', bg = 'lightgray')
    self.canvas.grid(row = 2, column = 1)

    self.simulation.pack(side = 'left')

  def calculate(self):
    quantum_number = float(self.quantum_number_input.get())
    step = float(self.precision_input.get()) 
    for amplitude in range(-50, 50, 3) + range(50, -50, -3):
      for theta in drange(0, 2, step):
        r = amplitude * sin(quantum_number * pi * theta) + 200
        y = sin(pi * theta) * r
        x = cos(pi * theta) * r
        self.canvas.create_line(280 + x, 280 + y, 281 + x, 281 + y)
      self.simulation.update_idletasks()
      self.canvas.delete(ALL)

    
def main():
  app = Application()
  app.master.title("Electron Orbital Simulator")
  app.mainloop()
  
if __name__ == "__main__":
  main()
