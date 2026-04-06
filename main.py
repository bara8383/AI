from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


from tokenizer import CharTokenizer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Mark1 Day1: prompt -> token ids -> text")
    parser.add_argument("--prompt", type=str, help="Input text (UTF-8)")
    parser.add_argument(
        "--log-dir",
        type=Path,
        default=Path("logs"),
        help="Directory to store JSONL logs (default: logs)",
    )
    parser.add_argument(
        "--run-id",
        type=str,
        default=None,
        help="Optional run id. Auto-generated if omitted.",
    )
    return parser


def append_jsonl(log_dir: Path, payload: dict) -> Path:
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"run_{datetime.now(timezone.utc):%Y%m%d}.jsonl"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    return log_path


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not args.prompt:
        parser.print_help()
        return 0

    run_id = args.run_id or f"day1_{uuid4().hex[:8]}"

    tokenizer = CharTokenizer.build_vocab([args.prompt])
    token_ids = tokenizer.encode(args.prompt, add_bos_eos=True)
    restored_text = tokenizer.decode(token_ids, skip_special_tokens=True)

    seq_len = len(token_ids)

    print("=== Mark1 Day1 I/O ===")
    print(f"input_text   : {args.prompt}")
    print(f"tokens       : {list(args.prompt)}")
    print(f"token_ids    : {token_ids}")
    print(f"decoded_text : {restored_text}")
    print(f"seq_len      : {seq_len}")

    log_row = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "run_id": run_id,
        "stage": "tokenize",
        "input_text": args.prompt,
        "seq_len": seq_len,
        "token_count": seq_len,
        "token_ids": token_ids,
        "notes": "char-level tokenizer",
    }
    log_path = append_jsonl(args.log_dir, log_row)
    print(f"log_file     : {log_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
