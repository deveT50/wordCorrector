#-*- encoding: utf-8 -*-
#! /usr/bin/env python

#http://qiita.com/yasunori/items/31a23eb259482e4824e2
#http://mayo.hatenablog.com/entry/2014/07/11/111432
#---------------------------------------------------------
#入力:引数１：任意のtxtファイル
#出力：単語ごとに改行されたtxtファイル:wakati_YYMMDhhmmss.txt"
#
#---------------------------------------------------------

import os
import sys
import MeCab
import datetime

todaydetail = datetime.datetime.today()

#デフォルトエンコーディング設定
reload(sys)
sys.setdefaultencoding("utf-8")

#neologd辞書をインストール済みの場合(返り値に品詞情報も加わるのでこのコードのままでは使用できない)
#mecab = MeCab.Tagger(' -d /usr/lib/mecab/dic/mecab-ipadic-neologd')
#インストールしていない場合
#mecab = MeCab.Tagger('mecabrc')
#mecab = MeCab.Tagger('-Ochasen')
mecab = MeCab.Tagger("-O wakati")

#除去する文字
#今回は<html>等を除去するので<>は残したまま
STOP_WORD = "　 の □ ■ ◆　◇　※　◎　▽　 1 2 3 4 5 6 7 8 9 0 １ ２ ３ ４ ５ ６ ７ ８ ９ ０ ^ - 。 、 「 」 （ ） ? ？ ： ， , ． ! ！ # $ % & ' ( ) = ~ | ` { } * + ? _  [ ] @ : ; / . ¥ ^ 【 】 ￥ ＿ ／ 『 』 ＞ ？ ＿ ＊ ＋ ｀ ｜ 〜 ＊ ＋ ＞ ？ ＃ ” ＃ ＄ ％ ＆ ’ \" ・".split()
#STOP_WORD =　STOP_WORD + " 1 2 3 4 5 6 7 8 9 0 １ ２ ３ ４ ５ ６ ７ ８ ９ ０ ".split()



#txt→単語ごとに改行されたlist
def news2wakati(argtxt):
    
    wakati_text = ""
    text = argtxt
    wakati_raw = mecab.parse(text.encode('utf-8'))
    wakati_formalize = []
    #空白で分割
    for row in wakati_raw.split(" "):
        row = row.rstrip().lower()
        #stopWOrd除去
        for sw in STOP_WORD:
            row = row.replace(sw, '')
        #空でなければlistに追加
        if row!="" and row!=" " and row!="\n" and row!="\r" and row!="\r\n":
            wakati_formalize.append(row+"\n")
    
    return wakati_formalize


if __name__ == "__main__":
    
    time=todaydetail.strftime("%Y%m%d%H%M%S")
    f = open("wakati_"+time+".txt", 'w')

    doc = open(sys.argv[1]).read().strip("\r").strip("\n").lower()

    #前処理する
    txt=news2wakati(doc)
    
    #listをtxtにして書き出す
    outstr=""        
    for i in range(len(txt)):
        outstr=outstr+txt[i]
    
    f.write(outstr)
    f.close()

