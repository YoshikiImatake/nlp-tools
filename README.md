# nlp-tools

## MakeMecabText.py
テキストファイルを読み込み、形態素解析した結果を出力する。

## McbReader.py
形態素解析の結果をリストとして保持する。
Driver.pyで試せる。

## Driver.py
McbReaderの実行用ドライバ。

# 使い方
1. 以下のファイル構成でPythonコードとサンプルテキストを用意する。
[任意のディレクトリ名]/  
    ┠MakeMecabText.py  
    ┠McbReader.py  
    ┠Driver.py  
    ┠text/  
    ┃   ┗sample.txt  
    ┗text_mcb/  

2. MakeMecabText.pyを実行する。
3. Driver.pyを実行する。
