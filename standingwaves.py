# Justin Svegliato
from Tkinter import *
from math import sin, cos, degrees, radians, pi

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
    #self.grid(padx = 20, pady = 20)
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

    self.canvas = Canvas(self.simulation, width = 550, height = 550, 
                         highlightbackground = 'lightgray', bg = 'lightgray')
    self.canvas.grid(row = 2, column = 1)

    self.simulation.pack(side = 'left')

  def calculate(self):
    self.point = PhotoImage(file = "images/point.gif")
    for  i in drange(0, 2, float(self.precision_input.get())):
      quantum_number = float(self.quantum_number_input.get())
      r = 50 * sin(quantum_number * i * pi) + 200
      y = sin(i * pi) * r
      x = cos(i * pi) * r
      self.canvas.create_image(280 + -x, 280 + -y, image = self.point)     
      self.canvas.create_image(280 + x, 280 + y, image = self.point)
    
def main():
  app = Application()
  app.master.title("Electron Orbital Simulator")
  app.mainloop()
  
if __name__ == "__main__":
  main()
