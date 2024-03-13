"""
import tkinter as tk

def main():
    root = tk.Tk()
    label = tk.Label(root, text="Hello World!")
    label.pack(anchor="w")
    root.mainloop()

if __name__=="__main__":
    import os
    import sys
    print(sys.argv)
    main()
"""
import sys
import tkinter as tk

def main():
    root = tk.Tk()
    label = tk.Label(root, text=sys.argv)
    label.pack(anchor="w")
    root.mainloop()

if __name__=="__main__":
    main()
