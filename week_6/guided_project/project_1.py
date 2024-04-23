import tkinter as tk
from tkinter import messagebox

def calculate_shipping_fee():
    location = location_var.get()
    weight = weight_entry.get()

    try:
        weight = float(weight)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid weight")
        return

    if location == "Epe":
        if weight > 10:
            shipping_fee = 10000  # 10kg or above
        else:
            shipping_fee = 5000   # Below 10kg
    elif location == "Lekki":
        if weight > 10:
            shipping_fee = 5000  # 10kg or above
        else:
            shipping_fee = 3500   # Below 10kg

    messagebox.showinfo("Shipping Fee", f"The shipping fee is ₦{shipping_fee}")

# Create main window
root = tk.Tk()
root.title("Shipping Fee Calculator")

# Location selection
location_var = tk.StringVar()
location_label = tk.Label(root, text="Select Location:")
location_label.grid(row=0, column=0, padx=10, pady=5)
location_optionmenu = tk.OptionMenu(root, location_var, "Epe", "Lekki")
location_optionmenu.grid(row=0, column=1, padx=10, pady=5)

# Weight input
weight_label = tk.Label(root, text="Enter Weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_shipping_fee)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
