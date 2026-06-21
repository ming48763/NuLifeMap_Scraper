#!/usr/bin/env bash
# 發生錯誤時就停止執行
set -o errexit

# 安裝 Python 套件
pip install -r requirements.txt

# 安裝 Playwright 瀏覽器核心與其依賴的系統套件
playwright install chromium


