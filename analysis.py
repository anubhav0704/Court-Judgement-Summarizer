import os
import glob
from collections import Counter
import statistics

# 👉 Change this when needed (optional)
DATA_DIR = "/content/data"  # Colab-friendly path

def analyze_files():
    if not os.path.exists(DATA_DIR):
        print("Data directory not found. Skipping analysis.")
        return

    files = glob.glob(os.path.join(DATA_DIR, "*.txt"))
    print(f"Found {len(files)} files.")

    total_words = []
    total_lines = []
    vocab = Counter()

    for fpath in files:
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            lines = [l.strip() for l in f if l.strip()]
            words = " ".join(lines).split()

            total_words.append(len(words))
            total_lines.append(len(lines))
            vocab.update([w.lower() for w in words])

    print(f"Avg Words: {statistics.mean(total_words):.2f}")
    print(f"Avg Lines: {statistics.mean(total_lines):.2f}")
    print(f"Vocab Size: {len(vocab)}")
    print(f"Top 10 words: {vocab.most_common(10)}")

if __name__ == "__main__":
    analyze_files()

