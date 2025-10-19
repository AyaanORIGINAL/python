import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.root.geometry("800x600")

        self.menu = {
            "FRIES MEAL": 2, "LUNCH MEAL": 2,
            "BURGER MEAL": 3, "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5, "DRINKS": 1
        }
        self.exchange_rate = 121

                # ==== Background Setup ====
        self.bg_canvas = tk.Canvas(root, width=800, height=600)
        self.bg_canvas.pack(fill="both", expand=True)
        try:
            bg_img = Image.open("fud.png").resize((800, 600))
            self.bg_image = ImageTk.PhotoImage(bg_img)
            self.bg_canvas.create_image(0, 0, anchor="nw", image=self.bg_image)
        except Exception as e:
            print(f"Background not loaded: {e}")
            self.bg_canvas.create_rectangle(0, 0, 800, 600, fill="#0d79ec", outline="")


        # ==== Frame on Background ====
        self.frame = ttk.Frame(self.bg_canvas, padding=20)
        self.bg_canvas.create_window(400, 300, window=self.frame)

        ttk.Label(self.frame, text="Restaurant Order Management",
                  font=("Arial", 20, "bold")).grid(row=0, columnspan=3, pady=15)

        self.entries = {}
        for i, (item, price) in enumerate(self.menu.items(), 1):
            ttk.Label(self.frame, text=f"{item} ($ {price})", font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
            entry = ttk.Entry(self.frame, width=7, justify="center")
            entry.grid(row=i, column=1, padx=5)
            self.entries[item] = entry

        self.currency = tk.StringVar(value="USD")
        ttk.Label(self.frame, text="Currency:", font=("Arial", 12)).grid(row=len(self.menu)+1, column=0)
        combo = ttk.Combobox(self.frame, textvariable=self.currency, values=["USD", "BDT"], width=10, state="readonly")
        combo.grid(row=len(self.menu)+1, column=1, pady=10)
        combo.bind("<<ComboboxSelected>>", self.update_prices)

        ttk.Button(self.frame, text="Place Order", command=self.place_order).grid(
            row=len(self.menu)+2, columnspan=3, pady=15
        )

    def update_prices(self, _=None):
        currency = self.currency.get()
        rate = self.exchange_rate if currency == "BDT" else 1
        for item, label in self.entries.items():
            new_price = self.menu[item] * rate
            label.config(text=f"{item} ({currency} {new_price:.2f})")

    def place_order(self):
        cur, rate, sym = self.currency.get(), 1, "$"
        if cur == "BDT": rate, sym = self.exchange_rate, "৳"
        total, summary = 0, "🧾 Order Summary:\n"
        for item, entry in self.entries.items():
            q = entry.get()
            if q.isdigit() and int(q) > 0:
                q, cost = int(q), int(q) * self.menu[item] * rate
                total += cost
                summary += f"{item}: {q} x {sym}{self.menu[item]*rate:.2f} = {sym}{cost:.2f}\n"

        messagebox.showinfo("Order Details", f"{summary}\nTotal: {sym}{total:.2f}") if total else \
            messagebox.showerror("Error", "Please order at least one item.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)