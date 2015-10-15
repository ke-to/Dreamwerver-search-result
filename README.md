# Dreamwerver Search Result
Dreamweverのgrep検索の結果から、ヒットしたファイルの重複なしリストを作成するpythonのスクリプトです。

## 使い方
1. Dreamwerverで検索
- レポートの保存
- レポートをスクリプトと同じディレクトリに移動
- search_list.pyを起動

### 用途に合わせて以下の部分を編集してください。  
- dom = xml.dom.minidom.parse("ファイル名")
- for url in dom.getElementsByTagName("取得したいパラメータ"):
- fileName = 'ファイル名'

※DreamwerverCCでの動作のみを確認しています。