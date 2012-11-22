# Justin Svegliato
from Tkinter import *
from math import sin, cos, degrees, radians, pi
<<<<<<< HEAD
import time
import threadpool
=======
>>>>>>> 090cad47d8f58190d41b5cc7a2df265d7428c3e3

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
<<<<<<< HEAD
=======
    self.configure(bg = 'lightgray')
    #self.grid(padx = 20, pady = 20)
>>>>>>> 090cad47d8f58190d41b5cc7a2df265d7428c3e3
    self.simulation = Frame(self, bg = 'lightgray')
 
    self.controls = LabelFrame(self.simulation, text = 'Controls',
                               bg = 'lightgray')
    self.controls.grid(column = 1)

    self.quantum_number_label = Label(self.controls, text = 'Quantum Number', 
                                      anchor = W,  justify = LEFT, bg = 'lightgray')
    self.quantum_number_input = Entry(self.controls, highlightbackground = 'lightgray')
    self.quantum_number_label.grid(row = 1, column = 1)
    self.quantum_number_input.grid(row = 1, column = 2)
<<<<<<< HEAD

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

=======

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

>>>>>>> 090cad47d8f58190d41b5cc7a2df265d7428c3e3
    self.canvas = Canvas(self.simulation, width = 550, height = 550, 
                         highlightbackground = 'lightgray', bg = 'lightgray')
    self.canvas.grid(row = 2, column = 1)

    self.simulation.pack(side = 'left')

  def calculate(self):
<<<<<<< HEAD
    quantum_number = float(self.quantum_number_input.get())
    step = float(self.precision_input.get()) 
    for amplitude in range(-50, 50, 3) + range(50, -50, -3):
      for theta in drange(0, 2, step):
        r = amplitude * sin(quantum_number * pi * theta) + 200
        y = sin(pi * theta) * r
        x = cos(pi * theta) * r
        self.canvas.create_line(280 + x, 280 + y, 281 + x, 281 + y, width = .001)
      self.simulation.update_idletasks()
      self.canvas.delete(ALL)

=======
    self.point = PhotoImage(file = "images/point.gif")
    for  i in drange(0, 2, float(self.precision_input.get())):
      quantum_number = float(self.quantum_number_input.get())
      r = 50 * sin(quantum_number * i * pi) + 200
      y = sin(i * pi) * r
      x = cos(i * pi) * r
      self.canvas.create_image(280 + -x, 280 + -y, image = self.point)     
      self.canvas.create_image(280 + x, 280 + y, image = self.point)
    
>>>>>>> 090cad47d8f58190d41b5cc7a2df265d7428c3e3
def main():
  app = Application()
  app.master.title("Electron Orbital Simulator")
  app.mainloop()
  
if __name__ == "__main__":
  main()
