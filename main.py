import sys

import matplotlib.pyplot as plt
from Population import *
from tkinter import *
from tkinter import ttk, messagebox


def start():
    population = Population()
    population.initialize_population()
    counter = population.start_simulation()
    maxpoints = population.get_maxpoints()
    avgpoints = population.get_avgpoints()
    plt.plot([i for i in maxpoints.keys()], [i for i in maxpoints.values()])
    plt.plot([i for i in avgpoints.keys()], [i for i in avgpoints.values()])
    plt.axis((0,counter, 0, max(maxpoints.values())))
    plt.ylabel('Fitness')
    plt.xlabel('Generation Number')
    plt.show()
    root.destroy()



root = Tk()
root.title("Genetic Algorithm")
root.geometry("400x250")
frm = ttk.Frame(root, padding=90)


frm.grid()
ttk.Label(frm, text="Generate!").grid(column=0, row=0)
ttk.Button(frm, text="Start", command=start).grid(column=0, row=1)
ttk.Label(frm, text="        ",background='blue').grid(column=0, row=2)
ttk.Label(frm, text="max values").grid(column=1, row=2)
ttk.Label(frm, text="        ",background='orange').grid(column=0, row=3)
ttk.Label(frm, text="average values").grid(column=1, row=3)
root.mainloop()
