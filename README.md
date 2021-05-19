### プラン
１ｐ
1. 遊び方の追加
1. 連続何回成功したかのカウンター
1. ポイントで買えるアイテム
    ```bash
    出たカードがわかる（チートアイテム？）
    背景の変更（複数種類）
    ベット報酬の倍率が変わる　２倍→３倍→・・・（もとは１倍）（買うと見えるようになる）
    スキップできる
    透視できる
    ```
1. カード残り枚数の可視化（すべてなくなったらボーナス？）
1. ゲームクリアを設ける？製作者からのメッセージを表示する


### ローカルでの起動の仕方
1. git cloneする
    ```bash
    git clone https://github.com/SunsRain3783/High_And_Low
    ```
2. フォルダを移動
    ```bash
    cd High_And_Low
    ```
3. ライブラリのインストール
    ```bash
    pip install -r requirements.txt
    ```
### CSSや画像などstaticファイルを変更したとき
```bash
python manage.py collectstatic
```
