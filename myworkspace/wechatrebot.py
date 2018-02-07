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
import re
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')         #改变标准输出的默认编码

KEY = "19a7dd704b5640bdaafb1fd758cb6c9e"
UID = "微信机器人"
from urllib.parse import urlparse
def qs(url):
    query = urlparse(url).params
    print(query)
    print("222222222222222222222222222222222222222222")
    return dict([(k,v[0]) for k,v in urlparse.parse_qs(query).items()])

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

from flask import Flask,request

app = Flask(__name__)
@app.route('/wechat',methods=['POST','GET'])
def autoReply():
    # 获取原文本的iterator
    if request.method == 'POST':
        content = request.form['text']
        staus = request.form['staus']
        gnname = request.form['gnname']
    else:
        content = request.args.get('text', default="未保存至通讯录的群聊消息！")
        staus = request.args.get('staus' , default='1')
        gnname = request.args.get('gnname', default="公司群")
    # 登录微信
    itchat.auto_login(hotReload=True)
    print("gnname", gnname)
    gnname = gnname.replace("%2B",'+')
    print("gnname1",gnname)
    # print (len(allFriendes))
    if staus == '0':
        allFriendes = itchat.get_friends() #获取所有好友
        for fs in allFriendes:  #发送朋友消息
            # print (fs['UserName'])
            if fs['NickName'] == gnname:
                itchat.send(content, toUserName=fs['UserName'])
                return "成功发送消息！！！"
    # 显示所有的群聊，包括未保存在通讯录中的，如果去掉则只是显示在通讯录中保存的
    # itchat.dump_login_status()
    # mpsList = itchat.get_chatrooms(update=True)[1:] #获取群组
    # 获取名字中含有特定字符的群聊，返回值为一个字典的列表
    # lists = itchat.search_chatrooms(name='LittleCoder')
    # print (lists)
    # for it in mpsList:
    #     print('群聊',it)

    # print (22222222222222222222222222222)
    # memberList = itchat.update_chatroom('22') #传入群聊的UserName，返回特定群聊的用户列表
    # print (len(memberList))
    # for nt in memberList:
    #     print (nt['NickName'])
    # else:
    #     mpsList = itchat.get_chatrooms(update=True)[1:]
    #     # total = 0
    #     for it in mpsList:
    #         print(it['UserName'])
    #     total = total + 1
    # print('群聊的数目是%d' % total)

    # 显示所有的群聊，包括未保存在通讯录中的，如果去掉则只是显示在通讯录中保存的
    # itchat.dump_login_status()
    # REAL_SINCERE_WISH = u'祝%s 新年快乐！！'
    # chatroomName = '车友群'
    else:
        itchat.get_chatrooms(update=True)
        mpsList = itchat.get_chatrooms(update=True)[1:]  # 获取群组

        for group in mpsList:
            if group['NickName'] == gnname:
                chatrooms = itchat.search_chatrooms(name=gnname)
                chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
                chatroomstr = chatroom['HeadImgUrl']
                # g = re.search("username=.*\=", chatroomstr)
                re_str = '.*username=(.*)&skey'
                re_pat = re.compile(re_str)
                search_ret = re_pat.search(chatroomstr)
                userName = ''
                if search_ret:
                    str = search_ret.groups()
                    userName = str[0]

                # m = re.match("^user name(.*?)=$", chatroomstr)
                # re.match()
                # print ('5555555555555',m)
                # if m:
                # print ("Match:" + m.group(0))

                # userName = '@@c04dda89aa2d4cacf9835423f1a237a75d91b8afaf4db6e95dbb8b5292610aa2&skey'
                itchat.send(content, toUserName=userName) #发送群聊消息
                return "成功发送消息！！！"

        return '没有找到群聊：'+gnname+"！请先保存到通讯录"

#单聊的机器人
@itchat.msg_register('Text')
def single_replay(msg):
    tuling_reply = get_replay(msg["Text"])
    print(tuling_reply)
    return  tuling_reply
    # return  "你好"
    # 自己实现问答
    # return  "[自动回复]您好，我正忙，一会儿再联系您！！！"

#群聊的机器人
@itchat.msg_register('Text',isGroupChat=True)
def group_replay(msg):
    tuling_reply = get_replay(msg["Text"])
    # default_reply = "@帅哥干嘛"
    if msg["IsAt"]:
        return  tuling_reply or default_reply

if __name__=="__main__":
    # autoReply()
    # print("运行成功！！！")
    # itchat.auto_login(hotReload=True)
    # itchat.run()
    # app.run()
    app.run('0.0.0.0', 80, debug=True)