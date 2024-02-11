import sys

import pygame
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw
# from mutagen.mp3 import MP3
from tinytag import TinyTag as tag
from UI.player_ui_ui import Ui_mw_main


class MainClass(qtw.QMainWindow, Ui_mw_main):
    song_path = ''
    folder_path = ''

    songs = {}
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_add_file.clicked.connect(self.song_info)
    
    def song_info(self):
        s_path = qtw.QFileDialog.getOpenFileName()
        file = s_path[0]  # .split('/')[-1]
        print(file)
        # print(tag.is_supported(file))
        info = tag.get(file)
        # print(f'album: {info.album}')
        # print(f'album artist: {info.albumartist}')
        # print(f'artist: {info.artist}')
        # print(f'composer: {info.composer}')
        # print(f'title: {info.title}')
        # print(f'comment: {info.comment}')
        # print(f'duration: {info.duration}')
        # print(f'genre: {info.genre}')
        song = '{} - {} ({})    {}'.format(
            info.artist,
            info.title,
            info.album,
            info.duration
        )
        print(song)

        print(info.bitrate)
        

        # audio = MP3(file)
        # print(audio.info.pprint(), '\n\n')
        # print(mutagen.File(file))




if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec())