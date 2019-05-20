import csv
import os
from tkinter import filedialog
from tkinter import messagebox
import shutil
import uuid

filename =  filedialog.askopenfilename(initialdir = "/",title = "Selecciona archivo",filetypes = (("csv","*.csv"),("all files","*.*")))
idx = uuid.uuid1()
try:
   with open(filename, mode="r") as f:
      dialect = csv.Sniffer().sniff(f.read(1024), delimiters=",:")
      f.seek(0)
      reader = csv.reader(f, dialect, quoting=csv.QUOTE_NONE)
      tmp_table = '{}.tmp'.format(filename)
      with open (tmp_table, mode="w")as w:
         writer = csv.writer(w, delimiter=";", quoting=csv.QUOTE_NONE)
         writer.writerows(reader)
   shutil.copy(filename, '{}_respaldo_{}'.format(filename,idx))
   os.remove (filename)
   os.rename (tmp_table, filename)



   messagebox.showinfo("Cambio de separador", "La modificación se realizó correctamente.")

   os.system("notepad {}".format(filename))
except:
   messagebox.showinfo("Cambio de separador", "No se pudo realizar la modificación, contactese con soporte.")
   os.system("notepad {}".format(filename))

