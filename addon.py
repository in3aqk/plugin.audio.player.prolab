#!/usr/bin/env python
# -*- coding: utf-8 -*-


#https://kodi.wiki/view/HOW-TO:Audio_addon
#https://github.com/zag2me/plugin.audio.example/blob/master/default.py

import xbmcplugin
import xbmcgui
import sys

from resources.lib import utils
from resources.lib import const
addon_handle = None


def getFiles():
    song_list = []
    songs = [{
         'album_cover': 'blabla1',
         'title': 'title1',
         'url': 'aaaa'
        },
        {
         'album_cover': 'blabla2',
         'title': 'title2',
         'url': 'aaaa'
        }]
    
    

    for song in songs:        
        utils.addon_log(const.debug, song)
        li = xbmcgui.ListItem(label=song['title'], thumbnailImage=song['album_cover'])
        li.setProperty('fanart_image', song['album_cover'])        
        li.setProperty('IsPlayable', 'true')                
        song_list.append((song['url'], li, False))

    utils.addon_log(const.debug, song_list)

    xbmcplugin.addDirectoryItems(addon_handle, song_list, len(song_list))
    # set the content of the directory
    xbmcplugin.setContent(addon_handle, 'songs')
    xbmcplugin.endOfDirectory(addon_handle)



def main():
    getFiles()


if __name__ == '__main__':
    addon_handle = int(sys.argv[1])
    utils.addon_log(const.debug, "Main")
    main()
    
