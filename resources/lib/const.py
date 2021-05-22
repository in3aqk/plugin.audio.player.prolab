import xbmcaddon
import xbmc
import sys

# True debug on kodi.log
debug = True

# Plugin constants
__id__ = "plugin.audio.player.prolab"
ADDON = xbmcaddon.Addon(id=__id__)
__plugin__ = ADDON.getAddonInfo('name')
__author__ = "Paolo Mattiolo"
__url__ = "Proloab S.r.l."
__platform__ = "xbmc media center, [LINUX,WIN32]"
__date__ = "2021"
__version__ = ADDON.getAddonInfo('version')


# Resolves path to where plugin settings and cache will be stored
addonProfilePath = xbmc.translatePath(ADDON.getAddonInfo('profile')).decode('utf-8')
# Resolves path to where plugin i located
addonPath = xbmc.translatePath(ADDON.getAddonInfo('path')).decode('utf-8')

valid_music_ext = ['.mp3','.aac','.wav','.flac','.wma','.ogg']

