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
