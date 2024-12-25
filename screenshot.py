#!/usr/bin/env python
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from argparse import ArgumentParser

class clipConfig:
    def __init__(self, width=378,height=559,x=0,y=0,scale=1):
        self.config = {
            'width': width,
            'height': height,
            'x': x,
            'y': y,
            'scale': scale
        }
    def get(self):
        return self.config

# Ref: https://qiita.com/hajimejimejime/items/d378be12860718518752
def save_screenshot(driver, filename, clip=clipConfig(), is_full_size=False):
    # スクリーンショット設定
    screenshot_config = {
        # Trueの場合スクロールで隠れている箇所も含める、Falseの場合表示されている箇所のみ
        'captureBeyondViewport': is_full_size,
        'clip': clip.get()
    }

    # スクリーンショット取得
    base64_image = driver.execute_cdp_cmd("Page.captureScreenshot", screenshot_config)

    # ファイル書き出し
    with open(filename, "wb") as fh:
        fh.write(base64.urlsafe_b64decode(base64_image["data"]))

# コマンドラインオプション
parser = ArgumentParser()
parser.add_argument('--width', type=int, default=380)
parser.add_argument('--height', type=int, default=561)
parser.add_argument('--x', type=int, default=0)
parser.add_argument('--y', type=int, default=0)
parser.add_argument('-o', '--output', type=str, default='screenshot.png')
parser.add_argument('filename', type=str)
args = parser.parse_args()

# driver 向けオプション
options = Options()
options.add_argument('--headless')
# driver生成
with webdriver.Chrome(options=options) as driver:
    # URLを表示 (MacOS or Linuxの想定)
    driver.get("file://" + os.path.abspath(args.filename))
    # キャプチャ設定の生成
    clip_config = clipConfig(args.width, args.height, args.x, args.y)
    # キャプチャ実施
    save_screenshot(driver, args.output, clip=clip_config)
