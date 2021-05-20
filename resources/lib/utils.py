import xbmc
import const
import os
from traceback import format_exc, print_exc
import time


"""
Write a debug string on the kodi.log
"""

def addon_log(debug, string):
    if debug:
        try:
            if not isinstance(string, str):
                string = str(string)
            msg = string.decode("utf-8", 'ignore')
            xbmc.log("[%s-%s]: %s " % (const.__plugin__, const.__version__, msg.encode('utf-8', 'ignore')), level=xbmc.LOGNOTICE)
        except:
            print_exc()


