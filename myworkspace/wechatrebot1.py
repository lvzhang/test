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
@itchat.msg_register('Text',isGroupChat=True)
def autoReply():
    global  itchat
    # 获取原文本的iterator
    if request.method == 'POST':
        content = request.form['text']
        staus = request.form['staus']
        gnname = request.form['gnname']
    else:
        content = request.args.get('text', default="这个是测试发送消息，!!!!!!!!!!!")
        staus = request.args.get('staus' , default='1')
        gnname = request.args.get('gnname', default="车友群")
    # 登录微信
    itchat.auto_login(hotReload=True)
    allFriendes = itchat.get_friends() #获取所有好友
    # print (len(allFriendes))
    if staus == '0':
        for fs in allFriendes:  #发送朋友消息
            # print (fs['UserName'])
            if fs['NickName'] == 'd':
                print ('发送个人消息')
                result = itchat.send(content, toUserName=fs['UserName'])
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
    userName = ''
    mpsList = itchat.get_chatrooms(update=True)[1:]
    total = 0
    print ("gnname:",gnname)
    for it in mpsList:
        nickname = it['NickName']
        print("len(nickname)",len(nickname))
        if nickname == "公司群":
            userName = it['UserName']
            if staus == '1':
                print ('发送群聊消息！！！')
                result = itchat.send(content, toUserName=userName)  # 发送群聊消息
                return 
        total = total + 1
    print('群聊的数目是%d' % total)

    # 显示所有的群聊，包括未保存在通讯录中的，如果去掉则只是显示在通讯录中保存的
    itchat.dump_login_status()
    chatroomName = userName
    # chatroomName = gnname
    itchat.get_chatrooms(update=True)
    print('chatroomName', chatroomName)
    chatrooms = itchat.search_chatrooms(name=chatroomName)
    print('chatrooms', chatrooms)
    chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
    chatroomstr = chatroom['HeadImgUrl']
    # g = re.search("username=.*\=", chatroomstr)
    re_str = '.*username=(.*)&skey'
    re_pat = re.compile(re_str)
    search_ret = re_pat.search(chatroomstr)

    if search_ret:
        str = search_ret.groups()
        userName = str[0]

    print (chatroomstr)

    print (userName)
    print ('content', content)
    print ('staus1', staus)
    if staus == '1':
        print ('发送群聊消息！！！')
        result = itchat.send(content, toUserName=userName) #发送群聊消息

    if chatrooms is None:
        print('没有找到群聊：' + chatroomName)
    else:
        chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
        for friend in chatroom['MemberList']:
            friend = itchat.search_friends(userName=friend['UserName'])
            # 如果是演示目的，把下面的方法改为 print 即可
            # print (friend)
            # itchat.send(content % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
            # time.sleep(.5)

    friend = itchat.search_friends(nickName="d")
    # print (friend)
    # mpsList = itchat.get_chatrooms(update=True)[1:]

    # userName = "@8d9ca2debf960bc91dfc221e1c5346af"
    # userName = "@29607212c2471b3b8920f3f401d42c7ff34dc2a884f4c63362ccf7ab22c196b4"
    # result = itchat.send("test，!!!!!!!!!!!", toUserName=userName)
    print ("成功！！！！！")
    return "成功发送消息！！！"
    # for it in mpsList:
    # print(it['UserName'])



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
    default_reply = "@帅哥干嘛"
    if msg["IsAt"]:
        return  tuling_reply or default_reply

if __name__=="__main__":
    # autoReply()
    # print("运行成功！！！")
    # itchat.auto_login(hotReload=True)
    # itchat.run()
    # app.run()
    app.run('0.0.0.0', 80, debug=True)