from functions import *
import tkinter
import customtkinter
from tkinter import messagebox
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
def main():
    app = customtkinter.CTk()
    app.geometry("700x400")
    app.resizable(0, 0)

    # Configurazione griglia
    app.grid_rowconfigure(0, weight = 1)
    app.grid_rowconfigure(2, weight = 1)
    app.grid_rowconfigure(4, weight = 1)
    app.grid_rowconfigure(6, weight = 1)
    app.grid_rowconfigure(8, weight = 1)
    app.grid_columnconfigure(0, weight = 1)
    app.grid_columnconfigure(2, weight = 1)
    app.grid_columnconfigure(4, weight = 1)
    app.grid_columnconfigure(6, weight = 1)
    app.grid_columnconfigure(8, weight = 1)

    # Definizione entry nella quale verà inserito il numero da convertire
    entry_var = customtkinter.StringVar()
    entry = customtkinter.CTkEntry(master = app, font=("Roboto medium", 20), textvariable=entry_var)
    # Posizionamento della entry sulla griglia definita in precedenza
    entry.grid(row = 3, column = 1, rowspan = 2, columnspan = 4, sticky = "nesw")

    # Definizione label testo "Convertitore di basi" e piazzamento sulla griglia
    label_1 = customtkinter.CTkLabel(master = app, text="Convertitore di basi", font=("Roboto medium", -16))
    label_1.grid(row = 2, column = 1, columnspan = 4, sticky = "sew")

    # Definizione dei 3 menu a tendina (base partenza, arrivo e precisione) e piazzamento sulla griglia
    basep = customtkinter.StringVar(value = "Partenza")
    basepmenu = customtkinter.CTkOptionMenu(master = app, values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"], variable=basep, height=40,  font=("Roboto medium", -16))
    basepmenu.grid(column = 7, row = 2, sticky = "ew")

    basea = customtkinter.StringVar(value = "Arrivo")
    baseamenu = customtkinter.CTkOptionMenu(master = app, values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"], variable=basea, height=40,  font=("Roboto medium", -16))
    baseamenu.grid(column = 7, row = 3, sticky = "ew")

    prec = customtkinter.StringVar(value = "Precisione")
    precmenu = customtkinter.CTkOptionMenu(master = app, values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"], variable=prec, height=40,  font=("Roboto medium", -16))
    precmenu.grid(column = 7, row = 4, sticky = "ew")

    # Funzione di conversione
    def conversione(n, base_p, base_a, precisione):
        try:
            # Casistica base 8/16 e base 16/8
            if (base_p == 8 and base_a == 16) or (base_p == 16 and base_a == 8):
                a = base816base2(n.upper(), int(base_p))
                b = base2base816(a, int(base_a))
                messagebox.showinfo(title="Conversione", message=f"Conversione: {b}")
            # Casistica base n/m 
            else:
                a = baseNbase10(n.upper(), int(base_p))
                b = base10baseM(a, int(base_a), int(precisione))
                messagebox.showinfo(title="Conversione", message=f"Conversione: {b}")
        except Exception:
            pass

    # Definizione bottone conversione e piazzamento sulla griglia
    btn_convert = customtkinter.CTkButton(master = app, height=40, text = "converti",  font=("Roboto medium", -16), command = lambda *args:conversione(entry.get(), basep.get(), basea.get(), prec.get()), hover=True)
    btn_convert.grid(row = 5, column = 7, sticky = "ew")

    app.mainloop()

    

main()