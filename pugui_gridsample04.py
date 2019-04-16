
import tkinter
from tkinter import ttk
import os

class TestTreeview(ttk.Labelframe):
    def __init__(self, master=None):
        '''LabelとTreeviewの表示'''
        super().__init__(master, text="Treebox")
        
        #親フォルダ名表示用ラベル
        self.folder_name = tkinter.Label(self, text="folder name", bg='lightblue')
        self.folder_name.pack()

        #ファイル名表示用ラベル
        self.file_name = tkinter.Label(self, text="file name", bg='lightyellow')
        self.file_name.pack()

        #Treeview
        self.tree = ttk.Treeview(self) #1
        self.tree.bind("<<TreeviewSelect>>", self.show_selected) #2
        path = os.getcwd()
        root_node = self.tree.insert("", "end", text=path, open=True) #3
        self.process_directory(root_node, path) #4
        self.tree.pack()

    def process_directory(self, parent, path):
        '''ディレクトリ内のファイル名を表示するメソッド'''
        for p in os.listdir(path): #1
            abspath = os.path.join(path, p) #2
            oid = self.tree.insert(parent, "end", text=p, open=False) #3
            isdir = os.path.isdir(abspath) #4
            if isdir: #5
                self.process_directory(oid, abspath)

    def show_selected(self, event):
        '''選択したファイル名とその親フォルダをラベルに表示するメソッド'''
        curItem = self.tree.focus() #1
        parentItem = self.tree.parent(curItem) #2
        self.folder_name["text"] = self.tree.item(parentItem)["text"] #3
        self.file_name["text"] = self.tree.item(curItem)["text"] #4

if __name__ == "__main__":
    root = tkinter.Tk()
    f = TestTreeview(master=root)
    f.pack()
    root.mainloop()

