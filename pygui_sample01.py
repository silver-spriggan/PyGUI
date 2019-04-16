"""
2019.2 
pygui_sample01.py
主にtkinterを利用したGUI自主練サンプル
"""

# ----------------------------
# ライブラリの定義
# ----------------------------
import os
import tkinter
import psutil
import socket
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup

# ----------------------------
# From 定義
# ----------------------------
# Tkクラス生成
global frm
frm = tkinter.Tk()

# 画面サイズ
frm.geometry('600x400')

# 画面タイトル
frm.title('主にtkinterを利用したGUI自主練画面')

# ----------------------------
# OS系の情報表示
# ----------------------------

# ラベル(見出し)
lbl_head01 = tkinter.Label(frm, text='メモリ使用率:')
lbl_head01.place(x=30, y=20)

# メモリ使用率を取得、表示
mem = psutil.virtual_memory() 
lbl_mem01 = tkinter.Label(frm, text=str(mem.percent) + '%')
lbl_mem01.place(x=100, y=20)

# ラベル(見出し)
lbl_head02 = tkinter.Label(frm, text='ディスク使用率:')
lbl_head02.place(x=190, y=20)

# ディスク使用率を取得、表示
dsk = psutil.disk_usage('/')
lbl_mem02 = tkinter.Label(frm, text=str(dsk.percent) + '%')
lbl_mem02.place(x=270, y=20)

# ラベル(見出し)
lbl_head03 = tkinter.Label(frm, text='バッテリー残量:')
lbl_head03.place(x=340, y=20)

# バッテリー残量を取得、表示
btr = psutil.sensors_battery()
lbl_mem03 = tkinter.Label(frm, text=str(btr.percent) + '%')
lbl_mem03.place(x=420, y=20)

# ラベル(見出し)
lbl_head04 = tkinter.Label(frm, text='IPアドレス:')
lbl_head04.place(x=30, y=40)

# IPアドレスを取得
ip = socket.gethostbyname(socket.gethostname())
lbl_mem04 = tkinter.Label(frm, text=str(ip))
lbl_mem04.place(x=100, y=40)

# ラベル(見出し)
lbl_head05 = tkinter.Label(frm, text='computer name:')
lbl_head05.place(x=30, y=60)

# computer nameを取得
host = socket.gethostname()
lbl_mem05 = tkinter.Label(frm, text=str(host))
lbl_mem05.place(x=120, y=60)

# ----------------------------
# 関数定義
# click event(menu object)
# ----------------------------
# メニューから呼び出される関数
def open_file():
    typ = [('CSV file', '*.csv'), ('Text file', '*.txt'), ('All', '*')]
    dir = 'C:\\'
    fle = filedialog.askopenfilenames(filetypes = typ, initialdir = dir) 

    filelist = list()

    for f in fle:
        # print(f)
        filelist.append(str(f))
 
    for intindex, objfilelist in enumerate(filelist):
        print(intindex, objfilelist)

def open_path():
    dir = 'C:\\'
    fld = filedialog.askdirectory(initialdir = dir) 
 
    files = []
    texts = []

    print ('fld = ' + str(fld))
    fld = fld.replace('/',os.sep) 
    print ('fld = ' + str(fld))

    for x in os.listdir(fld):
        if os.path.isfile(fld + os.sep + x):
            files.append(fld + os.sep + x) 

    print (files)

    for y in files:
        if(y[-4:] == '.txt'):     #ファイル名の後ろ4文字を取り出してそれが.txtなら
            texts.append({'file':y , 'size':os.path.getsize(y)})  #リストに追加

    for intindex, objfilelist in enumerate(texts):
        print(intindex, objfilelist)
 
def exit_disp():
    print('Click menu Exit')
    frm.quit()

# ----------------------------
# 関数定義
# click event(button object)
# ----------------------------
# folder　clickイベント
def folder_click():
    dir = 'C:\\'
    fld = filedialog.askdirectory(initialdir = dir) 
    lbl_folder01 = tkinter.Label(frm, text=str(fld))
    lbl_folder01.place(x=30, y=130)

# webreq　clickイベント
def webreq_click():
    url = 'https://www.google.co.jp/search'

    # グーグルへ接続
    req = requests.get(url, params={'q': 'パイソン'})

    # アドレス取得
    lbl_folder02 = tkinter.Label(frm, text=str(req.url))
    lbl_folder02.place(x=130, y=130)

# scryping　clickイベント
def scryping_click():
    url = 'https://headlines.yahoo.co.jp/rss/zdn_n-c_sci.xml'

    strValue = list()

    # Yahooへ接続
    req = requests.get(url)

    # BeautifulSoupで解析
    txt= BeautifulSoup(req.text, 'html.parser')

    # スクレイピング
    for rss in txt.findAll('item'):
        strValue.append(str(rss.title.string))

    # 表示
    lbl_folder03 = tkinter.Label(frm, text=str(strValue))
    lbl_folder03.place(x=130, y=130)

# ----------------------------
# メニューバー作成 
# ----------------------------
men = tkinter.Menu(frm) 

#メニューバーを画面にセット 
frm.config(menu=men) 

#メニューに親メニュー（ファイル）を作成する 
menu_file = tkinter.Menu(frm) 
men.add_cascade(label='file', menu=menu_file) 

#親メニューに子メニュー（開く・閉じる）を追加する 
menu_file.add_command(label='open file', command=open_file) 
menu_file.add_command(label='set path ', command=open_path) 
menu_file.add_separator() 
menu_file.add_command(label='exit', command=exit_disp)

# ----------------------------
# 画面へ button Object 配置
# ----------------------------

# ボタン(set folder)
btn1 = tkinter.Button(frm, text='set folder', command=folder_click)
btn1.place(x=30, y=90)

# ボタン(get web request)
btn2 = tkinter.Button(frm, text='web request', command=webreq_click)
btn2.place(x=130, y=90)

# ボタン(スクレイピング)
btn3 = tkinter.Button(frm, text='Scryping', command=scryping_click)
btn3.place(x=230, y=90)

# ボタン(exit)
btn_exit = tkinter.Button(frm, text='閉じる', command=frm.destroy)
btn_exit.place(x=500, y=350)

# ----------------------------
# 画面を表示
# ----------------------------
frm.mainloop()
