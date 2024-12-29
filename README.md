# HTML+CSSによる宛名書きテンプレート

宛名書きのサービスが年々減っているので、HTML+CSS で単純に処理したほうが楽なのではないかと思いついて作成しました。

## 使い方

HTML ([`address.html`](address.html)) を編集し、Chrome などを使って PDF に変更したのち、等倍ではがきに印刷してください。

Class `page` が指定してある `section` 要素が宛名1ページに該当しますので、複数の宛名を印刷したい場合は単純に `section` をコピペで増やしていってください。

2025年の年賀状をベースにデザインしていますが、はがきの種類などによっては、郵便番号の位置を微調整する必要があるかもしれません。
以下の Class の CSS 設定内容を調整してください。主に以下の変数を修正してください。

|変数|意味|
|--|--|
|`--to-pc-offset-x`|宛先郵便番号の開始位置(X)|
|`--to-pc-offset-y`|宛先郵便番号の開始位置(Y)|
|`--from-pc-offset-x`|差出人郵便番号の開始位置(X)|
|`--from-pc-offset-y`|差出人郵便番号の開始位置(Y)|

## 特徴

- HTMLの構造はできるだけシンプルにしてありますので、比較的簡単に書き換えられるはずです。
- 郵便番号の開始位置は調整が必要になる可能性が高いので、前述の通り変数で修正できるようにしてあります。
- Flex Layout を活用して、住所、宛名、差出人情報を均等割付します。
- フォントは無料で手に入る `UDデジタル教科書体 ProN` を使っています。
  [Morisawa Fonts のフリープラン](https://morisawafonts.com/plans/free/) などを使って取得してください。
  動作は MacOS で確認しています。Windows 同梱同種のフォントと `font-family` を調整する必要があるかもしれません。
- ディスプレイで見る際には、背景に郵便局の「年賀はがき商品のご案内」にあるお年玉付き年賀はがきの画像をベースとして作成したガイドを表示する設定にしてあります。ガイドは印刷時には出力されません。
  - お年玉付き年賀はがきではなく、通常のはがきを使う場合は「[通常はがき](https://www.post.japanpost.jp/service/standard/two/type/normal.html)」のページの画像を使うとよいでしょう。

## 技術的な補足

### 郵便番号のレイアウトについて

- Courier の文字幅はほぼ 0.6em ですので、`letter-spacing` は文字送りの幅を X とした場合、
  `letter-spacing:calc(X - 0.6em);` で指定すると正しい字送りが実現できます。
- 宛先郵便番号枠の文字送りは、郵便局が公開している文字送りの仕様をベースに計算しています。
- 差出人郵便番号枠の文字送りは、標準仕様がないようなので、画像から計算して枠の送り幅が 4.0mm と想定しています。

### 背景画像

ディスプレイ表示に使っている [`nenga_hagaki.png`](nenga_hagaki.png) は、郵便局の「年賀はがき商品のご案内」に出ている年賀状画像をベースに作成しています。

### スクリーンショットを Chrome で取るためのスクリプト

- [`screenshot.py`](screenshot.py) はSelenium の Chrome Driver を用いて年賀状のスクリーンショットを取るためのスクリプトです。

## 参考にしたもの

- 基本的な考え方: https://qiita.com/tanazaway/items/72bc167871d66522b3c5
- 宛先の郵便番号枠の仕様: https://www.post.japanpost.jp/zipcode/zipmanual/p05.html
- Courierの縦横比(5:3): https://stackoverflow.com/questions/19113725/what-dependency-between-font-size-and-width-of-char-in-monospace-font
