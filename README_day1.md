# Mark1 Day1 運用メモ

## 固定したI/O仕様
- 入力: `python main.py --prompt "..."`
- 内部表現:
  - `tokens`: 文字単位
  - `token_ids`: `List[int]`
  - `seq_len`: `len(token_ids)`
- 出力:
  - 標準出力に `input_text`, `tokens`, `token_ids`, `decoded_text`, `seq_len`
  - `logs/run_YYYYMMDD.jsonl` に1実行1行のJSONL

## tokenizer仕様
- 文字単位 tokenizer
- 特殊トークン: `<PAD>`, `<UNK>`, `<BOS>`, `<EOS>`
- `encode`: デフォルトで BOS/EOS を付与
- `decode`: デフォルトで特殊トークンを除外

## ログ仕様（Day1固定）
以下のキーを必須とする:
- `ts`, `run_id`, `stage`
- `input_text`
- `seq_len`, `token_count`
- `token_ids`
- `notes`
