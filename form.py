import tkinter as tk
import os
import tkinter.filedialog
# import shutil for copping fileOBJ

i = 0

class ScrolledFrame(tk.Frame):

    def __init__(self, parent, vertical=True, horizontal=False):
        global ent1
        global ent2
        super().__init__(parent)

        self._canvas = tk.Canvas(self)
        self._canvas.grid(row=0, column=0)

        self._vertical_bar = tk.Scrollbar(self, orient="vertical", 
command=self._canvas.yview)
        if vertical:
            self._vertical_bar.grid(row=0, column=1, sticky="ns")
        self._canvas.configure(yscrollcommand=self._vertical_bar.set)

        self._horizontal_bar = tk.Scrollbar(self, orient="horizontal", 
command=self._canvas.xview)
        if horizontal:
            self._horizontal_bar.grid(row=1, column=0, sticky="we")
        self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

        self.frame = tk.Frame(self._canvas)
        self._canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", self.resize)

        btn1 = tkinter.Button(root, text="Source Path", command = call)
        btn1.pack(fill="both", expand=1)

        ent1 = tkinter.Entry(root)
        ent1.pack(fill="both", expand=1)

        # btn1 = tkinter.Button(root, text="destination",command = des)
        # btn1.pack(fill="bot   ", expand=1)

        # ent2 = tkinter.Entry(root)
        # ent2.pack(fill="both", expand=1)

        # cpy = tkinter.Button(root, text="Copy",command = copy_file)
        # cpy.pack(fill="x")


        self.pack()

    def resize(self, event=None): 
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))


#This is not in class    
def call():
     global filez
     global buttons
     global i


     buttons = []
     filez = tkinter.filedialog.askdirectory(parent=root,
     initialdir = "/",title='Choose a file')
     ent1.delete(0,"end") 
     ent1.insert(0, filez)  

     dirs = os.listdir(filez)


     # remove previous IntVars
     intvar_dict.clear()

     # remove previous Checkboxes      
     for cb in checkbutton_list:
        cb.destroy()
     checkbutton_list.clear()



     for filename in dirs:

         # create IntVar for filename and keep in dictionary
         intvar_dict[filename] = tk.IntVar()

         # create Checkbutton for filename and keep on list
         c = tk.Checkbutton(sf.frame, text=filename, 
variable=intvar_dict[filename])
         c.pack()
         checkbutton_list.append(c)
         buttons.append((intvar_dict[filename],filename))
     #check all
     if  i == 0:    
         var = tk.IntVar()
         c1 = tk.Checkbutton(root, text="select all", 
variable=var,command=select_all,activebackground='red',foreground='red')
         c1.pack(side="left")
         i = i + 1

# def des():
#     global destination

#     destination = tkinter.filedialog.askdirectory(parent=root, title='Choose a Path')
#     ent2.delete(0,"end")
#     ent2.insert(20, destination)

# def copy_file():
#     for key, value in intvar_dict.items():
#         if value.get() > 0:
#             src_path = filez +"//"+key
#             if (os.path.isfile(src_path)) == True: 
#                 shutil.copy(src_path,destination) 
#             elif (os.path.isdir(src_path)) == True:

#                  shutil.copytree(src_path,destination+"//"+key)
#             else:
#                 pass
#     for item in buttons:
#         v , n = item
#         if v.get():
#             v.set(0)


# def select_all(): # Corrected
#     for item in buttons:
#         v , n = item
#         if v.get():
#             v.set(0)
#         else:
#             v.set(1)            



root = tk.Tk()

intvar_dict = {}
checkbutton_list = []

sf = ScrolledFrame(root)

#call()

root.mainloop()