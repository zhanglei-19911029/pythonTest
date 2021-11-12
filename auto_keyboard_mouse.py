# 微信自动化发信息
import json

import pyautogui
import pyperclip
from datetime import datetime

import requests
from apscheduler.schedulers.blocking import BlockingScheduler


# blocking类型调度器会阻塞当前进程，若想要后台运行的调度器，可以使用以下代码：
# from apscheduler.schedulers.background import BackgroundScheduler as BlockingScheduler

def hot_song():
    api_url = f'https://api.uomg.com/api/rand.music?sort=热歌榜&format=json'  # 选择输出分类[热歌榜，新歌榜，飙升榜，抖音榜，电音榜]，为空输出热歌榜
    # api_url = 'https://api.66mz8.com/api/rand.music.163.php'  # 随机歌曲
    # api_url = 'https://api.66mz8.com/api/music.163.php?format=json'  # 网易云热评
    # api_url = f'https://api.uomg.com/api/rand.music?sort=热歌榜&format=json'
    r = requests.get(api_url)
    return r.json().get('data', '')


def love_word():
    api = 'https://api.vvhan.com/api/love'
    # api = 'https://api.mcloc.cn/love'
    res = requests.get(api).text
    return res


def rainbow():
    api = 'https://chp.shadiao.app/api.php'
    res = requests.get(api).text
    return res


def ma_ren():
    api = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'
    res = requests.get(api).text
    return res


def main():
    pyautogui.PAUSE = 0

    icon_position = pyautogui.Point(x=1398, y=1045)  # 任务栏图标位置
    entry_position = pyautogui.Point(x=923, y=758)  # 输入框位置

    pyautogui.moveTo(icon_position, duration=1)  # duration为执行时长，可选
    pyautogui.click(icon_position)
    pyautogui.moveTo(entry_position, duration=0.7)
    pyautogui.click(entry_position)
    speak = love_word()
    speak = json.dumps(speak, ensure_ascii=False)
    pyperclip.copy(speak)
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.press('enter')

    # pyautogui.typewrite(
    #     [*list('zhengzai '), *list('jinxing '), 'shift', *list('pyautogui'), 'shift', *list('shiyan '), 'enter'],
    #     0.1)  # 第一个参数是输入文本，第二个是输入每个字符的间隔时间


if __name__ == '__main__':
    # print(pyautogui.position())  # 将鼠标放在输入框上，运行以下语句，获取此时光标的坐标
    main()
    # scheduler = BlockingScheduler()  # 实例化
    # scheduler.add_job(main, 'date', run_date=datetime(2021, 11, 1, 12, 00, 00))  # 添加任务
    # scheduler.add_job(main, 'interval', start_date='2021-11-9 11:40:15', end_date='2021-11-9 14:42:15',
    #                   seconds=1, max_instances=10)
    # scheduler.start()
    # test = love_word()
    # print(test)
