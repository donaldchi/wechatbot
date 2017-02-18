import itchat

newInstance = itchat.new_instance()
newInstance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl')

@newInstance.msg_register(TEXT)
def reply(msg):
    return msg['Text']

newInstance.run()
