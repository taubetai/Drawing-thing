import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()