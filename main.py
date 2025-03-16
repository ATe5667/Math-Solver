import sys
import tkinter as tk
from graphics import *

def on_close():
    root.destroy()
    sys.exit()

if __name__ == "__main__":
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()