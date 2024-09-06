## poetry導入

1. pipxをインストール  
   pipx... PythonのCLIツールをグローバル環境を汚さずにインストールするためのツール
    MacOS  
```
brew install pipx
pipx ensurepath
```
2. poetryをインストール  
    MacOS  
```
pipx install poetry
```

## やっておきたい設定
```
poetry config virtualenvs.in-project true
```
理由: プロジェクトフォルダの位置を変えても仮想環境の紐付けをやり直す必要がなくなる

## poetryでプロジェクト新規作成
poetry new poetry_new_test

## 依存パッケージの追加
poetry add package_name