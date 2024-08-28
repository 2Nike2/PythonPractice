## Visual Studio Code拡張機能Pylint設定方法
- 拡張機能アイコンをクリックし、検索欄に「Pylint」と入力してインストールボタンをクリック。

## コマンド実行Pylint設定方法
pip install pylint
pylint *.py

## 自動のコミット前Pylintチェック
pip install pre-commit
pre-commit sample-config > .pre-commit-config.yaml
pre-commit install
pylint --generate-rcfile > ~/.config/pylintrc