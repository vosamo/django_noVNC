__author__ = 'liushaolin'
# coding=utf-8
import os
from multiprocessing import Process
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_noVNC.settings")
from django.conf import settings

def worker():
    '''
        Multi process service VNC start
    '''

    dir_path = os.path.dirname(__file__)

    websockify_path = os.path.join(dir_path, 'vnc', 'utils', 'websockify', 'websockify')
    web_path = os.path.join(dir_path, 'vnc')
    target_path = os.path.join(dir_path, 'vnc', 'vnc_tokens')

    cmd = u'python %s --web=%s --target-config=%s %s' %(websockify_path, web_path, target_path, settings.VNC_PROXY_PORT)

    os.system(cmd)

def start_websockify():
    '''
        Start the VNC agent service
        ./utils/websockify/websockify --web=. --target-config=vnc_tokens 6080
        {'target_cfg': '/home/xiaofei/work/noVNC/vnc_tokens', 'listen_port': 6080}
    '''

    print u'start vnc proxy..'

    t = Process(target=worker, args=())
    t.start()

    print u'vnc proxy started..'

if __name__ == '__main__':
    start_websockify()