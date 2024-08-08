import tkinter as tk
from tkinter import messagebox

class KiranaStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kirana Store Calculator")
        
        self.item_list = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # Labels and Entry for item name
        self.name_label = tk.Label(self.root, text="Item Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Labels and Entry for item price
        self.price_label = tk.Label(self.root, text="Item Price (Rs.)")
        self.price_label.grid(row=1, column=0, padx=10, pady=5)
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Labels and Entry for item quantity
        self.quantity_label = tk.Label(self.root, text="Quantity")
        self.quantity_label.grid(row=2, column=0, padx=10, pady=5)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Add Item Button
        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Generate Receipt Button
        self.generate_button = tk.Button(self.root, text="Generate Receipt", command=self.generate_receipt)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=5, column=0, columnspan=2, pady=10)
    
    def add_item(self):
        item_name = self.name_entry.get()
        item_price = self.price_entry.get()
        item_quantity = self.quantity_entry.get()
        
        if not item_name or not item_price or not item_quantity:
            messagebox.showerror("Input Error", "Please enter all fields")
            return
        
        try:
            item_price = float(item_price)
            item_quantity = int(item_quantity)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid price and quantity")
            return
        
        total_price = item_price * item_quantity
        self.item_list.append((item_name, item_price, item_quantity, total_price))
        
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        
        messagebox.showinfo("Item Added", f"Added {item_quantity} of {item_name} at Rs. {item_price} each. Total: Rs. {total_price}")
    
    def generate_receipt(self):
        if not self.item_list:
            messagebox.showwarning("No Items", "No items to generate receipt")
            return
        
        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Receipt")
        
        receipt_text = tk.Text(receipt_window)
        receipt_text.pack()
        
        receipt_text.insert(tk.END, "{:<20} {:<10} {:<10} {:<10}\n".format("Item", "Price", "Quantity", "Total"))
        receipt_text.insert(tk.END, "-"*50 + "\n")
        
        total_bill = 0
        for item in self.item_list:
            name, price, quantity, total = item
            receipt_text.insert(tk.END, f"{name:<20} {price:<10} {quantity:<10} {total:<10}\n")
            total_bill += total
        
        receipt_text.insert(tk.END, "-"*50 + "\n")
        receipt_text.insert(tk.END, f"Total Bill: Rs. {total_bill}\n")
        receipt_text.insert(tk.END, "-"*50 + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = KiranaStoreApp(root)
    root.mainloop()
