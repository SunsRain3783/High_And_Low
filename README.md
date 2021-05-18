### プラン
１ｐ
・親カードと子カードの一致をなくす
・遊び方の追加
・数字の一覧表示（出たカードがわかるようにする）
・連続何回成功したかのカウンター
・プレイヤーは初期ポイントを保持
・ポイントは決められた範囲でベットでき、成功に応じて獲得ポイントが加算
・途中でやめたらポイント獲得、ハズレは０
・


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
