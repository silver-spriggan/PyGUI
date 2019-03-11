"""
2019.2 
pygui_sample01.py
主にtkinterを利用したGUI自主サンプル
"""

import tkinter
import psutil
import socket
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup


# Tkクラス生成
frm = tkinter.Tk()
# 画面サイズ
frm.geometry('600x400')
# 画面タイトル
frm.title('サンプル画面')

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


# clickイベント
def folder_click():
    dir = 'C:\\'
    fld = filedialog.askdirectory(initialdir = dir) 
    lbl_folder01 = tkinter.Label(frm, text=str(fld))
    lbl_folder01.place(x=30, y=130)

# clickイベント
def webreq_click():
    url = 'https://www.google.co.jp/search'

    # グーグルへ接続
    req = requests.get(url, params={'q': 'パイソン'})

    # アドレス取得
    lbl_folder02 = tkinter.Label(frm, text=str(req.url))
    lbl_folder02.place(x=130, y=130)

# clickイベント
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

# 画面をそのまま表示
frm.mainloop()
