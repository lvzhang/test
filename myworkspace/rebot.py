#!/user/bin/env python
#_*_ coding=utf-8 *_*
"""
Function:智能聊天机器人
Date:2015/05/26
Author:lvzhang
ChangeLog:v0.1 init
"""
# APIKey:72579859d2b1443f90475458303a333c
# Name:lvzhang
# http://www.tuling123.com/openapi/api

import requests
import itchat

# KEY = "72579859d2b1443f90475458303a333c"
# UID = "君君"
KEY = "19a7dd704b5640bdaafb1fd758cb6c9e"
UID = "微信机器人"

def get_replay(msg):
    # api_tuling = "http://www.tuling123.com/openapi/api"
    api_tuling = "http://www.tuling123.com/openapi/api"
    data ={
    'key': KEY,
    'info': msg,
    'userid':UID
    }
    try:
        print(11111111111)
        ret = requests.post(api_tuling,data=data).json()
        # return  "我是超人1111"
        return  ret.get('text')

    except:
        return 111
    # 自己实现问答

#单聊的机器人
@itchat.msg_register('Text')
def single_replay(msg):
    tuling_reply = get_replay(msg["Text"])
    print(tuling_reply)
    return  tuling_reply
    return  "你好"

    # 自己实现问答
    # return  "[自动回复]您好，我正忙，一会儿再联系您！！！"

#群聊的机器人
@itchat.msg_register('Text',isGroupChat=True)
def group_replay(msg):
    tuling_reply = get_replay(msg["Text"])
    default_reply = "@帅哥干嘛"
    if msg["IsAt"]:
        return  tuling_reply or default_reply

if __name__=="__main__":
    print("运行成功！！！")
    itchat.auto_login(hotReload=True)
    itchat.run()