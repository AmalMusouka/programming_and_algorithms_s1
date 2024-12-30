import tkinter as tk

root = tk.Tk()
root.title('hello')

canvas = tk.Canvas(root, width=800, height=800)
canvas.grid()

#event handler
def on_click(event):
    print('click')

canvas.bind('<Button>', on_click) #binding an event handler

root.mainloop()