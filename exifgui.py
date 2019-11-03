import tkinter as tk
from tkinter import filedialog
from exif import sort


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.folder_img = tk.PhotoImage(file="folder.gif")
        self.source_path = tk.StringVar()
        self.dest_path = tk.StringVar()
        self.init_main()

    def set_source(self):
        sourse_path = filedialog.askdirectory(title="Select folder")
        if sourse_path:
            self.source_path.set(sourse_path)

    def set_dest(self):
        dest_path = filedialog.askdirectory(title="Select folder")
        if dest_path:
            self.dest_path.set(dest_path)

    def sort(self):
        # print(self.source_path.get())
        sourceFolder = self.source_path.get()+"/"
        destFolder = self.dest_path.get()+"/"
        print(sourceFolder)
        # print(destFolder)

        sort(sourceFolder, destFolder)
        # raise NotImplementedError

    def init_main(self):
        label_title = tk.Label(root, text='Sort your pictures')
        label_title.place(x=50, y=20)

        label_source = tk.Label(root, text='Source:')
        label_source.place(x=50, y=50)
        label_destination = tk.Label(root, text='Destination:')
        label_destination.place(x=50, y=80)

        btn_run = tk.Button(root, text='Run', command=self.sort)
        btn_run.place(x=295, y=120)

        self.source_path.set("Select path")
        self.dest_path.set("Select path")

        btn_select_source = tk.Button(root, text='Source folder', command=self.set_source, image=self.folder_img)
        btn_select_source.place(x=300, y=49)    

        btn_select_dest = tk.Button(root, text='Destination folder', command=self.set_dest, image=self.folder_img)
        btn_select_dest.place(x=300, y=79)   

        entry_source = tk.Entry(bg='white', textvariable=self.source_path)
        entry_source.place(x=120, y=50, height=25, width=177)

        entry_dest = tk.Entry(bg='white', textvariable=self.dest_path)
        entry_dest.place(x=120, y=80, height=25, width=177)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("EXIF sort")
    root.geometry("380x180")
    root.resizable(False, False)
    root.mainloop()



