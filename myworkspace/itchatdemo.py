#!/usr/bin/env python
#_*_ coding=utf-8 *_*
"""
    Function:chushi itchat
    Dat:2017/05/26
    Author:cici
    ChangeLog:v0.1 init
"""
import  itchat
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')   #改变标准输出的默认编码
#登录微信
itchat.auto_login(hotReload=True)

#给文件传输助手发消息
itchat.send("你好，filehelper",toUserName="filehelper")

# 給某位好友发消息
allFriendes = itchat.get_friends()
print (allFriendes[0])
friend = itchat.search_friends(nickName="新一")
mpsList=itchat.get_chatrooms(update=True)[1:]
# for it in mpsList:
    # print(it['UserName'])
print (friend)
# print (allFriendes[1]["UserName"])
# userName = allFriendes[0]["UserName"]
# print (userName)
# userName = itchat.get_friends()[1]["UserName"]
# userName = itchat.get_friends()[1]["UserName"]
userName = "@29607212c2471b3b8920f3f401d42c7ff34dc2a884f4c63362ccf7ab22c196b4"
# itchat.send("test，!!!!!!!!!!!",toUserName="@@6701600c7d8bb8ec5899bdce1e9b35c59c947d4acf489b1c6f6bf54bb6e753c8")
result=itchat.send("test，!!!!!!!!!!!",toUserName=userName)
__file__ = "D:/hanlp资料/微信聊天机器人/myworkspace/1.txt"

mpsList = itchat.get_chatrooms(update=True)[1:]
total = 0
for it in mpsList:
    nickname=it['NickName']
    print(len(nickname))
    if nickname=="公司群":
        print ("公司群")
    # print (nickname.decode('utf-8'))
    total = total + 1
print('群聊的数目是%d' % total)

itchat.dump_login_status()
chatroomName = '永远的一家'
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
userName = ''
if search_ret:
    str = search_ret.groups()
    userName = str[0]

print (chatroomstr)
# m = re.match("^user name(.*?)=$", chatroomstr)
# re.match()
# print ('5555555555555',m)
# if m:
# print ("Match:" + m.group(0))

# userName = '@@c04dda89aa2d4cacf9835423f1a237a75d91b8afaf4db6e95dbb8b5292610aa2&skey'
print (userName)
print ('content', content)
print ('staus1', staus)
if staus == '1':
    print ('发送群聊消息！！！')
    result = itchat.send(content, toUserName=userName)  # 发送群聊消息

# path = os.path.abspath(os.path.dirname(__file__))
itchat.send_file(__file__,toUserName=userName)
f="D:/hanlp资料/微信聊天机器人/myworkspace/1.jpg"  #图片地址
# result = itchat.send_image(f,toUserName=userName)
print("成功",result)
