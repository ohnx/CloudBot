import time
from util import hook


# CTCP responses
@hook.regex(r'^\x01VERSION\x01$')
def ctcp_version(notice=None):
    notice('\x01VERSION: CloudBot - http://git.io/cloudbotirc')


@hook.regex(r'^\x01PING\x01$')
def ctcp_ping(notice=None):
    notice('\x01PING: PONG')


@hook.regex(r'^\x01TIME\x01$')
def ctcp_time(notice=None):
    notice('\x01TIME: The time is: %s' % time.strftime("%r", time.localtime()))
