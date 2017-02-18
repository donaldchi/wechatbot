#!/usr/bin/env python
# coding: utf-8
import itchat, time
from itchat.content import *
import requests
import json

tuling_key = "b2ddb652ec774191997d6453c78c23ca"

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
	text = response_from_tuling(msg['Text'])
	itchat.send('%s: %s' % ("Bot龙", text), msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
	msg['Text'](msg['FileName'])
	return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
	itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
	itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
	if msg['isAt']:
		itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

#send msg to tuling123.com and get the response
def response_from_tuling(text):
	apiUrl = 'http://openapi.tuling123.com/openapi/api'

	data = {
		'key'    : tuling_key, # 如果这个Tuling Key不能用，那就换一个
		'info'   : text, # 这是我们发出去的消息
		'userid' : 'wechat-robot', # 这里你想改什么都可以
	}

	try:
		r = requests.post(apiUrl, data=data).json()
		return r['text']
	except:
		return "我不想说这个话题"


itchat.auto_login(True)
itchat.run()
