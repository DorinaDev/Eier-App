import tkinter as tk
from tkinter import messagebox

# Klasse für die Berechnung
class EierKochRechner:
  def __init__(self, gewichtsklasse):
    self.gewichtsklasse = gewichtsklasse
  
  def berechne_kochzeit(self, härtegrad):
    if self.gewichtsklasse == "S": 
      return 2.000 * härtegrad + 0.500
    elif self.gewichtsklasse == "M":
      return 0.968 * härtegrad + 2.825
    elif self.gewichtsklasse == "L":
      return 1.373 * härtegrad + 1.491
    elif self.gewichtsklasse == "XL":
      return 1.095 * härtegrad + 2.563
    else:
      return None

# Funktion für den Button
def berechne_zeit():
    gewicht = entry_größe.get().strip().upper()  # Eingabe normalisieren
    haertegrad = haertegrad_var.get()

    # Validierung
    if gewicht not in ["S", "M", "L", "XL"]:
        messagebox.showerror("Fehler", "Bitte eine gültige Eiergröße eingeben (S, M, L, XL).")
        return

    try:
        haertegrad = int(haertegrad)
        if haertegrad not in range(1, 6):
            raise ValueError
    except ValueError:
        messagebox.showerror("Fehler", "Bitte einen Härtegrad zwischen 1 und 5 wählen.")
        return

    # Berechnung
    eirechner = EierKochRechner(gewicht)
    kochzeit = eirechner.berechne_kochzeit(haertegrad)

    if kochzeit is not None:
        ergebnis_label.config(text=f"Kochzeit: {round(kochzeit)} Min.")
    else:
        messagebox.showerror("Fehler", "Ungültige Eingabe.")

# GUI erstellen
root = tk.Tk()
root.title("Eier-Koch App")
root.geometry("400x300")
root.configure(bg="#f5f5dc")

# Eingabe für Größe
tk.Label(root, text="Eiergröße (S, M, L, XL):", bg="#f5f5dc", font=("Garamond", 12)).pack(pady=5)
entry_größe = tk.Entry(root, font=("Garamond", 12))
entry_größe.pack(pady=5)

# Dropdown für Härtegrad
haertegrad_var = tk.StringVar(value="3")
tk.Label(root, text="Härtegrad wählen:", bg="#f5f5dc", font=("Garamond", 12)).pack(pady=5)
haertegrad_menu = tk.OptionMenu(root, haertegrad_var, "1", "2", "3", "4", "5")
haertegrad_menu.pack(pady=5)

# Button zum Berechnen
tk.Button(root, text="Berechnen", command=berechne_zeit, font=("Garamond", 12), bg="#ffcc00").pack(pady=10)

# Ergebnis-Anzeige
ergebnis_label = tk.Label(root, text="", bg="#f5f5dc", font=("Garamond", 14, "bold"))
ergebnis_label.pack(pady=10)

# Hauptloop starten
root.mainloop()