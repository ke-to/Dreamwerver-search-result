# Dreamwerver Search Result
Dreamweverのgrep検索の結果から、ヒットしたファイルの重複なしリストを作成するpythonのスクリプトです。

## 特徴
- .pyファイルが置かれているディレクトリの全XMLファイルを参照する
- XMLファイル内のパス情報を一覧化
- XMLと同じ名前で.txtを出力する

## 使い方
1. Dreamwerverで検索
- レポートの保存
- レポートをスクリプトと同じディレクトリに移動
- search_list.pyを起動

### 用途に合わせて以下の部分を編集してください。  
- for url in dom.getElementsByTagName("取得したいパラメータ"):

※DreamwerverCCでの動作のみを確認しています。