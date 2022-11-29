import tkinter as tk
from mainWindow import mainWindow

# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


if __name__ == "__main__":
    mainWindow()
    root.title('Beat Saber Score Comparator')
    root.mainloop()
