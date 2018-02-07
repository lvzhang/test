#!/user/bin/env python
#_*_ coding=utf-8 *_*
"""
Function:微信消息自动回复
Date:2015/05/26
Author:lvzhang
ChangeLog:v0.1 init
"""
import itchat

@itchat.msg_register('Text')
def text_replay(msg):
    # 自己实现问答
    print("已经自动回复")
    return  "[自动回复]您好，我正忙，一会儿再联系您！！！"

if __name__=="__main__":
    print("运行成功！！！")
    itchat.auto_login(hotReload=True)
    itchat.run()


