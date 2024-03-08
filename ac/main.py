import tkinter as tk
from tkinter import filedialog

class FileExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Explorer")

        # 폴더 선택 버튼
        self.select_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=10)

        # 선택된 폴더 경로를 표시하는 레이블
        self.folder_label = tk.Label(root, text="")
        self.folder_label.pack(pady=10)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_label.config(text=f"Selected Folder: {folder_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()
