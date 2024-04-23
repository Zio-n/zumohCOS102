import tkinter as tk
from tkinter import messagebox

class FoodOrderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Food Order System")
        
        self.items = {
            "Burger": {"price": 500, "quantity": 10},
            "Pizza": {"price": 800, "quantity": 8},
            "Fries": {"price": 300, "quantity": 20},
            "Salad": {"price": 400, "quantity": 15},
            "Coke": {"price": 200, "quantity": 30}
        }
        
        self.order = {}
        
        self.create_widgets()
    
    def create_widgets(self):
        # Menu Display
        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(self.menu_frame, text="Menu").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.menu_frame, text="Quantity Available").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.menu_frame, text="Price (₦)").grid(row=0, column=2, padx=10, pady=5)
        
        row_num = 1
        for item, details in self.items.items():
            tk.Label(self.menu_frame, text=item).grid(row=row_num, column=0, padx=10, pady=5)
            tk.Label(self.menu_frame, text=details["quantity"]).grid(row=row_num, column=1, padx=10, pady=5)
            tk.Label(self.menu_frame, text=details["price"]).grid(row=row_num, column=2, padx=10, pady=5)
            row_num += 1
        
        # Customer Input Section
        self.customer_frame = tk.Frame(self.master)
        self.customer_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
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
        
        self.add_to_cart_btn = tk.Button(self.customer_frame, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_btn.grid(row=3, column=1, padx=10, pady=5, sticky="e")
        
        # Cart Display
        self.cart_frame = tk.Frame(self.master, bg="white")
        self.cart_frame.grid(row=0, column=1, rowspan=2, padx=100, pady=10, sticky="nsew")

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
        if quantity > self.items[item]["quantity"]:
            messagebox.showerror("Error", "Quantity requested exceeds available stock.")
            return
            
        if item in self.order:
            self.order[item]["quantity"] += quantity
        else:
            self.order[item] = {"quantity": quantity, "price": self.items[item]["price"]}
            
        self.update_cart_display()
        
        
    def update_cart_display(self):
        cart_content = ""
        total = 0
        for item, details in self.order.items():
            cart_content += f"{item}: {details['quantity']}\n"
            total += details['quantity'] * details['price']
        self.cart_content_label.config(text=cart_content)
        self.total_label.config(text=f"Total (₦): {total}")
    
    
    def clear_cart(self):
        self.order = {}
        self.update_cart_display()
        
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
    app = FoodOrderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
