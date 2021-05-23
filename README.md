### プラン
2. WIN表示はスムーズに、LOSE表示は多少長めにして、LOSEならホーム画面に戻る
5. ポイントで買えるアイテム
    ```bash
    スキップシューズ(最大10個)
    フリップグローブ(最大10個)
    ロワースイッチ(最大５個)
    ハイヤースイッチ(最大５個)
    報酬倍率３倍
    ```
1. カンストでゲームクリア→製作者からのメッセージを表示する


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
