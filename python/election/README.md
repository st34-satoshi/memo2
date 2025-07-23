# 選挙を分析する

## 必要なツール
- [uv](https://docs.astral.sh/uv/)

### 準備
- `uv sync`

## 世代別比例投票先をグラフにする
### 実行
- `uv run main.py`

### 結果
TBA

### データの準備
#### データの完成系
年代別に投票した政党を実際の数値で把握する
TBA jsonファイルを作る

#### 年代別の比例投票先画像から政党ごとの割合を把握する
- `uv run read_voting_percentage_from_image.py`