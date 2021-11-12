from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


# 定义自己要执行的command
@manager.command
def test():
    print(u'test run')


# if __name__ == '__main__':
#     manager.run()
