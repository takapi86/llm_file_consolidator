# LLM File Consolidator

`llm_file_consolidator.py` は、複数のソースコードファイルを1つにまとめ、圧縮して出力ファイルに書き込むツールです。

## 特徴
- 複数のファイルを読み込み、1つのテキストに統合
- テキストの前処理（余分な空白の削除）
- トークン数の計算
- 結果を指定された出力ファイルに書き込み

## 使い方

### 前提条件
- Python 3.x
- 必要なパッケージをインストール:

```sh
pip install tiktoken rich
```

### 実行方法

1. スクリプトを実行し、標準入力からファイルパスを渡します。

以下は llm_file_consolidator.py のためのREADMEです。

2. ファイルパスを標準入力で渡します。

例

```sh
find . -name ".py" | python llm_file_consolidator.py -o output.txt
```

### コマンドライン引数
- `-o`, `--output`: 結果を書き込む出力ファイルのパス（必須）

## スクリプトの概要
- `process_file(file_path)`: ファイルを読み込み、その内容を返します。
- `preprocess_text(text)`: テキスト内の余分な空白を削除します。
- `get_token_count(text)`: テキストをトークン化し、そのトークン数を返します。
- `write_output(output_file, preprocessed_text)`: 前処理されたテキストを出力ファイルに書き込みます。
- `parse_arguments()`: コマンドライン引数を解析します。
- `main()`: 全体の処理を管理します。
