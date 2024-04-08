# Point Cloud Library for Python

## How to install

### from wheel

```bash
pip install https://d2p2mp26w3f0s0.cloudfront.net/pypcl/PyPcl-0.0.1-cp311-cp311-linux_x86_64.whl
```

| Python | Arch | wheel url |
|:--|:--|:--|
| 3.11 | x86_64 | https://d2p2mp26w3f0s0.cloudfront.net/pypcl/PyPcl-0.0.1-cp311-cp311-linux_x86_64.whl |
| 3.12 | x86_64 | https://d2p2mp26w3f0s0.cloudfront.net/pypcl/PyPcl-0.0.1-cp312-cp312-linux_x86_64.whl |
| 3.11 | aarch64 | https://d2p2mp26w3f0s0.cloudfront.net/pypcl/PyPcl-0.0.1-cp311-cp311-linux_aarch64.whl |
| 3.12 | aarch64 | https://d2p2mp26w3f0s0.cloudfront.net/pypcl/PyPcl-0.0.1-cp312-cp312-linux_aarch64.whl |


# How to setup [WIP]

依存パッケージをダウンロード

```bash
sudo apt install libpcl-dev
```

whlファイルの作成

```bash
cd /path/to/PyPcl
poetry install
poetry run python setup.py bdist_wheel
```

`/dist` 下の whl ファイルを pip でインストールできる。
