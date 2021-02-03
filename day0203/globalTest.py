"""
name='ハサキ'
def change_name():
    name='浅木'
def hello():
    print('こんにちは'+name+'。')
change_name()
hello()
"""
name='ハサキ'
def change_name():
    global name
    name='浅木'
def hello():
    print('こんにちは'+name+'。')
change_name()
hello()
