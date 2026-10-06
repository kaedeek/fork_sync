# GitHub Fork Sync Script

This is a script that allows you to sync multiple **forked** repositories at once.

Feel free to give it a try! 🚀

[Japanese](README-JP.md)

## Project structure

```plaintext
fork_sync/
├── src/
│   └── main.py
├── .env
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

- [**.env**](.env) ファイルに下記のように記載

```
TOKEN= <生成したトークン>
```