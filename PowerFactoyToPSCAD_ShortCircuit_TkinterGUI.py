# Leo Fitzgerald 24.03.2025

# Convert PowerFactory Grid Short Circuit to PSCAD Input Format

# Tkinter GUI equivalent of SourceModelling.py in same res folder 

# To do: include PPS/NPS/ZPS Ratios from PowerFactory


from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
import tkinter.font
import math
from tkinter import messagebox



class PowerFactoryToPSCAD_ShortCircuit():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('890x350')
            self.w1.configure(bg="#414141")
            self.w1.title("PowerFactory to PSCAD Short Circuit Tool")
        else:
            self.w1 = Frame(parent)
            self.w1 = Frame(parent, bg="#414141")
            self.w1.place(x = 0, y = 0, width = 890, height = 350)
        self.text_output_R0ohm_copy = Entry(self.w1, font = tkinter.font.Font(family = "Calibri", size = 9), state = "disabled", bg="#414141", fg="white")
        self.text_output_R0ohm_copy.place(x = 3020, y = 970, width = 110, height = 22)
        self.group1 = LabelFrame(self.w1, text = "Input from PowerFactory", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", bg="#414141", fg="white")
        self.group1.place(x = 10, y = 10, width = 870, height = 110)
        self.text_input_Vline = Entry(self.group1, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_input_Vline.place(x = 90, y = 30, width = 110, height = 22)
        self.text_input_Vline.insert(INSERT, "11")
        self.label1_VLL = Label(self.group1, text = "V Line-Line ", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_VLL.place(x = 10, y = 30, width = 80, height = 22)
        self.label_kV = Label(self.group1, text = "kV", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_kV.place(x = 210, y = 30, width = 30, height = 22)
        self.text_input_Isc3P = Entry(self.group1, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_input_Isc3P.place(x = 340, y = 0, width = 110, height = 22)
        self.text_input_Isc3P.insert(INSERT, "21")
        self.label_Isc3P = Label(self.group1, text = "Ikss3P", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Isc3P.place(x = 270, y = 0, width = 70, height = 22)
        self.label_Ikss3P = Label(self.group1, text = "kA", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Ikss3P.place(x = 460, y = 0, width = 30, height = 22)
        self.text_input_Isc1P = Entry(self.group1, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_input_Isc1P.place(x = 580, y = 0, width = 110, height = 22)
        self.text_input_Isc1P.insert(INSERT, "1.5")
        self.label_Isc1P = Label(self.group1, text = "Ikss1P", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Isc1P.place(x = 520, y = 0, width = 60, height = 22)
        self.label_Ikss1P = Label(self.group1, text = "kA", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Ikss1P.place(x = 700, y = 0, width = 30, height = 22)
        self.text_input_Isc3P_XR = Entry(self.group1, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_input_Isc3P_XR.place(x = 340, y = 30, width = 110, height = 22)
        self.text_input_Isc3P_XR.insert(INSERT, "18")
        self.label_Isc3P_XR = Label(self.group1, text = "Ikss3P X/R", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Isc3P_XR.place(x = 270, y = 30, width = 70, height = 22)
        self.text_input_Isc1P_XR = Entry(self.group1, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_input_Isc1P_XR.place(x = 580, y = 30, width = 110, height = 22)
        self.text_input_Isc1P_XR.insert(INSERT, "40")
        self.label_Isc1P_XR = Label(self.group1, text = "Ikss1P X/R", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Isc1P_XR.place(x = 520, y = 30, width = 60, height = 22)
        self.text_input_Sbase = Entry(self.group1, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_input_Sbase.place(x = 90, y = 0, width = 110, height = 22)
        self.text_input_Sbase.insert(INSERT, "100")
        self.label1_Sbase = Label(self.group1, text = "Sbase", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_Sbase.place(x = 10, y = 0, width = 80, height = 22)
        self.label_SbaseMVA = Label(self.group1, text = "MVA", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_SbaseMVA.place(x = 210, y = 0, width = 30, height = 22)
        self.button_Calculate = Button(self.group1, text = "Calculate", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.button_Calculate.place(x = 750, y = 0, width = 90, height = 22)
        self.button_Calculate['command'] = self.on_button_Calculate
        self.group2 = LabelFrame(self.w1, text = "Output to PSCAD", font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", bg="#414141", fg="white")
        self.group2.place(x = 10, y = 130, width = 870, height = 210)
        self.text_output_Zbase = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_Zbase.place(x = 540, y = 30, width = 110, height = 22)
        self.label_Zbase = Label(self.group2, text = "Zbase", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Zbase.place(x = 490, y = 30, width = 50, height = 22)
        self.text_output_Vbase = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_Vbase.place(x = 540, y = 60, width = 110, height = 22)
        self.label_Vbase = Label(self.group2, text = "Vbase", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Vbase.place(x = 490, y = 60, width = 50, height = 22)
        self.text_output_Ssc3P = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_Ssc3P.place(x = 540, y = 90, width = 110, height = 22)
        self.label_Ssc3P = Label(self.group2, text = "Ssc3P", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Ssc3P.place(x = 490, y = 90, width = 50, height = 22)
        self.text_output_Ssc1P = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_Ssc1P.place(x = 540, y = 120, width = 110, height = 22)
        self.label_Ssc1P = Label(self.group2, text = "Ssc1P", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Ssc1P.place(x = 490, y = 120, width = 50, height = 22)
        self.label_Zbase_ohm = Label(self.group2, text = "ohm", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Zbase_ohm.place(x = 660, y = 30, width = 30, height = 22)
        self.label_Vbase_kV = Label(self.group2, text = "kV", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Vbase_kV.place(x = 660, y = 60, width = 30, height = 22)
        self.label_Ssc3P_MVA = Label(self.group2, text = "MVA", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Ssc3P_MVA.place(x = 660, y = 90, width = 30, height = 22)
        self.label_Ssc1P_MVA = Label(self.group2, text = "MVA", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Ssc1P_MVA.place(x = 660, y = 120, width = 30, height = 22)
        self.text_output_Z1ohm = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_Z1ohm.place(x = 50, y = 0, width = 110, height = 22)
        self.text_output_Z1pu = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_Z1pu.place(x = 300, y = 0, width = 110, height = 22)
        self.text_output_R1ohm = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_R1ohm.place(x = 50, y = 30, width = 110, height = 22)
        self.text_output_R1pu = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_R1pu.place(x = 300, y = 30, width = 110, height = 22)
        self.text_output_X1ohm = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_X1ohm.place(x = 50, y = 60, width = 110, height = 22)
        self.text_output_X1pu = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_X1pu.place(x = 300, y = 60, width = 110, height = 22)
        self.text_output_Z0ohm = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_Z0ohm.place(x = 50, y = 90, width = 110, height = 22)
        self.text_output_Z0pu = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_Z0pu.place(x = 300, y = 90, width = 110, height = 22)
        self.text_output_R0ohm = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_R0ohm.place(x = 50, y = 120, width = 110, height = 22)
        self.text_output_R0pu = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_R0pu.place(x = 300, y = 120, width = 110, height = 22)
        self.text_output_X0ohm = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_X0ohm.place(x = 50, y = 150, width = 110, height = 22)
        self.text_output_X0pu = Entry(self.group2, font = tkinter.font.Font(family = "Calibri", size = 9), state = "normal", bg="#414141", fg="white")
        self.text_output_X0pu.place(x = 300, y = 150, width = 110, height = 22)
        self.label1_Z1 = Label(self.group2, text = "Z1", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_Z1.place(x = 20, y = 0, width = 20, height = 22)
        self.label1_R1 = Label(self.group2, text = "R1", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_R1.place(x = 20, y = 30, width = 20, height = 22)
        self.label1_X1 = Label(self.group2, text = "X1", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_X1.place(x = 20, y = 60, width = 20, height = 22)
        self.label1_Z0ohm = Label(self.group2, text = "Z0", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_Z0ohm.place(x = 20, y = 90, width = 20, height = 22)
        self.label1_R0 = Label(self.group2, text = "R0", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_R0.place(x = 20, y = 120, width = 20, height = 22)
        self.label1_X0 = Label(self.group2, text = "X0", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_X0.place(x = 20, y = 150, width = 20, height = 22)
        self.label1_Z1pu = Label(self.group2, text = "Z1", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_Z1pu.place(x = 270, y = 0, width = 20, height = 22)
        self.label1_R1pu = Label(self.group2, text = "R1", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_R1pu.place(x = 270, y = 30, width = 20, height = 22)
        self.label1_X1pu = Label(self.group2, text = "X1", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_X1pu.place(x = 270, y = 60, width = 20, height = 22)
        self.label1_Z0 = Label(self.group2, text = "Z0", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_Z0.place(x = 270, y = 90, width = 20, height = 22)
        self.label1_R0pu = Label(self.group2, text = "R0", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_R0pu.place(x = 270, y = 120, width = 20, height = 22)
        self.label1_X0pu = Label(self.group2, text = "X0", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label1_X0pu.place(x = 270, y = 150, width = 20, height = 22)
        self.label_Z1ohm = Label(self.group2, text = "ohm", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Z1ohm.place(x = 170, y = 0, width = 30, height = 22)
        self.label_X1ohm = Label(self.group2, text = "ohm", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_X1ohm.place(x = 170, y = 60, width = 30, height = 22)
        self.label_Z0ohm_copy = Label(self.group2, text = "ohm", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Z0ohm_copy.place(x = 170, y = 90, width = 30, height = 22)
        self.label_R0ohm = Label(self.group2, text = "ohm", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_R0ohm.place(x = 170, y = 120, width = 30, height = 22)
        self.label_X0ohm = Label(self.group2, text = "ohm", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_X0ohm.place(x = 170, y = 150, width = 30, height = 22)
        self.label_Z1pu_copy = Label(self.group2, text = "p.u.", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Z1pu_copy.place(x = 420, y = 0, width = 30, height = 22)
        self.label_R1pu_copy = Label(self.group2, text = "p.u.", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_R1pu_copy.place(x = 420, y = 30, width = 30, height = 22)
        self.label_X1pu_copy = Label(self.group2, text = "p.u.", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_X1pu_copy.place(x = 420, y = 60, width = 30, height = 22)
        self.label_Z0pu = Label(self.group2, text = "p.u.", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_Z0pu.place(x = 420, y = 90, width = 30, height = 22)
        self.label_R0pu_copy = Label(self.group2, text = "p.u.", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_R0pu_copy.place(x = 420, y = 120, width = 30, height = 22)
        self.label_X0pu = Label(self.group2, text = "p.u.", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_X0pu.place(x = 420, y = 150, width = 30, height = 22)
        self.label_R1ohm = Label(self.group2, text = "ohm", anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9), cursor = "arrow", state = "normal", bg="#414141", fg="white")
        self.label_R1ohm.place(x = 170, y = 30, width = 30, height = 22)

    def on_button_Calculate(self):
        try: 
            # retrieve inputr values
            Vline = float(self.text_input_Vline.get())
            Sbase = float(self.text_input_Sbase.get())
            Isc3P = float(self.text_input_Isc3P.get())
            Isc1P = float(self.text_input_Isc1P.get())
            Isc3P_XR = float(self.text_input_Isc3P_XR.get())
            Isc1P_XR = float(self.text_input_Isc1P_XR.get())
            XR3P = float(self.text_input_Isc3P_XR.get())
            XR1P = float(self.text_input_Isc1P_XR.get())
            
            # calculate values
            Vbase = Vline / math.sqrt(3)
            Zbase = (Vline * Vline) / Sbase
            Ssc3P = Vline * Isc3P * math.sqrt(3)
            Ssc1P = Vbase * Isc1P
            Z1ohm = Vline / (Isc3P * math.sqrt(3))
            Z1pu = Z1ohm / Zbase
            R1ohm = Z1ohm * math.cos(math.atan(XR3P))
            R1pu = R1ohm / Zbase
            X1ohm = Z1ohm * math.sin(math.atan(XR3P))
            X1pu = X1ohm / Zbase
            Z0ohm = ((3*Vbase) / (Isc1P)) - 2*Z1ohm
            R0ohm = Z0ohm * math.cos(math.atan(XR1P))
            X0ohm= Z0ohm * math.sin(math.atan(XR1P))
            Z0pu = Z0ohm / Zbase
            R0pu = R0ohm / Zbase
            X0pu = X0ohm / Zbase
        	   
            # update the outoyut fieldss       
            self.text_output_Zbase.delete(0, END)
            self.text_output_Zbase.insert(0, f"{Zbase:.4f}")
            self.text_output_Vbase.delete(0, END)
            self.text_output_Vbase.insert(0, f"{Vbase:.4f}")
            self.text_output_Ssc3P.delete(0, END)
            self.text_output_Ssc3P.insert(0, f"{Ssc3P:.4f}")
            self.text_output_Ssc1P.delete(0, END)
            self.text_output_Ssc1P.insert(0, f"{Ssc1P:.4f}")
            self.text_output_Z1ohm.delete(0, END)
            self.text_output_Z1ohm.insert(0, f"{Z1ohm:.4f}")
            self.text_output_Z1pu.delete(0, END)
            self.text_output_Z1pu.insert(0, f"{Z1pu:.4f}")
            self.text_output_R1ohm.delete(0, END)
            self.text_output_R1ohm.insert(0, f"{R1ohm:.4f}")
            self.text_output_R1pu.delete(0, END)
            self.text_output_R1pu.insert(0, f"{R1pu:.4f}")
            self.text_output_X1ohm.delete(0, END)
            self.text_output_X1ohm.insert(0, f"{X1ohm:.4f}")
            self.text_output_X1pu.delete(0, END)
            self.text_output_X1pu.insert(0, f"{X1pu:.4f}")
            self.text_output_Z0ohm.delete(0, END)
            self.text_output_Z0ohm.insert(0, f"{Z0ohm:.4f}")
            self.text_output_Z0pu.delete(0, END)
            self.text_output_Z0pu.insert(0, f"{Z0pu:.4f}")
            self.text_output_R0ohm.delete(0, END)
            self.text_output_R0ohm.insert(0, f"{R0ohm:.4f}")
            self.text_output_R0pu.delete(0, END)
            self.text_output_R0pu.insert(0, f"{R0pu:.4f}")
            self.text_output_X0ohm.delete(0, END)
            self.text_output_X0ohm.insert(0, f"{X0ohm:.4f}")
            self.text_output_X0pu.delete(0, END)
            self.text_output_X0pu.insert(0, f"{X0pu:.4f}")
        
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
        
    

if __name__ == '__main__':
    a = PowerFactoryToPSCAD_ShortCircuit(0)
    a.w1.mainloop()