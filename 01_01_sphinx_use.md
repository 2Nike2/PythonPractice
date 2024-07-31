## Sphinxの使い方

1. 下記を実行  
  pip install sphinx
  pip install myst-parser
2. 指定のプロジェクトに移動し、プロジェクトのディレクトリ直下でdocsディレクトリを作成  
  cd project_dir  
  mkdir docs
3. Sphinxの雛形を作成  
  sphinx-quickstart docs
  ソースディレクトリとビルドディレクトリを分ける（y / n） [n]: y  
  他は適当に入力
  4. docs/source/conf.pyを編集、
  まず先頭に
  ```
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
  ```
  を追加  
  そして拡張機能を  
  ```
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser'
]
```
  に書き換える。  


  5. index.rstの編集  
  ```
    .. toctree::
     :maxdepth: 2
     :caption: Contents:
    
     main
  ```
6. ドキュメントを生成
  ```
  sphinx-apidoc -f -o ./docs/source ./
  cd docs
  make html
  ```
