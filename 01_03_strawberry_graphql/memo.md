## 参考
PythonのGraphQLライブラリStrawberryを使ってみた
https://qiita.com/nttpc-aiyo/items/bb946b864e67c2da9a53

データ挿入
```
mutation {
  taskAdd(taskInput:{title:"テスト", description:"詳細"}){
    id
    title
    description
  }
}
```

データ取得
```
{
  tasks {
    id
    title
    description
  }
}
```