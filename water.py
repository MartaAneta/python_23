from tkinter import Tk, Label, Entry, Button, messagebox


class Water:
    def __init__(self):
        self.total_quantity = 0

    def add_water(self, grams):
        self.total_quantity += grams

    def calculate_total_quantity(self):
        return self.total_quantity


class WaterTrackerApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Water Tracker")
        self.window.geometry("800x600")
        self.window.configure(background='lightblue')

        self.water_labels = ["Drinks"]
        self.waters = []

        water_label = Label(self.window, text="Water, wpisz ilość wypitej wody w mililitrach:", font=("Arial", 12), width=40)
        water_label.pack()
        water_label.configure(background='blue')

        water_grams_entry = Entry(self.window)
        water_grams_entry.pack()
        water_grams_entry.configure(background="#800080", font=("Arial", 12), width=40)

        total_quantity_label = Label(self.window, text="Water Quantity: 0", font=("Arial", 12), width=40)
        total_quantity_label.pack()
        total_quantity_label.configure(background="#00FF00")

        self.add_button = Button(self.window, text="Add", command=self.add_water)
        self.add_button.pack()
        self.add_button.configure(background="#00FF00", font=("Arial", 12), width=40)

        self.total_quantity = 0

        self.waters.append({
            "label": self.water_labels,
            "water_grams_entry": water_grams_entry,
            "total_quantity_label": total_quantity_label,
            "water": Water()
        })

    def add_water(self):
        for water_data in self.waters:
            grams = water_data["water_grams_entry"].get()

            if grams:
                try:
                    grams = int(grams)
                    water_data["water"].add_water(grams)
                    water_data["total_quantity_label"].config(
                        text="{} Quantity: {}".format(water_data["label"],
                                                      water_data["water"].calculate_total_quantity())
                    )
                    water_data["water_grams_entry"].delete(0, "end")  # Usunięcie wpisanego tekstu
                except ValueError:
                    messagebox.showerror("Invalid Input", "Grams must be a valid integer.")

        self.total_quantity = sum(water_data["water"].calculate_total_quantity() for water_data in self.waters)
        self.total_quantity_label.config(text="Total Quantity: " + str(self.total_quantity))

    def run(self):
        self.window.mainloop()


app = WaterTrackerApp()
app.run()
