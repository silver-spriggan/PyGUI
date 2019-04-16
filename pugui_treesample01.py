import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

class PathTreeFrame(ttk.Frame):
    """ディレクトリ・ファイルツリーを表示するFrame."""
 
    def __init__(self, master, path=os.curdir):
        """初期化
 
        args:
            master: 親ウィジェット
            path: どのパスを起点にツリーを作るか。デフォルトはカレント
 
        """
        # 親クラスのコンストラクタ（オブジェクトが生成される時に実行されるメソッド）を実行しつつ、
        # 追加処理を行うというチョイ足し
        super().__init__(master)

        # このselfは、インスタンス自身を示すもの
        self.root_path = os.path.abspath(path)
        self.nodes = {}
        self.create_widgets()
 
    def create_widgets(self):
        """ウィジェットの作成"""
        # ツリービューの作成とスクロール設定
        self.tree = ttk.Treeview(self)
        ysb = ttk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)
 
        # レイアウト。スクロールバーは拡大させない
        self.tree.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        ysb.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
 
        # ディレクトリを開いた際と、ダブルクリック(ファイル選択)を関連付け
        self.tree.bind('<<TreeviewOpen>>', self.open_node)
        self.tree.bind('<Double-1>', self.choose_file)
 
        # ルートのパスを挿入
        self.insert_node('', self.root_path, self.root_path)
 
    def insert_node(self, parent, text, abspath):
        """Treeviewにノードを追加する
 
        args:
            parent: 親ノード
            text: 表示するパス名
            abspath: 絶対パス
 
        """
        # まずノードを追加する
        node = self.tree.insert(parent, 'end', text=text, open=False)
 
        # ディレクトリならば、空の子要素を追加し開けるようにしておく
        if os.path.isdir(abspath):
            self.tree.insert(node, 'end')
            self.nodes[node] = (False, abspath)
        else:
            self.nodes[node] = (True, abspath)
 
    def open_node(self, event):
        """ディレクトリを開いた際に呼び出される
 
        self.nodes[node][0]がFalseの場合はまだ開かれたことがないと判断し、
        そのディレクトリ内のパスを追加する
        一度開いたか、又はファイルの場合はself.nodes[node][0]はTrueになります
 
        """
        node = self.tree.focus()
        already_open, abspath = self.nodes[node]
 
        # まだ開かれたことのないディレクトリならば
        if not already_open:
 
            # 空白の要素が追加されているので、消去
            self.tree.delete(self.tree.get_children(node))
 
            # ディレクトリ内の全てのファイル・ディレクトリを取得し、Treeviewに追加
            for entry in os.scandir(abspath):
                self.insert_node(
                    node, entry.name, os.path.join(abspath, entry.path)
                )
 
            # 一度開いたディレクトリはTrueにする
            self.nodes[node] = (True, abspath)
 
    def choose_file(self, event):
        """ツリーをダブルクリックで呼ばれる"""
        node = self.tree.focus()
        # ツリーのノード自体をダブルクリックしているか?
        if node:
            already_open, abspath = self.nodes[node]
            if os.path.isfile(abspath):
                print(abspath)
 
    def update_dir(self, event=None):
        """ツリーの一覧を更新する"""
        self.create_widgets()
 
    def change_dir(self, event=None):
        """ツリーのルートディレクトリを変更する"""
        dir_name = filedialog.askdirectory()
        if dir_name:
            self.root_path = dir_name
            self.create_widgets()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Path Tree')
    app = PathTreeFrame(root)
    app.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
    root.bind('<F4>', app.change_dir)
    root.bind('<F5>', app.update_dir)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()
