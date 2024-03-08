import tkinter as tk

def create_gui(index):
    window = tk.Tk()
    window.title(f"GUI {index}")

    label = tk.Label(window, text=f"Counter: {0}")
    label.pack(padx=20, pady=10)

    def update_counter(count):
        label["text"] = f"Counter: {count}"
        window.after(1000, update_counter, count + 1)

    update_counter(0)

if __name__ == "__main__":
    for i in range(5):
        create_gui(i)

    tk.mainloop()
