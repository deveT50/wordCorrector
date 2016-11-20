# wordCorrector  
単語自動校正器

jubatusハッカソン(https://jubatus.connpass.com/event/41692/)にて作成したもの  
入力文章に含まれる単語を単語数だけのクラスに分類し、誤記のある単語が正しい単語と同じクラスに分類されるようにする  
新聞記事のテキストデータをjubatusで学習し、作成した文章の誤記を修正するシステムを意図している  

*前処理*  
1.get_data.sh       ”□”、”◇”等の不要な文字を削除  
2.news2wakati.py    入力txtファイルを単語に分かち書きし、1単語1行のtxtファイルを出力  

*学習*  
1.config.json       jubatusサーバのセットアップファイル  
2.cubreporter.py    jubatusクライアントで実行する学習・予測のコード  

その他  
*in.txt                       news2wakati.pyの入力ファイルの例（ハッカソンで提供されたデータは終了時に削除しているため）  
*wakati_20161120150948.txt    news2wakati.pyの出力ファイルの例  
