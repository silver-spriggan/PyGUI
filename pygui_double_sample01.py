# -*- coding: utf-8 -*-

#====================================================================================
# ライブラリ
#====================================================================================
# GUIを扱う
import tkinter
# tkinterよりデザインが良くなる
from tkinter import ttk

#====================================================================================
# 関数定義
#====================================================================================
#------------------------------------------------------------------------------------
# startボタンを押したときの処理
#------------------------------------------------------------------------------------
def changePage(page):
    # MainPageを上位層にする
    page.tkraise()

#====================================================================================
# 本体関数
#====================================================================================
# main関数を追加し、スコープを切る
def main() -> None:
    # インスタンス生成
    window = tkinter.Tk()

    # ウィンドウタイトルを決定
    window.title("WORDPRACTICE")

    # ウィンドウの大きさを決定
    window.geometry("800x600")

    # ウィンドウのグリッドを 1x1 にする
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    #-----------------------------------StartPage---------------------------------
    ### StartPage用のFrameを生成
    startPage = tkinter.Frame(window)

    ### タイトル表示
    #--- ラベル生成
    # 空白
    spaceLabel1 = [tkinter.Label(startPage, text="") for column in range(10)]
    spaceLabel2 = [tkinter.Label(startPage, text="") for column in range(3)]
    # タイトル
    titleLabelFont  = ("Helevetice", 32, "bold")
    titleLabel      = ttk.Label(startPage, text="WORDPRACTICE", font=titleLabelFont)

    #--- ラベル配置
    # 空白
    for index in range(10):
        spaceLabel1[index].pack()
    # タイトル
    titleLabel.pack()

    ### ボタン表示
    #---  ボタン生成
    startButton =\
     ttk.Button(startPage, text="           Start           ", command=lambda : changePage(mainPage))

    #---  ボタン配置
    # 空白
    for index in range(3):
        spaceLabel2[index].pack()
    # ボタン
    startButton.pack()

    #StartPageを配置
    startPage.grid(row=0, column=0, sticky="nsew")

    #-----------------------------------MainPage---------------------------------
    ### MainPage用のFrameを生成
    mainPage = tkinter.Frame(window)

    ###  空白
    #---  ラベル生成
    spaceLabel1 = [tkinter.Label(mainPage, text="") for column in range(5)]
    # タイトル
    titleLabelFont  = ("Helevetice", 18)
    titleLabel      =\
       ttk.Label(mainPage, text="ユーザー名を入力してください。", font=titleLabelFont)

    #---  ラベル配置
    # 空白
    for index in range(5):
        spaceLabel1[index].pack()
    # タイトル
    titleLabel.pack()

    ### フレーム表示
    #---  フレーム生成
    frame = ttk.Frame(mainPage)
    #---  フレーム配置
    frame.pack()

    ### ユーザー名入力表示
    #--- ラベル生成
    # 空白
    spaceLabel2 = [tkinter.Label(frame, text="") for column in range(3)]

    # ユーザー名
    userNameLabelFont  = ("Helevetice", 14)
    userNameLabel      = ttk.Label(frame, text="ユーザー名：", font=userNameLabelFont)

    #--- ラベル配置
    # 空白
    for index in range(3):
        spaceLabel2[index].grid(row=index, column=0)
    # ユーザー名
    userNameLabel.grid(row=4, column=0)

    #---  エントリー生成
    userName = tkinter.StringVar()
    userNameEntry = ttk.Entry(frame, textvariable=userName, width=30)

    #---  エントリー配置
    userNameEntry.grid(row=4, column=1)

    ### ボタン表示
    #---  ボタン生成
    okButton = ttk.Button(frame, text="  OK  ")

    #---  ボタン配置
    okButton.grid(row=4, column=3)

    # MainPageを配置
    mainPage.grid(row=0, column=0, sticky="nsew")

    # StartPageを上位層にする
    startPage.tkraise()

    # プログラムを始める
    window.mainloop()

#====================================================================================
# 本体処理
#====================================================================================
if __name__ == "__main__":
    main()
