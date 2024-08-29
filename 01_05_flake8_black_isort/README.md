## コマンド実行設定方法
pip install flake8
pip install flake8-docstrings
pip install black
pip install isort

flake8 *.py
black *.py
isort *.py

## 自動のコミット前チェック
pip install pre-commit
pre-commit sample-config > .pre-commit-config.yaml
pre-commit install
