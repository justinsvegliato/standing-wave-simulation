# Justin Svegliato
from Tkinter import *
import time
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
    self.configure(bg = 'lightgray')
    self.simulation = Frame(self)
 
    self.controls = LabelFrame(self.simulation, text = 'Controls')
    self.controls.grid(column = 1)

    self.quantum_number_label = Label(self.controls, text = 'Quantum Number')
    self.quantum_number_input = Entry(self.controls)
    self.quantum_number_label.grid(row = 1, column = 1)
    self.quantum_number_input.grid(row = 2, column = 1)

    self.calculate_button = Button(self.controls,
                                   text = 'Create',
                                   command = self.calculate)
    self.calculate_button.grid(row = 3, column = 1)

    self.canvas = Canvas(self.simulation, width = 550, height = 550)
    self.canvas.grid(column = 2)

    self.simulation.pack(side = 'left')

  def calculate(self):
    self.point = PhotoImage(file = "images/point.gif")
    for  i in drange(0, 2, .001):
      quantum_number = float(self.quantum_number_input.get())
      r = 50 * sin(quantum_number * i * pi) + 190
      y = sin(i * pi) * r
      x = cos(i * pi) * r
      self.canvas.create_image(280 + -x, 280 + -y, image = self.point)     
      self.canvas.create_image(280 + x, 280 + y, image = self.point)
    
def main():
  app = Application()
  app.master.title("Standing Waves")
  app.mainloop()
  
if __name__ == "__main__":
  main()
