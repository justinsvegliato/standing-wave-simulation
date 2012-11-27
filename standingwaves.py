# Justin Svegliato
from Tkinter import *
from math import sin, cos, degrees, radians, pi, pow, ceil
import time

class Application(Frame):
  animation = False
  loop = True
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.createWidgets()
    
  def createWidgets(self):
    self.simulation = Frame(self, bg = 'lightgray')
 
    self.controls = LabelFrame(self.simulation, text = 'Controls', bg = 'lightgray')
    self.controls.grid(column = 1, columnspan = 3)
    
    self.initial_quantum_number_label = Label(self.controls, text = 'Quantum Numbers', 
                                              anchor = W, justify = LEFT, bg = 'lightgray')
    self.initial_quantum_number_label.grid(row = 1, column = 1)

    self.initial_quantum_number_input = Entry(self.controls, 
                                              highlightbackground = 'lightgray')
    self.initial_quantum_number_input.grid(row = 1, column = 2)
    self.initial_quantum_number_input.bind("<Button-1>", self.reset)
    self.initial_quantum_number_input.bind("<Key>", self.reset)
    
    self.next_quantum_number_input = Entry(self.controls, highlightbackground = 'lightgray')
    self.next_quantum_number_input.grid(row = 1, column = 3)
    self.next_quantum_number_input.bind("<Button-1>", self.reset)
    self.next_quantum_number_input.bind("<Key>", self.reset)

    self.calculate_button = Button(self.controls, text = 'Simulate', command = self.execute, 
                                   highlightbackground = 'lightgray')
    self.calculate_button.grid(row = 1, column = 4)
    
    self.initial_energy = StringVar()
    self.initial_energy.set("")
    self.initial_quantum_number_energy_label = Label(self.simulation, 
    																								 textvariable = self.initial_energy, 
    																								 bg = 'lightgray')
    self.initial_quantum_number_energy_label.grid(row = 2, column = 1)
                                             			 
    self.energy_difference = StringVar()
    self.energy_difference.set("")
    self.energy_difference_label = Label(self.simulation, 
    																		 textvariable = self.energy_difference, 
                                         bg = 'lightgray')
    self.energy_difference_label.grid(row = 2, column = 2)
                                          
    self.next_energy = StringVar()
    self.next_energy.set("")
    self.next_quantum_number_energy_label = Label(self.simulation, 
                           												textvariable = self.next_energy, 
                           												bg = 'lightgray')
    self.next_quantum_number_energy_label.grid(row = 2, column = 3) 
                               								
    self.simulation_canvas = Canvas(self.simulation, width = 550, height = 550, 
    																bg = 'lightgray', highlightbackground = 'lightgray')
    self.simulation_canvas.grid(row = 4, column = 1, columnspan = 3)

    self.simulation.grid(columnspan = 3)
  
  def reset(self, event):
    self.animation = False
    self.loop = True   
    self.initial_energy.set("")
    self.next_energy.set("")
    self.energy_difference.set("")

  def execute(self):
    initial_quantum_number = self.initial_quantum_number_input.get()
    next_quantum_number = self.next_quantum_number_input.get()
    if initial_quantum_number != "" and \
       int(initial_quantum_number) > 0 and \
       int(initial_quantum_number) < 21:
      if (next_quantum_number != "" and \
          int(next_quantum_number) > 0 and \
          int(next_quantum_number) < 21) or \
          next_quantum_number == "":
        initial_energy_value = ceil(-13.60 / pow(int(initial_quantum_number), 2) * 100) / 100
        self.initial_energy.set("Initial: " + str(initial_energy_value) + " eV")
        if next_quantum_number == "":
          self.next_energy.set("")
          self.energy_difference.set("")
        else:
          next_energy_value = ceil(-13.60 / pow(int(next_quantum_number), 2) * 100) / 100
          self.next_energy.set("New: " + str(next_energy_value) + " eV")
          difference = ceil((initial_energy_value - next_energy_value) * 100) / 100
          self.energy_difference.set("Difference: " + str(difference) + " eV")
        self.animation = True
        self.drawCanvas() 

  def drawCanvas(self):
    quantum_numbers = [] 
    quantum_numbers.append(int(self.initial_quantum_number_input.get())) 
    if self.next_quantum_number_input.get() != "": 
      quantum_numbers.append(int(self.next_quantum_number_input.get())) 
      
    if len(quantum_numbers) == 1: 
      self.drawWaves(quantum_numbers, 50, 200, (270, 290)) 
    elif len(quantum_numbers) == 2: 
      self.drawWaves(quantum_numbers, 30, 100, (140, 250))
   
  def drawWaves(self, quantum_numbers, max_amp, initial_radius, (x_origin, y_origin)):
    amplitudes = range(-max_amp, max_amp, 3) + range(max_amp, -max_amp, -3)
    for amplitude in amplitudes:
      def drange(start, stop, step):
        r = start
        while r < stop:
          yield r
          r += step
      thetas = drange(0, 2, .008)   
      for theta in thetas:
        i = 0
        for quantum_number in quantum_numbers:
          offset = ((2 * initial_radius) + (max_amp * 2)) * i
          position = (x_origin + offset, y_origin)
          self.plot_point(quantum_number, amplitude, theta, initial_radius, position)
          i += 1        
      self.simulation.update_idletasks()
      self.simulation_canvas.delete(ALL) 
      
  def plot_point(self, quantum_number, amplitude, theta, initial_radius, (x_origin, y_origin)):
    r = amplitude * sin(quantum_number * pi * theta) + initial_radius
    x_offset = cos(pi * theta) * r
    y_offset = sin(pi * theta) * r
    x = x_origin + x_offset
    y = y_origin + y_offset
    self.simulation_canvas.create_line(x, y, x + 2, y + 2, fill='red')
    
def main():
  app = Application()
  app.master.title("Electron Orbital Simulator")
  def render():
    if app.animation and app.loop:
      app.loop = False
      app.drawCanvas()
      app.loop = True
    app.after(1, render)
  app.after(2000, render()) 
  app.mainloop()
  
if __name__ == "__main__":
  main()