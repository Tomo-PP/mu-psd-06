# 実践ソフトウェア開発 サンプルソース

# はじめに

本サンプルソースは、講義：実践ソフトウェア開発で課題となる開発のベースになるソースです。

Frontend担当者とBackend担当者に分割して開発する前提で、PythonとJavaScriptを用いて開発を行います。

--------------------------------------------------------------------------------
# ソフトウェアのインストール

コマンドプロンプトから、以下のコマンドを実行して、必要なソフトウェアをインストールしてください。

```
winget install OpenJS.NodeJS.LTS
winget install Python
winget install Git.Git
winget install Microsoft.VisualStudioCode
```

wingetが使えない場合やWindows以外の環境を利用する場合、個別の入手先は以下のリンクを参照してください。

- https://nodejs.org/en
- https://www.python.org/downloads/　
- https://code.visualstudio.com/download
- https://gitforwindows.org/

--------------------------------------------------------------------------------
# テンプレートプロジェクトの取得

```
mkdir C:\source 
cd C:\source
git clone https://github.com/tt-hasegawa/mu-psd-00.git
```

00のところは事前に割り当てられた01から09までの番号を利用してください。
また、ペアの人と同じリポジトリを利用してください。

--------------------------------------------------------------------------------

# バックエンド開発

Python + Flaskを用いてバックエンドのAPIを開発します。
リクエストされたURLに応じて、必要なリソースを返したり、
事前に作成したAIでの応答を返す機能を実装します。

## ライブラリのインストール

```
cd backend
pip install -r requirements.txt
```

## 実行方法
```
cd backend
python server.py
```

http://localhost:5000/

にアクセスして動きを確認してみましょう。

## ソースの解説

- バックエンドサーバのソースファイルはServer.pyです。

- @app.route(…)がURLを表し、次行の関数がそのロジック実装になります。

- 関数の戻り値がBackendサーバで表示される値になります。

## AI機械学習について

今回の演習サンプルでは、scikit-learnという機械学習ライブラリを用います。

機械学習の手順は、原則以下のとおりです。

- データを準備して、訓練データ、テストデータに分割する。

```
# CSVファイルをDataFrameに読み込みます。
df = pd.read_csv('data/toyota.csv')

# データ構造を確認します。
df.info()
sns.pairplot(df)
sns.distplot(df['price'])
plt.show()
y = df['price']
x = df[['year','tax']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)
```

- 学習モデルを決定し、訓練データを読み込ませて、学習を行う。

```
model=LinearRegression()
model.fit(x_train,y_train)
```

- 

- テストデータを用いて検証する。

```
ret1=model.score(x_train,y_train)
print(ret1)
ret2=model.score(x_test,y_test)
print(ret2)
```

- できた学習モデルを保存する。


```
joblib.dump(model,'model.pkl')
```


最後の手順でファイルに保存されたAIを、バックエンドサーバから呼び出して、回答します。

```
def add_data(year,tax):
    # 引数の作成
    data={"year":[year],"tax":[tax]}
    param=pd.DataFrame(data)

    # AIモデルの読込
    model = joblib.load('model.pkl')

    # 先読み実行
    ret=y_pred=model.predict(param)

    # 得られた結果をJSON形式にして返す
    price=ret[0]
    return jsonify({"price":price})
```




--------------------------------------------------------------------------------

# フロントエンド開発

SvelteKitと呼ばれるJavaScriptフレームワークを用いてWeb画面を作成します。

## ライブラリのインストール

```
cd frontend
npm i
```

## 実行方法
```
cd frontend 
npm run dev
```

http://localhost:5173

にアクセスして動きを確認してみましょう。

## ソースの解説

- Srcフォルダの下にページごとに+page.svelteファイルが1個あり、これを編集していきます。

- Svelteファイルは以下3つのブロックに分かれます。

- scriptブロック  JavaScriptでプログラムコードを書く

- mainブロック    html文書構造を記述するブロック

- styleブロック   CSSで、表示／装飾するスタイルを記載する

- scriptブロックで宣言した変数の内容をHTMLに表示する場合は、{ }で括って記述します。

- scriptブロックで動的に変更された値も即座にHTML側に反映されます。

- styleブロックにはタグ名、クラス名で属性の設定先を指定します。

## 一からソースを生成する場合

Svelte kitで一からソースを作成したい場合は以下のコマンドでプロジェクトを作成できます。

```
npm create svelte@latest frontend
```


## その他便利コマンド

- ソースのフォーマット
```
cd frontend
npm run format
```

- 文法チェック
```
cd frontend
npm run lint
```


--------------------------------------------------------------------------------

# 開発の進め方

## やりたいことをきめる
 
 documents/design-document.mdの概要説明欄にやりたいこと、解決したい課題、実現したい機能をまとめてください。

## 画面構成を考える

作成するアプリが必要になる画面の一覧を画面構成に列挙していってください。

## 画面遷移を考える

できたら、それがどのような相関関係になるか、画面遷移を含めて、page-design.drawio.svgに描いてみてください。

## やりとりするデータを決める

AIにどんな情報を入力して、どんな回答を得たいか、を考えてください。

## APIとデータに格納する部分を作る

フロントエンド／バックエンドの間でやりとりするデータの定義を考えて決めてください。

JSONの実装形式とサンプルデータ、コメントを記載して、どんなデータをやりとりするか、を記述してください。

--------------------------------------------------------------------------------

# プロジェクトの進め方

Githubリポジトリ画面上段にあるissueに沿って課題を進めていき、終わり次第、issueをクローズしていってください。


--------------------------------------------------------------------------------

# 参考リンク

- [とほほのFlask入門](https://www.tohoho-web.com/ex/flask.html)

- [とほほのCSS入門](https://www.tohoho-web.com/css/basic.htm)

- [とほほのPython入門](https://www.tohoho-web.com/python/)

- [Svelte](https://svelte.jp/)

- [SvelteKit](https://kit.svelte.jp/)
