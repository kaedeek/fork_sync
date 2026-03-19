# GitHub Fork Sync Script

これは、**Fork**してるリポジトリを一度に同期するスクリプトです。
是非、使ってください～

## Project structure

```plaintext
fork_sync/
├── src/
│   └── main.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Quick Start Guide

```bash
# Clone the repository
git clone https://github.com/kaedeek/fork_sync.git
cd fork_sync

# Install dependencies
pip install -r requirements.txt
```

## Setting

- [Developer Settings](https://github.com/settings/developers) にアクセス

- **Personal access tokens** をタップして **Tokens (classic)** をタップ

- **scopes** の **repo** をタップしTokenを生成

```python
# ===== 設定 =====
TOKEN = "生成したTokenをセット"
BRANCH_OVERRIDE = None
# =================
```