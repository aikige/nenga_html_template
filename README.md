# HTML+CSSによる宛名書きテンプレート

宛名書きのサービスが年々減っているので、HTML+CSS で単純に処理したほうが楽なのではないかと思いついて作成しました。

## 使い方

HTML ([`address.html`](address.html)) を編集し、Chrome などを使って PDF に変更したのち、等倍ではがきに印刷してください。

2025年の年賀状をベースにデザインしていますが、はがきの種類などによっては、郵便番号の位置を微調整する必要があるかもしれません。
以下の Class の CSS 設定内容を調整してください。主に `top` と `left` を調整することになります。
- `to_postalcode3` 
- `to_postalcode4` 
- `from_postalcode3`
- `from_postalcode4`

## 特徴

- HTMLの構造はできるだけシンプルにしてありますので、比較的簡単に書き換えられるはずです。
- Class `page` が指定してある `section` 要素が宛名1ページに該当します。複数の宛名を印刷したい場合は単純に `section` を増やしていってください。
- 郵便番号は等幅文字として `Courier` を使って、
  それを `position:absolute` で `section` を基準とした絶対座標に置いていますが、
  前述の通り場合によっては位置を微調整する必要があるかもしれません。
- Flex Layout を活用して、住所、宛名、差出人情報を均等割付します。
- フォントは無料で手に入る `UDデジタル教科書体 ProN` を使っています。
  [Morisawa Fonts のフリープラン](https://morisawafonts.com/plans/free/) などを使って取得してください。
  動作は MacOS で確認しています。Windows 同梱同種のフォントと `font-family` を調整する必要があるかもしれません。
- ディスプレイで見る際には、背景に郵便局の「年賀はがき商品のご案内」にあるお年玉付き年賀はがきの画像をベースとして作成したガイドを表示する設定にしてあります。
  - お年玉付き年賀はがきではなく、通常のはがきを使う場合は「[通常はがき](https://www.post.japanpost.jp/service/standard/two/type/normal.html)」のページの画像を使うとよいでしょう。

## 参考にしたもの

- 基本的な考え方: https://qiita.com/tanazaway/items/72bc167871d66522b3c5
- 宛先の郵便番号枠の仕様: https://www.post.japanpost.jp/zipcode/zipmanual/p05.html
- Courierの縦横比(5:3): https://stackoverflow.com/questions/19113725/what-dependency-between-font-size-and-width-of-char-in-monospace-font
