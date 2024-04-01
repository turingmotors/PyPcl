# setup方法 [WIP]
依存パッケージをダウンロード
```
sudo apt install libpcl-dev
```
whlファイルの作成
```
cd /path/to/PyPcl
python setup.py bdist_wheel
```
仮想環境に移動後、/dist下のwhlファイルをpipでインストールできる。
