import tkinter as tk
def open_new_window():
    tk.Toplevel(root)
root = tk.Tk()
root.title("RVS CET")

menu_bar = tk.Menu(root)
menu = tk.Menu(menu_bar, tearoff=0)
menu.add_command(label="Next Window", command=open_new_window)
menu_bar.add_cascade(label="File", menu=menu)
root.config(menu=menu_bar)

root.mainloop()
