# ChatGPT API のテスト用

## 動作環境

Python 3.11.6 を使用。Mac上で動作確認。

APIキーは環境変数で渡す。
~~~shell:shell
export OPENAI_API_KEY="APIキー"      ← " " で囲む
~~~

必要に応じてライブラリをインストールする。
~~~shell:shell
pip3 install openai
~~~

## ファイル説明

### 01-HelloWorld.py

ChatGPT API を動かしてみる。Hello World 的なスクリプト。

### 02-role.py

ロール設定の例。バカボンパパ仕様。

### 03-image-generation.py

Dall-Eによる画像生成。URLにアクセスするとブラウザ表示される。

### 04-image.py

gpt-4oによる画像ファイルの認識。

## その他

### data

実験用ファイル格納フォルダー

### openai-py311.zip

AWS Lambda の「レイヤー」用のファイル。Python 3.11.6 に、fastapiとOpenAIのみ追加したもの。

