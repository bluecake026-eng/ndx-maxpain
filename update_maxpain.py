name: Update NDX Max-Pain

on:
  schedule:
    # 20:35 ET Mo-Fr  (00:35 UTC next day)
    - cron: '35 0 * * 2-6'
  workflow_dispatch:   # manual button

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v4
        with: { python-version: '3.11' }

      - run: pip install yfinance pandas

      - run: python update_maxpain.py

      - name: commit + push
        run: |
          git config user.name  github-actions
          git config user.email github-actions@github.com
          git add ndx_maxpain.txt
          git diff --quiet HEAD || (git commit -m "maxpain $(date -Iseconds)" && git push)
