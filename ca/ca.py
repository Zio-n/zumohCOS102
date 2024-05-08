import tkinter as tk
from tkinter import messagebox

class PAUOrderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PAU Cafeteria Ordering System")
        
        self.items = {
            # Rice/Pasta
            "Jollof Rice": {"price": 350, "quantity": 10},
            "Coconut Fried Rice": {"price": 350, "quantity": 8},
            "Jollof Spaghetti": {"price": 350, "quantity": 20},
            # Proteins
            "Sweet Chili Chicken": {"price": 1100, "quantity": 15},
            "Grilled Chicken Wings": {"price": 400, "quantity": 30},
            "Fried Beef": {"price": 400, "quantity": 30},
            "Fried Fish": {"price": 500, "quantity": 30},
            "Boiled Egg": {"price": 200, "quantity": 12},
            "Sauteed Sausages": {"price": 200, "quantity": 13},
            # Side dishes
            "Savoury Beans": {"price": 350, "quantity": 30},
            "Roasted Sweet Potatoes": {"price": 300, "quantity": 13},
            "Fried Plantains": {"price": 150, "quantity": 12},
            "Mixed Vegetable Salad": {"price": 150, "quantity": 13},
            "Boiled Yam": {"price": 150, "quantity": 13},
            # Soups & Swallows
            "Eba": {"price": 100, "quantity": 30},
            "Pounded Yam": {"price": 100, "quantity": 13},
            "Semo": {"price": 100, "quantity": 12},
            "Atama Soup": {"price": 450, "quantity": 13},
            "Boiled Yam": {"price": 480, "quantity": 13},
            # Beverages
            "Water": {"price": 200, "quantity": 30},
            "Glass Drink (35cl)": {"price": 150, "quantity": 13},
            "PET Drink (35cl)": {"price": 300, "quantity": 12},
            "PET Drink (50cl)": {"price": 350, "quantity": 13},
            "Glass/Canned malt": {"price": 500, "quantity": 13},
            "Fresh Yo": {"price": 600, "quantity": 30},
            "Pineapple Juice": {"price": 350, "quantity": 13},
            "Mango Juice": {"price": 350, "quantity": 12},
            "Zobo Drink": {"price": 350, "quantity": 13},
        }
        self.order = {}
        
        self.create_widgets()
    
    def create_widgets(self):
        # Menu Display
        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(self.menu_frame, text="Menu").grid(row=0, column=0, columnspan=3, padx=10, pady=5)

        self.menu_canvas = tk.Canvas(self.menu_frame, bg='white')
        self.menu_canvas.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.menu_scrollbar = tk.Scrollbar(self.menu_frame, orient="vertical", command=self.menu_canvas.yview)
        self.menu_scrollbar.grid(row=1, column=2, sticky='ns')

        self.menu_canvas.configure(yscrollcommand=self.menu_scrollbar.set)
        self.menu_canvas.bind('<Configure>', lambda e: self.menu_canvas.configure(scrollregion=self.menu_canvas.bbox("all")))

        self.menu_frame_inner = tk.Frame(self.menu_canvas)
        self.menu_canvas.create_window((0, 0), window=self.menu_frame_inner, anchor="nw")

        row_num = 0
        for item, details in self.items.items():
            tk.Label(self.menu_frame_inner, text=item).grid(row=row_num, column=0, padx=10, pady=5)
            tk.Label(self.menu_frame_inner, text=details["quantity"]).grid(row=row_num, column=1, padx=10, pady=5)
            tk.Label(self.menu_frame_inner, text=details["price"]).grid(row=row_num, column=2, padx=10, pady=5)
            row_num += 1
        
        # Customer Input Section
        self.customer_frame = tk.Frame(self.master)
        self.customer_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.customer_name_label = tk.Label(self.customer_frame, text="Customer Name:")
        self.customer_name_label.grid(row=0, column=0, padx=10, pady=5)
        self.customer_name_entry = tk.Entry(self.customer_frame)
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.food_item_label = tk.Label(self.customer_frame, text="Select Food Item:")
        self.food_item_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.food_item_var = tk.StringVar()
        self.food_item_dropdown = tk.OptionMenu(self.customer_frame, self.food_item_var, *self.items.keys())
        self.food_item_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        self.quantity_label = tk.Label(self.customer_frame, text="Quantity:")
        self.quantity_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.quantity_entry = tk.Entry(self.customer_frame)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        self.clear_cart_btn = tk.Button(self.customer_frame, text="Clear Cart", command=self.clear_cart)
        self.clear_cart_btn.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        
        self.add_to_cart_btn = tk.Button(self.customer_frame, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_btn.grid(row=3, column=1, padx=10, pady=20, sticky="e")
        
        
        # Cart Display
        self.cart_frame = tk.Frame(self.master, bg="white")
        self.cart_frame.grid(row=0, column=2, rowspan=4, padx=10, pady=10, sticky="nsew")

        self.cart_title_label = tk.Label(self.cart_frame, text="Cart", bg="white")
        self.cart_title_label.grid(row=0, column=0, padx=10, pady=5)

        self.cart_content_label = tk.Label(self.cart_frame, text="", bg="white")
        self.cart_content_label.grid(row=1, column=0, padx=10, pady=5)

        self.total_label = tk.Label(self.cart_frame, text="Total (₦): 0", bg="white")
        self.total_label.grid(row=2, column=0, padx=10, pady=100)

        self.pay_btn = tk.Button(self.cart_frame, text="Pay", command=self.show_order)
        self.pay_btn.grid(row=3, column=0, padx=10, pady=5)
    
    
    def add_to_cart(self):
        item = self.food_item_var.get()
        quantity = int(self.quantity_entry.get())
        if quantity <= 0:
            messagebox.showerror("Error", "Quantity must be greater than zero.")
            return
        if item not in self.items:
            messagebox.showerror("Error", "Invalid food item.")
            return
        
        
        if item in self.order:
            self.order[item]["quantity"] += quantity
        else:
            self.order[item] = {"quantity": quantity, "price": self.items[item]["price"]}
        
        if self.order[item]["quantity"] > self.items[item]["quantity"]:
            self.order[item]["quantity"] -= quantity
            messagebox.showerror("Error", "Quantity requested exceeds available stock.")
            return
        
        self.update_cart_display()
        
    def clear_cart(self):
        self.order = {}
        self.update_cart_display()
        
    def update_cart_display(self):
        cart_content = ""
        total = 0
        for item, details in self.order.items():
            cart_content += f"{item}: {details['quantity']}\n"
            total += details['quantity'] * details['price']
        self.cart_content_label.config(text=cart_content)
        self.total_label.config(text=f"Total (₦): {total}")
    

        
    def show_order(self):
        total = sum(item["quantity"] * item["price"] for item in self.order.values())
        discount = self.calculate_discount(total)
        discounted_total = total * (1 - discount)
        
        order_summary = "Item\tQuantity\tPrice (₦)\n"
        for item, details in self.order.items():
            order_summary += f"{item}\t{details['quantity']}\t\t{details['quantity'] * details['price']}\n"
        order_summary += f"\nTotal: ₦{total:.2f}\nDiscount: {discount * 100:.0f}%\nTotal (After Discount): ₦{discounted_total:.2f}"
        
        messagebox.showinfo("Order Summary", order_summary)
    
    def calculate_discount(self, total):
        if total < 1000:
            return 0
        elif total < 2500:
            return 0.1
        elif total < 5000:
            return 0.15
        else:
            return 0.25

def main():
    root = tk.Tk()
    app = PAUOrderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
