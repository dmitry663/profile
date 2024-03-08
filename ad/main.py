import os
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
            # GUI를 가장 위로 가져오기
            self.root.lift()

if __name__ == "__main__":
    lock_file_path = "lock_file.txt"

    # lock 파일이 존재하면 이미 실행 중
    if os.path.exists(lock_file_path):
        print("Already running. Exiting...")
        exit()

    # lock 파일 생성
    with open(lock_file_path, "w") as lock_file:
        lock_file.write("lock")

    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()

    # 프로그램 종료 후 lock 파일 삭제
    os.remove(lock_file_path)
