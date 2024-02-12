import os
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
        self.pb_add_file.clicked.connect(self.add_song)
        self.pb_add_folder.clicked.connect(self.add_songs)
    
    def add_songs(self):
        s_path = qtw.QFileDialog.getExistingDirectory()
        for x in os.listdir(s_path):
            print(x)

        

    
    def add_song(self):
        s_path = qtw.QFileDialog.getOpenFileName()
        file = s_path[0]  # .split('/')[-1]
        # print(file)
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
            self.song_time(info.duration)
        )
        self.scrollAreaWidget.layout().addWidget(qtw.QLabel(song))

        
        # self.scrollArea.setVerticalScrollBarPolicy()
        # self.lb_song.setText(song)
        # print(song)
    
    def song_time(self, inf):
        hours = int(inf // 3600)
        hour_other = inf % 3600

        mins = int(hour_other // 60)
        mins_other = hour_other % 60

        seconds = int(mins_other % 60)

        time_took = '{}:{}:{}'.format(
            hours if hours > 10 else '0' + str(hours),
            mins if mins > 10 else '0' + str(mins),
            seconds if seconds > 10 else '0' + str(seconds)
            )
        return time_took




if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec())