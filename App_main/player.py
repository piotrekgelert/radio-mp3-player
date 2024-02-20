import json
import os
import pathlib
import sys
import time

import pygame
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw
from tinytag import TinyTag as tag
from UI.player_ui_ui import Ui_mw_main


class MainClass(qtw.QMainWindow, Ui_mw_main):
    songs: dict = {}
    songs_duration: int = 0
    is_playing: bool = False
    is_paused: bool = False
    radio_checked: bool = False
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radio_buttons()
        self.pygame_init()
        self.pb_add_file.clicked.connect(self.add_song)
        self.pb_add_folder.clicked.connect(self.add_songs)
        self.pb_remove_all.clicked.connect(self.clear_song_list)
        self.lw_songs.itemClicked.connect(self.song_chosen)
        self.pb_start.clicked.connect(self.play)
        self.pb_pause.clicked.connect(self.pause)
        
        self.pb_stop.clicked.connect(self.stop)
        self.dl_song_volume.valueChanged.connect(self.volume_set)
        self.pb_previous.clicked.connect(self.prev_song)
        self.pb_next.clicked.connect(self.next_song)
        
        self.pb_radiostation_1.clicked.connect(lambda: [self.button_clicked(1)])
        self.pb_radiostation_2.clicked.connect(lambda: [self.button_clicked(10)])
        self.pb_radiostation_3.clicked.connect(lambda: [self.button_clicked(12)])
        self.pb_radiostation_4.clicked.connect(lambda: [self.button_clicked(3)])
        self.pb_radiostation_5.clicked.connect(lambda: [self.button_clicked(11)])
        self.pb_radiostation_6.clicked.connect(lambda: [self.button_clicked(19)])
        self.pb_radiostation_7.clicked.connect(lambda: [self.button_clicked(20)])
        self.pb_radiostation_8.clicked.connect(lambda: [self.button_clicked(16)])
        self.pb_radiostation_9.clicked.connect(lambda: [self.button_clicked(18)])
        self.pb_radiostation_10.clicked.connect(lambda: [self.button_clicked(2)])
        self.pb_radiostation_11.clicked.connect(lambda: [self.button_clicked(14)])
        self.pb_radiostation_12.clicked.connect(lambda: [self.button_clicked(8)])
        self.pb_radiostation_13.clicked.connect(lambda: [self.button_clicked(7)])
        self.pb_radiostation_14.clicked.connect(lambda: [self.button_clicked(6)])
        self.pb_radiostation_15.clicked.connect(lambda: [self.button_clicked(5)])
        self.pb_radiostation_16.clicked.connect(lambda: [self.button_clicked(9)])
        self.pb_radiostation_17.clicked.connect(lambda: [self.button_clicked(17)])
        self.pb_radiostation_18.clicked.connect(lambda: [self.button_clicked(4)])
        self.pb_radiostation_19.clicked.connect(lambda: [self.button_clicked(13)])
        self.pb_radiostation_20.clicked.connect(lambda: [self.button_clicked(15)])
        self.pb_start_radio.clicked.connect(self.test)

    
    def add_songs(self):
        s_path = qtw.QFileDialog.getExistingDirectory()
        for file in os.listdir(s_path):
            fpath = os.path.join(s_path, file)
            self.set_song(fpath)

    def add_song(self):
        s_path = qtw.QFileDialog.getOpenFileName()
        file:str = s_path[0]
        self.set_song(file)
        # print(file)
        # print(tag.is_supported(file))
        
        # print(f'album: {info.album}')
        # print(f'album artist: {info.albumartist}')
        # print(f'artist: {info.artist}')
        # print(f'composer: {info.composer}')
        # print(f'title: {info.title}')
        # print(f'comment: {info.comment}')
        # print(f'duration: {info.duration}')
        # print(f'genre: {info.genre}')

    
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
    
    def set_song(self, file_link:str):
        self.song_dict(file_link)
        info = tag.get(file_link)
        self.songs_duration = info.duration
        if all(
            True if x is not None else False for x in\
                [info.artist, info.title, info.album]
            ):
            song = '{} - {} ({}):    {}'.format(
                info.artist,
                info.title,
                info.album,
                self.song_time(info.duration)
            )
        else:
            song = '{}:     {}'.format(
                file_link.split('\\')[-1], self.song_time(info.duration))
        
        label = qtw.QListWidgetItem(song)
        self.lw_songs.addItem(label)
        
    def song_chosen(self, item:qtw.QListWidgetItem):
        song = item.text().split(':')[0]
        self.lb_le_now_play.setText(song)
    
    def song_dict(self, file_link:str):
        if len(self.songs):
            song_idx = [x for x in self.songs.keys()][-1]
            self.songs[song_idx+1] = file_link
        else:
            self.songs[0] = file_link

    def clear_song_list(self):
        self.songs.clear()
        self.lb_le_now_play.clear()
        self.lw_songs.clear()
    
    def pygame_init(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.0)
    
    def play(self):
        if len(self.songs) > 0:
            if self.lw_songs.currentRow() >= 0:
                pygame.mixer.music.load(self.songs[self.lw_songs.currentRow()])
                pygame.mixer.music.play()
                self.lb_le_status.setText('Playing')
                self.lb_mp_message.clear()
                if not self.is_playing:
                    self.is_playing = True
            else:
                Messages.non_selected(self)
        else:
            Messages.no_song(self)
    
    def stop(self):
        pygame.mixer.music.stop()
        self.lb_le_status.setText('Stopped')
        if self.is_playing:
            self.is_playing = False
    
    def pause(self):
        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.lb_le_status.setText('Paused')
            self.is_playing = False
            self.is_paused = True
        elif self.is_paused and not self.is_playing:
            pygame.mixer.music.unpause()
            self.lb_le_status.setText('Playing')
            self.is_playing = True
            self.is_paused = False
    
    def prev_song(self):
        current = self.lw_songs.currentRow()
        if current < 1:
            Messages.no_song(self)
        else:
            self.lw_songs.setCurrentRow(current - 1)
            self.song_chosen(self.lw_songs.currentItem())
    
    def next_song(self):
        current = self.lw_songs.currentRow()
        try:
            self.lw_songs.setCurrentRow(current + 1)
            self.song_chosen(self.lw_songs.currentItem())
        except:
            Messages.no_song(self)

    def volume_set(self):
        volume = self.dl_song_volume.value()
        vol = {
            0: (0, 0.0), 1: (1, 0.2), 2: (2, 0.4), 3: (3, 0.6), 4: (4, 0.8),
            5: (5, 1), 6: (6, 1.2), 7: (7, 1.4), 8: (8, 1.6), 9: (9, 1.8),
            10: (10, 2)
        }
        self.lcd_song_volume.display(vol[volume][0])
        pygame.mixer.music.set_volume(vol[volume][1])

    def set_radio_button(self):
        root_folder = r''.format(pathlib.Path(__file__).parent.absolute().parent)
        main_path = os.path.join(root_folder, 'App_images')
        def func(button: qtw.QPushButton, img_name: str, radio_name: str, radio_info: str):
            button.setIcon(qtg.QIcon(f'{main_path}\\{img_name}'))
            button.setText(f'{radio_name}\n{radio_info}')
            button.setStyleSheet('QPushButton { text-align: left}')
        return func
    
    def radio_buttons(self):
        info = self.get_button_data()
        buttons = self.set_radio_button()
        for x in range(1, 21):
            butt = self.sa_radios_scroll_content.children()[x].objectName()
            _, _, num = butt.split('_')
            buttons(getattr(self, butt),
                info[f'butt_{num}']['icon'], 
                info[f'butt_{num}']['name'], 
                info[f'butt_{num}']['desc']
            )

    def get_button_data(self):
        f_path = r'D:\Python_PORTFOLIO312\16_mp3_player_radio\App_main\irish_top_20_buttons.json'
        with open(f_path, 'r') as f:
            btn = json.load(f)
            return btn
        # print(self.sa_radios_scroll_content.children()[1].objectName())
    
    def button_clicked(self, nb: int):
        info: json = self.get_button_data()
        butt: str = self.sa_radios_scroll_content.children()[nb].objectName()
        _, _, num = butt.split('_')
        print(nb, num, '\n',
              info[f'butt_{num}']['name'],'\n',
              info[f'butt_{num}']['desc'],'\n')
        # buttons = [self.sa_radios_scroll_content.children()[x].objectName() for x in range(1, 21) if self.sa_radios_scroll_content.children()[x].clicked()]
        # return buttons
    
    def test(self):
        nd = {}
        for nb in range(1, 21):
            nd[nb] = self.sa_radios_scroll_content.children()[nb].objectName()
        print(nd)

class Messages(MainClass):

    def non_selected(self):
        self.lb_mp_message.setText('select song to play')
        self.lb_mp_message.setStyleSheet(
            'QLabel {color: rgb(255, 0, 0); font: 12pt "Comic Sans MS"}'
            )
    
    def no_song(self):
        self.lb_mp_message.setText('there is no song to play')
        self.lb_mp_message.setStyleSheet(
                'QLabel {color: rgb(255, 0, 0); font: 12pt "Comic Sans MS"}'
                )



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec())