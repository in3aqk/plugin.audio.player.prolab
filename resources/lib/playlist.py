
from posixpath import split
from resources.lib import utils
from resources.lib import const
import os



def get_file_list():
    music_directory = []

    for dirpath, dirs, files in os.walk("/media/pi/"):
        songs_arr = []
        music_found = False
        for filename in files:
            ext = os.path.splitext(filename)[1]
            if ext in const.valid_music_ext:
                song_detail = {
                    'name' : os.path.splitext(os.path.basename(filename))[0],
                    'filename': filename,
                    'song_thumb':utils.get_random_thumb()
                }
                songs_arr.append(song_detail)
                music_found = True

            fname = os.path.join(dirpath,filename)


        if music_found:

            folder = {
                'folder_path':dirpath,
                'folder_thumb':utils.get_random_thumb(),
                'folder_name':  get_folder_name(dirpath),
                'folder_content': {
                    'songs': songs_arr
                }
            }
            music_directory.append(folder)
    return music_directory


def get_folder_name(path):
    return os.path.split(path)[-1]