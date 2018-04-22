from Tkinter import *
import ttk

from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
from snow_clearance import snow_clearance


def find_paths(*args):
    try:
        k = int(vehicles.get())
        place= location.get()
        pp_1 = int(pp1.get())
        pp_2 = int(pp2.get())
        
        print(place)
        d=snow_clearance(k,place,pp_1,pp_2)
        paths.set('1,2,3,4,5,6,7,8,9,10')
    
    except ValueError:
        k=3
        l="Rutgers University"
        pass
def close_window():
    root.destroy()

root = Tk()
root.title("Snow Clearance")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

location = StringVar()
vehicles = StringVar()
pp1 = StringVar()
pp2 = StringVar()
paths = StringVar()

#location_entry = ttk.Entry(mainframe, width=7, textvariable=location)
#location_entry.grid(column=2, row=1, sticky=(W, E))

vehicles_entry = ttk.Entry(mainframe, width=3, textvariable=vehicles)
vehicles_entry.grid(column=2, row=2, sticky=(W, E))

pp1_entry = ttk.Entry(mainframe, width=3, textvariable=pp1)
pp1_entry.grid(column=3, row=4, sticky=(W, E))

pp2_entry = ttk.Entry(mainframe, width=3, textvariable=pp2)
pp2_entry.grid(column=5, row=4, sticky=(W, E))

ttk.Label(mainframe, textvariable=paths).grid(column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Find Paths", command=find_paths).grid(column=1, row=6, sticky=W)
ttk.Button(mainframe, text="Close", command=close_window).grid(column=1, row=7, sticky=W)

choices = { "Rutgers University","Manhattan Island, New York","Princeton University"}
location.set("Rutgers University") # set the default option

popupMenu = OptionMenu(mainframe, location, *choices)
popupMenu.grid(row = 1, column =2, columnspan=5, sticky=W)

ttk.Label(mainframe, text="location").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="vehicles").grid(column=1, row=2, sticky=W)
#ttk.Label(mainframe, text="paths").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Priority Path:").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Start").grid(column=2, row=4, sticky=W)
ttk.Label(mainframe, text="End").grid(column=4, row=4, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

vehicles_entry.focus()
root.bind('<Return>', find_paths)
mainloop()
