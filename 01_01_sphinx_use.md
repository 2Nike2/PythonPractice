## Sphinxの使い方

**超重要 パッケージの中にあるモジュールは \_\_init\_\_.pyが無ければ無視される**  
**この説明ではsrcディレクトリがドキュメント化対象のルートとする**  
**フォルダの指定の際に正確にドキュメント化対象のルートを選ばないと異常が発生するので、**  
**深すぎる階層だけでなく、ルートを含むからといって浅い階層を指定してもいけない**  
**他のフォルダ名や階層をルートとするときは、適宜読み替えること**  

1. 下記を実行  
  pip install sphinx
  pip install myst-parser
2. 指定のプロジェクトに移動し、プロジェクトのディレクトリ直下でdocsディレクトリを作成  
  cd project_dir  
  mkdir docs
3. Sphinxの雛形を作成  
  sphinx-quickstart docs
  ソースディレクトリとビルドディレクトリを分ける（y / n） [n]: n
  他は適当に入力
  4. docs/conf.pyを編集、
  まず先頭に
  ```
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))
  ```
  を追加  
  そして拡張機能を  
  ```
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]
```
  に書き換える。  


  5. index.rstの編集  
     (下記ではmain.py, module1.py, module2.pyをドキュメント化する場合を想定)  
  ```
    .. toctree::
     :maxdepth: 2
     :caption: Contents:
    
     main
     module1
     module2

  ```
6. ドキュメントを生成
  ```
  sphinx-apidoc -f -o ./docs ./src
  cd docs
  make html
  ```
