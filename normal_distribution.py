import random
import time
import matplotlib, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from Tkinter import *
import ttk


#root
root = Tk()
root.title("Medians and the Normal Distribution")

#mainframe
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

def create_list(sampleSize, upperLimit):
    numbList = []
    sampleSize = int(sample.get())
    upperLimit = int(upper.get())
    while sampleSize > 0:
        sampleSize -= 1
        randomNum = random.randrange(0,upperLimit+1)
        numbList.append(randomNum)
    numbList.sort(key=int)
    return numbList

def medians_variance(median_list):
    sum_of_medians = sum(median_list)
    variance = sum_of_medians / len(median_list)
    return variance


def median(numbList):

    srtd = sorted(numbList)
    mid = len(numbList)//2
    if len(numbList) % 2 == 0:
        return (srtd[mid-1] + srtd[mid]) / 2.0
    else:
        return srtd[mid]


def main():

    trials = int(number_lists.get())

    lists = []
    median_list = []

    binsize = 10

    for i in range(trials):
        lists.append(create_list(sampleSize, upperLimit))

    for current_list in lists:
        current_median = median(current_list)
        median_list.append(current_median)
        median_list.sort(key=float)


    p = f.gca()
    p.hist(median_list, binsize)
    p.set_xlabel('Median Value', fontsize = 15)
    p.set_ylabel('Frequency', fontsize = 15)
    canvas.show()
    time.sleep(2)
    f.clf()

    med = str(median(median_list))
    std = str(np.std(median_list))
    var = str((float(std)**2))

    #middle
    ttk.Label(mainframe, text = "Middle: ").grid(column = 5, row = 1, sticky = W)
    ttk.Label(mainframe, text = med).grid(column = 6, row = 1, sticky = W)

    #standard deviation
    ttk.Label(mainframe, text = "Standard Deviation: ").grid(column = 5, row = 2, sticky = W)
    ttk.Label(mainframe, text = std).grid(column = 6, row = 2, sticky = W)

    #variance
    ttk.Label(mainframe, text = "Variance: ").grid(column = 5, row = 3, sticky = W)
    ttk.Label(mainframe, text = var).grid(column = 6, row = 3, sticky = W)

#sampleSize Entry
sample = StringVar()
sampleSize = ttk.Entry(mainframe, width = 7, textvariable = sample)
sampleSize.grid(column = 2, row = 1, sticky =(W, N))

#upperLimit Entry
upper = StringVar()
upperLimit = ttk.Entry(mainframe, width = 7, textvariable = upper)
upperLimit.grid(column = 2, row = 2, sticky = (W, N))

#binsize Entry
Bin = StringVar()
binsize = ttk.Entry(mainframe, width = 7, textvariable = Bin)
binsize.grid(column = 2, row = 3, sticky = (W, N))

#sampleSize and upperLimit Labels
ttk.Label(mainframe, text="Sample Size ").grid(column = 1, row = 1, sticky = (W, N))
ttk.Label(mainframe, text="Upper Limit ").grid(column = 1, row = 2, sticky = (W, N))
ttk.Label(mainframe, text="Bin Size").grid(column = 1, row = 3, sticky = (N,W))

#canvas space
f = Figure(figsize=(6,6), dpi=100)
canvas = FigureCanvasTkAgg(f, master=mainframe)
canvas.get_tk_widget().grid(row=1, column=3, rowspan=10, sticky = (N,E))

#button for new histogram
button = ttk.Button(mainframe, text="New Histogram", command=main).grid(column=1, row=4, sticky=(N,W))

#scale
scale = StringVar()
number_lists = Scale(mainframe, from_=2, to=2000, orient=HORIZONTAL,length=600,variable = scale)
number_lists.grid(column = 3, row = 12, sticky= S)

for child in mainframe.winfo_children(): child.grid_configure(padx=2, pady=2)

sampleSize.focus()
upperLimit.focus()
root.bind('<Return>', main)

root.mainloop()
