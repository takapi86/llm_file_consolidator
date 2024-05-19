import sys
import tiktoken
import re
import argparse
from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn, TimeRemainingColumn

def process_file(file_path):
    try:
        with open(file_path, "r", encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return ""

def preprocess_text(text):
    return re.sub(r"\s+", " ", text).strip()

def get_token_count(text):
    enc = tiktoken.get_encoding("cl100k_base")
    disallowed_special = enc.special_tokens_set - {''}
    tokens = enc.encode(text, disallowed_special=disallowed_special)
    return len(tokens)

def write_output(output_file, preprocessed_text, file_path):
    with open(output_file, "a", encoding="utf-8") as f:
        header = f"\n# {'-' * 3}\n"
        header += f"# Filename: {file_path}\n"
        header += f"# {'-' * 3}\n\n"
        full_text = header + preprocessed_text
        f.write(full_text)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process and compress source code files.")
    parser.add_argument('-o', '--output', type=str, required=True, help="Output file to write results to.")
    return parser.parse_args()

def main():
    args = parse_arguments()
    console = Console()

    for line in sys.stdin:
        file_path = line.strip()
        if file_path:
            console.print(f"Processing file: {file_path}")
            file_content = process_file(file_path)
    preprocessed_text = preprocess_text(file_content)
    compressed_token_count = get_token_count(preprocessed_text)
    console.print(f"Compressed token count: {compressed_token_count}")
    write_output(args.output, preprocessed_text, file_path)

    console.print(f"\n[bright_green]Results written to {args.output}[/bright_green]")

if __name__ == "__main__":
    main()
