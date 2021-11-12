import os
import traceback

import requests
import itchat
import random
from itchat.content import *
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


def tianxing_ai(info):
    apiUrl = 'http://api.tianapi.com/txapi/robot/index'
    parm = {
        'key': '3ce5c4497faa08a36e8c55d26c8ef252',
        'question': info
    }
    r = requests.get(apiUrl, params=parm).json()
    return r['newslist'][0]['reply']


def tianxing_tuling(info):
    apiUrl = 'http://api.tianapi.com/txapi/tuling/index'
    parm = {
        'key': '3ce5c4497faa08a36e8c55d26c8ef252',
        'question': info
    }
    r = requests.get(apiUrl, params=parm).json()
    return r['newslist'][0]['reply']


def moli_ai(msg):
    apiUrl = f'http://i.itpk.cn/api.php?question={msg}'
    r = requests.get(apiUrl)
    return r.text


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '8edce3ce905a4c1dbb965e6b35c3834d',
        'info': msg,
        'userid': 'wechat-robot',
    }

    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return


def quest_answer(info=None):
    apiUrl = 'https://api.jisuapi.com/iqa/query'
    parm = {
        'appkey': '4987b9db578d1686',
        'question': info
    }
    r = requests.get(apiUrl, params=parm).json()
    return r["result"]["content"]


def ai_free(info=None):
    apiUrl = 'http://api.qingyunke.com/api.php'
    parm = {
        'key': 'free',
        'appid': 0,
        'msg': info
    }
    r = requests.get(apiUrl, params=parm).json()
    return r["content"]


def ci_ai(info=""):
    """
    应用名称:
    zhizhang
    APPID:
    1615272865940
    APIKey:
    PCYNGADYAOXZRLO78Y3W51YPJS8KB86OHC6O94VNOHM5QD668H
    APISecret:
    PCYNGADYAOXZRLO78Y3W51YPJS8KB86OHC6O94VNOHM5QD668H
    """
    apiUrl = 'http://www.weilaitec.com/cigirlrobot.cgr'
    parm = {
        'key': 'PCYNGADYAOXZRLO78Y3W51YPJS8KB86OHC6O94VNOHM5QD668H',
        'appid': 1615272865940,
        'ip': '10.225.10.45',
        'userid': 'zhizhang',
        'msg': info
    }
    r = requests.post(apiUrl, data=parm).text
    return r


def love_word():
    api = 'https://api.vvhan.com/api/love'
    res = requests.get(api).text
    return res


def joker():
    api = 'https://api.vvhan.com/api/xh'
    res = requests.get(api).text
    return res


def sao_word():
    api = 'https://api.vvhan.com/api/sao'
    res = requests.get(api).text
    return res


def zhe_li():
    api = 'https://api.vvhan.com/api/ian'
    res = requests.get(api).text
    return res


def weather_jpg():
    api = 'https://api.vvhan.com/api/ip'
    res = requests.get(api)
    return res.content


def weather(msg=None):
    api = 'https://api.vvhan.com/api/weather'
    res = requests.get(api, params=msg).json()
    return res


def ma_ren():
    api = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'
    res = requests.get(api).text
    return res


def rainbow():
    api = 'https://chp.shadiao.app/api.php'
    res = requests.get(api).text
    return res


def get_reply_res(msg):
    try:
        if msg:
            message = str(msg['Text']).strip()
            # nick_name = itchat.search_friends(userName=msg['FromUserName'])['NickName']  # 获取微信用户名
            # print("%s:%s" % (nick_name, message))
            if str(msg['Text']).strip() == '笑话' or str(msg['Text']).strip() == '1':
                reply = joker()  # 笑话
            elif str(msg['Text']).strip() == '骚话' or str(msg['Text']).strip() == '2':
                reply = sao_word()
            elif str(msg['Text']).strip() == '天气' or str(msg['Text']).strip() == '3':
                try:
                    res = weather()
                    reply = res["city"] + ' ' + res["info"]['date'] + ' ' + res["info"]['type'] + " " + res["info"][
                        "high"] + " " + res["info"][
                                "low"] + " " + res["info"]["fengxiang"] + " " + res["info"]["fengli"] + "\n" + \
                            res["info"][
                                "tip"]
                except:
                    reply = """杭州 11日星期四 小雨 高温 12℃ 低温 9℃ 东南风 1级
                               感冒多发期，适当减少外出频率，多喝热水，适当增减衣物"""
            elif str(msg['Text']).strip() == '骂人' or str(msg['Text']).strip() == '4':
                reply = ma_ren()
            elif str(msg['Text']).strip() == '夸人' or str(msg['Text']).strip() == '5':
                reply = rainbow()
            elif str(msg['Text']).strip() == '情话' or str(msg['Text']).strip() == '6':
                reply = love_word()
            else:
                try:
                    reply = ai_free(message)
                    if str(reply).strip() == '' or reply.startswith('参数有误'):
                        reply = tianxing_ai(message)
                except:
                    reply = tianxing_tuling(message)
            try:
                return reply
            except:
                result = ai_free(message)
                return result
    except:
        print(traceback.format_exc())
        print('text error')


# 这里实现微信消息的获取
@itchat.msg_register(TEXT, isFriendChat=True)
def tuling_reply(msg):
    return get_reply_res(msg)


@itchat.msg_register([MAP, CARD, NOTE, SHARING, PICTURE,
                      RECORDING, VOICE, ATTACHMENT, VIDEO, FRIENDS, SYSTEM], isFriendChat=True)
def test(msg):
    try:
        if msg:
            reply = love_word()
            return reply
    except:
        print('other error')


test_list = [1]


# def img():
# coding=utf8
# room = itchat.search_friends(name=r'张')  # 这里输入你好友的名字或备注。
# print(room)
# userName = room[0]['UserName']
# f = "C:\文件/lh.jpg"  # 图片地址

# print(res)
# try:
#     itchat.send_image(f, toUserName=userName)
#     print("success")
# except:
#     print("fail")


@itchat.msg_register([TEXT], isGroupChat=True)
def group_test(msg):
    try:
        message = str(msg['Text']).strip().split()
        print('group_test', message)
        if len(message) < 2:
            res = love_word()
        else:
            res = ai_free(message[-1])
            if res.startswith('参数有误') or str(res).strip() == '':
                res = tianxing_tuling(message[-1])
            path = r'C:\Users\zhanglei02\Desktop\图标\media'
            res = os.listdir(path)
            f = os.path.join(path, random.choice(res))
            if message[-1] == '图片' and msg.isAt:
                itchat.send_image(f, toUserName=msg['FromUserName'])
                return
        if msg.isAt:
            itchat.send(u'@%s\u2005 %s ' % (msg['ActualNickName'], res), toUserName=msg['FromUserName'])
        # else:
        #     print(1231)
        #     itchat.send(u'%s ' % res, toUserName=msg['FromUserName'])
    except:
        print('group_test error')


itchat.auto_login(hotReload=True)
itchat.run()

# img()
