from VersaLog import *
from dotenv import load_dotenv

import requests
import time
import os

load_dotenv()

logger = VersaLog(enum="detailed", show_tag=True, tag=["GITHUB", "FORK_SYNC"])

# ===== 設定 =====
TOKEN = os.getenv("TOKEN")
BRANCH_OVERRIDE = None
# =================

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}


def get_all_forks():
    forks = []
    page = 1

    while True:
        url = f"https://api.github.com/user/repos?per_page=100&page={page}"

        r = requests.get(url, headers=headers)

        if r.status_code != 200:
            logger.error("Failed to fetch repositories")
            logger.debug(r.text)
            break

        repos = r.json()

        if not repos:
            break

        forks.extend([repo for repo in repos if repo["fork"]])
        page += 1

    return forks


def sync_fork(repo, index, total):
    name = repo["name"]
    owner = repo["owner"]["login"]
    branch = BRANCH_OVERRIDE or repo["default_branch"]

    logger.step(f"Syncing {name}", index, total)

    url = f"https://api.github.com/repos/{owner}/{name}/merge-upstream"

    with logger.timer(name):
        r = requests.post(
            url,
            headers=headers,
            json={"branch": branch}
        )

        if r.status_code == 200:
            logger.info(f"{name} synced")
        elif r.status_code == 204:
            logger.info(f"{name} already up to date")
        else:
            logger.error(f"{name} failed")
            logger.debug(r.text)

    time.sleep(0.5)


def main():
    logger.info("Fork Sync Start")

    forks = get_all_forks()
    total = len(forks)

    logger.info(f"Found {total} forked repositories")

    with logger.timer("Total Sync"):
        for i, repo in enumerate(forks, start=1):
            sync_fork(repo, i, total)

            logger.progress(
                title="Overall Progress",
                current=i,
                total=total
            )

    logger.info("All forks processed")


if __name__ == "__main__":
    main()
