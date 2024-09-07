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

## 既存のプロジェクトをpoetryで管理
poetry init

## 依存パッケージの追加
poetry add package_name

## 仮想環境の実行
poetry shell

## 仮想環境の終了
exit

## 仮想環境の終了(shell残す)
deactivate

## requirements.txtの生成
$ poetry export --without-hashes --dev --output requirements.txt
