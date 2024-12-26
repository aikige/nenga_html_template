#!/usr/bin/env python
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

# Ref: https://chromedevtools.github.io/devtools-protocol/tot/Page/#type-Viewport
class clipViewport:
    def __init__(self, width=378,height=559,x=0,y=0,scale=1):
        self.viewport = {
            'width': width,
            'height': height,
            'x': x,
            'y': y,
            'scale': scale
        }
    def get(self):
        return self.viewport

# Ref: https://qiita.com/hajimejimejime/items/d378be12860718518752
# Chrome の DevTools 機能を使ってスクリーンショットを取得する
def save_screenshot(driver, filename, clip=clipViewport()):
    # スクリーンショット設定
    page_viewport = clip.get()

    # Emulation の設定を page_viewport が収まる画面サイズに変更
    # Ref: https://chromedevtools.github.io/devtools-protocol/tot/Emulation/#method-setDeviceMetricsOverride
    device_metrics = {
        'width': page_viewport['width'] + page_viewport['x'],
        'height': page_viewport['height'] + page_viewport['y'],
        'deviceScaleFactor': page_viewport['scale'],
        'mobile': False
    }
    driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', device_metrics)

    # スクリーンショット取得
    # Ref: https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-captureScreenshot
    screenshot_config = {
        'captureBeyondViewport': False,
        'clip': page_viewport
    }
    base64_image = driver.execute_cdp_cmd("Page.captureScreenshot", screenshot_config)

    # ファイル書き出し
    with open(filename, "wb") as fh:
        fh.write(base64.urlsafe_b64decode(base64_image["data"]))

if __name__ == '__main__':
    from argparse import ArgumentParser

    # コマンドラインオプション
    parser = ArgumentParser()
    parser.add_argument('--width', type=int, default=380)   # 378px + 2px (border)
    parser.add_argument('--height', type=int, default=561)  # 559px + 2px (border)
    parser.add_argument('--x', type=int, default=0)
    parser.add_argument('--y', type=int, default=0)
    parser.add_argument('-o', '--output', type=str, default='screenshot.png')
    parser.add_argument('filename', type=str)
    args = parser.parse_args()

    # driver 向けオプション
    options = Options()
    options.add_argument('--headless')
    #options.add_argument('--window-size=380,561')
    # driver生成
    with webdriver.Chrome(options=options) as driver:
        driver.maximize_window()
        # URLを表示 (MacOS or Linuxの想定)
        driver.get("file://" + os.path.abspath(args.filename))
        # キャプチャ設定の生成
        viewport = clipViewport(args.width, args.height, args.x, args.y)
        # キャプチャ実施
        save_screenshot(driver, args.output, clip=viewport)
