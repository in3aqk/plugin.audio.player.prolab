#!/usr/bin/env python
# -*- coding: utf-8 -*-


#https://kodi.wiki/view/HOW-TO:Audio_addon
#https://github.com/zag2me/plugin.audio.example/blob/master/default.py

import xbmc
import xbmcplugin
import xbmcgui
import sys

from resources.lib import playlist
from resources.lib import utils
from resources.lib import const
addon_handle = None
song_list = []

def get_list():

    music_directory = playlist.get_file_list()
    utils.addon_log(const.debug, music_directory)
    if len(music_directory):


        for item in music_directory:
            #utils.addon_log(const.debug, item)
            li = xbmcgui.ListItem(label="--     {}     --".format(item['folder_name']), thumbnailImage=item['folder_thumb'])
            li.setProperty('fanart_image', item['folder_thumb'])
            li.setProperty('IsPlayable', 'false')
            li.setIsFolder(True)
            song_list.append(("", li, True))
            songs = item['folder_content']['songs']
            for song in songs:
                li = xbmcgui.ListItem(label=song['name'], thumbnailImage=song['song_thumb'])
                li.setProperty('fanart_image', song['song_thumb'])
                li.setProperty('IsPlayable', 'true')
                li.setIsFolder(False)
                url = "{}/{}".format(item['folder_path'],song['filename'])
                song_list.append((url, li, False))



        xbmcplugin.addDirectoryItems(addon_handle, song_list, len(song_list))
        # set the content of the directory
        xbmcplugin.setContent(addon_handle, 'songs')
        xbmcplugin.endOfDirectory(addon_handle)
    else:
        # No usb key found, fakes the list
        li = xbmcgui.ListItem(label="KEY NOT FOUND", thumbnailImage="")
        li.setProperty('IsPlayable', 'false')
        li.setIsFolder(True)
        song_list.append(("", li, True))
        xbmcplugin.addDirectoryItems(addon_handle, song_list, len(song_list))
        xbmcplugin.setContent(addon_handle, 'songs')
        xbmcplugin.endOfDirectory(addon_handle)
        xbmc.executebuiltin("Notification(USB KEY,Insert usb key,10000)")



def main():
    get_list()


if __name__ == '__main__':
    addon_handle = int(sys.argv[1])
    main()

