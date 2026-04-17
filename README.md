# Mark1 (NumPy Transformer)

このリポジトリは、NumPyで実装した最小構成のDecoder-only Transformer言語モデルです。

## 前提環境
- Python 3.10+
- NumPy

インストール例:

```bash
python -m venv .venv
source .venv/bin/activate
pip install numpy
```

## model の実行方法

`main.py` を実行すると、プロンプトを入力にしてモデルの forward と簡易生成を行います。

### 最小実行例

```bash
python main.py --prompt "こんにちは、Mark1"
```

### 主なオプション

- `--max-new-tokens` : 生成する最大トークン数（デフォルト: `12`）
- `--temperature` : 生成温度（`0.0` で greedy、デフォルト: `0.0`）
- `--seed` : 乱数シード（デフォルト: `42`）
- `--d-model` : 埋め込み次元（デフォルト: `64`）
- `--n-heads` : ヘッド数（デフォルト: `4`）
- `--n-layers` : 層数（デフォルト: `2`）
- `--d-ff` : FFNの中間次元（デフォルト: `128`）
- `--max-seq-len` : 最大シーケンス長（デフォルト: `128`）
- `--log-dir` : 実行ログ(JSONL)の保存先（デフォルト: `logs`）
- `--run-id` : 任意の実行ID

例:

```bash
python main.py \
  --prompt "transformerの挙動を確認したい" \
  --max-new-tokens 16 \
  --temperature 0.7 \
  --seed 123
```

## 学習デモの実行方法

最小の学習デモ（LM headバイアス更新のみ）は次で実行できます。

```bash
python train_min.py
```

