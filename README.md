# defective-project

このプロジェクトはバグだらけのプロジェクトです。皆さんの力ですべてのバグを取り除いてください。

## バグの取り除き方

プログラムは*src*ディレクトリにあります。それに対応したテストプログラムは*tests*に用意されています。

例
```
src/type/hoge.py
tests/type/hoge_test.py
```
テストプログラムは、プログラムの返して欲しい結果が書いてあります。また問題に記述されてあるコメントを頼りにプログラムを修正しましょう。**テストプログラムは変更してはいけません**。修正出来たと思ったら、テストを実行してみましょう。無事テストが通っていれば成功です。

## テストの実行方法

テスト対象のコードは、`tests`ディレクトリ化に配置されてあります。
テストコードは、`tests_*.py`という名前の規則でネーミングされてあります。
テストの実行は、Pythonの実行と同様に、次のようなコマンド`python3 -m unittest test_foo.py`で実行できます。

### 個別実行

実行コードと対になるように章ごとにテストは配置しているので、自分が実行したい問題のファイル名のパスを指定して実行しましょう。

```
$ python3 -m unittest tests/hoge/test_foo.py
```

### 全体実行

すべてのテストを実行するには、以下のコマンドを実行します。
このコマンドが成功したときが、皆さんの勝利となります。

```
$ python3 -m unittest tests
```

## すべての終わり

すべてのバグが取り除かれれば、この説明文の一番上のバッジが`PASSED`となり緑になるはずです。みなさん、それを目指しましょう。また、テストをただ通すだけではいけません。誰が見てもわかりやすいスマートな解法を目指してみましょう。

