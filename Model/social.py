import time

from . import message_pb2
from . import base


class SocialMessage(base.Base):
    def __init__(self):
        self.instance = message_pb2.SocialMessage()

    def format_content(self):
        return self.user().nickname + ' 关注了主播'

    def __str__(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '【关注】' + self.format_content()
