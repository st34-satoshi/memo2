# pgnファイルを読んでブランダーを見つける
pgnファイルから複数の対局を探す
条件を指定してブランダーを探せる
- 下がった評価値
- 下がった後の評価値
- ブランダーを指したプレーヤーのレーティングの幅
- 相手のレーティングの幅
- ブランダーの手数の範囲: オープニングだけなら0~10とか？

## 開発
### 準備
data/に分析したい.pgnファイルを用意する

### 実行
- `pip install -r requirements.txt`
- `python main.py`: 対局の分析に時間がかかる.3局の分析に1分かかる(14局で5分くらいだった)

### 結果
blunder/にpng画像で出力される。{white-black-手数-直前の1手}.pgn