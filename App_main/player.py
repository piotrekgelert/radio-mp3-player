import gc
import json
import logging as log
import os
import pathlib
import sys
from threading import Thread

import miniaudio
import psutil
import pygame
import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw
from audio_processing import FFmpegProcess, PygameProcess
from player_icons_setup import ApplicationIconSetup
from tinytag import TinyTag as tag
from UI.player_ui_ui import Ui_mw_main
from utilities import NetworkAvaibility, SongDuration

log.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=log.DEBUG)

class MainClass(qtw.QMainWindow, Ui_mw_main):
    
    app_icons = ApplicationIconSetup
    app_audio = PygameProcess
    app_radio_audio = FFmpegProcess
    time_song = SongDuration
    songs: dict = {}
    songs_len: int = 0
    songs_duration: int = 0
    is_playing: bool = False
    is_paused: bool = False
    playing_num: str = ''
    radio_process = None
    threadd: Thread|None = None
    dev: miniaudio.PlaybackDevice|None = None
    radio_vol: float = 0.0
    internet_connection: bool|None = None
    styles: dict = {
        'buttons': 'color: rgb(255, 255, 255);background-color: rgb(170, 170, 255);font: 12pt "Comic Sans MS";',
        'frames': 'background-color: rgb(56, 56, 56);',
        'messages': 'color: rgb(255, 255, 255); background-color: rgb(56, 56, 56);',
        'background': 'background-color: rgb(80, 80, 80);'
    }
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        qtw.QDialog.setFixedSize(self, 830,  825)
        self.application_icons()
        self.radio_buttons()
        self.app_audio.pygame_init(self)
        self.initial_radio_volume_set()
        NetworkAvaibility.net_check(self)
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
        
        self.button_clicked_connnect()
        self.pb_start_radio.clicked.connect(self.start_listening)
        self.pb_start_radio.clicked.connect(self.activate_process)
        self.pb_stop_radio.clicked.connect(self.stop_listening)
        
        self.dl_radio_volume.valueChanged.connect(self.radio_volume_set)
        
    def add_songs(self) -> None:
        self.lb_mp_message.clear()
        try:
            s_path: str = qtw.QFileDialog.getExistingDirectory()
            ls_songs: list = os.listdir(s_path)
            self.songs_len: int = len(ls_songs)
            for file in ls_songs:
                fpath: str = os.path.join(s_path, file)
                self.set_song(fpath)
        except:
            Messages.not_added(self)

    def add_song(self) -> None:
        self.lb_mp_message.clear()
        try:
            s_path = qtw.QFileDialog.getOpenFileName()
            file:str = s_path[0]
            self.set_song(file)
        except:
            Messages.not_added(self)
    
    # def song_time(self, inf):
    #     hours = int(inf // 3600)
    #     hour_other = inf % 3600

    #     mins = int(hour_other // 60)
    #     mins_other = hour_other % 60

    #     seconds = int(mins_other % 60)

    #     time_took = '{}:{}:{}'.format(
    #         hours if hours > 10 else '0' + str(hours),
    #         mins if mins > 10 else '0' + str(mins),
    #         seconds if seconds > 10 else '0' + str(seconds)
    #         )
    #     return time_took
    
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
                self.time_song.song_time(self, info.duration)
            )
        else:
            song = '{}:     {}'.format(
                file_link.split('\\')[-1],
                self.time_song.song_time(self, info.duration))
        
        label = qtw.QListWidgetItem(song)
        self.lw_songs.addItem(label)
        
    def song_dict(self, file_link:str):
        if len(self.songs):
            song_idx = [x for x in self.songs.keys()][-1]
            self.songs[song_idx+1] = file_link
        else:
            self.songs[0] = file_link
    
    def song_chosen(self, item:qtw.QListWidgetItem):
        song = item.text().split(':')[0]
        self.lb_le_now_play.setText(song)
    
    def clear_song_list(self):
        self.songs.clear()
        self.lb_le_now_play.clear()
        self.lw_songs.clear()
    
    def play(self):
        lab_img = self.app_icons.setup_pixels(self, 'App_icons')
        if len(self.songs) > 0:
            if self.lw_songs.currentRow() >= 0:
                self.app_audio.music_start(self, self.songs[self.lw_songs.currentRow()])
                self.lb_mp_message.clear()
                
                if not self.is_playing:
                    self.is_playing = True
                    self.lb_le_status.setText('Playing')
                    lab_img(
                        self.lb_le_status_icon, 'play_mp3_status_75x64.png'
                        )
            else:
                Messages.no_song_selected(self)
        else:
            Messages.no_song(self)
    
    def stop(self):
        lab_img = self.app_icons.setup_pixels(self, 'App_icons')
        self.app_audio.music_stop(self)
        self.lb_le_status.setText('Stopped')
        
        if self.is_playing:
            self.is_playing = False
        lab_img(
            self.lb_le_status_icon, 'stop_mp3_status_75x64.png'
            )
        
    def pause(self):
        lab_img = self.app_icons.setup_pixels(self, 'App_icons')
        if self.is_playing and not self.is_paused:
            self.app_audio.music_pause(self)
            self.lb_le_status.setText('Paused')
            lab_img(
                self.lb_le_status_icon, 'pause_mp3_status_75x64.png'
                )
            
            self.is_playing = False
            self.is_paused = True
        elif self.is_paused and not self.is_playing:
            self.app_audio.music_unpause(self)
            self.lb_le_status.setText('Playing')
            lab_img(
                self.lb_le_status_icon, 'play_mp3_status_75x64.png'
                )
            self.is_playing = True
            self.is_paused = False
    
    def prev_song(self):
        self.lb_mp_message.clear()
        current = self.lw_songs.currentRow()
        if current < 1:
            Messages.no_song(self)
        else:
            if not self.pb_next.isEnabled():
                self.pb_next.setEnabled(True)
                self.lb_mp_message.clear()
            self.lw_songs.setCurrentRow(current - 1)
            self.song_chosen(self.lw_songs.currentItem())
            
    def next_song(self):
        self.lb_mp_message.clear()
        current = self.lw_songs.currentRow()
        if current+2 < self.lw_songs.count():
            self.lw_songs.setCurrentRow(current + 1)
            self.song_chosen(self.lw_songs.currentItem())
        else:
            Messages.no_song(self)

    def volume_set(self):
        volume = self.dl_song_volume.value()
        vol = {
            0: (0, 0.0), 1: (1, 0.3), 2: (2, 0.6), 3: (3, 0.9), 4: (4, 1.2),
            5: (5, 1.5), 6: (6, 1.8), 7: (7, 2.1), 8: (8, 2.4), 9: (9, 2.7),
            10: (10, 3)
        }
        self.lcd_song_volume.display(vol[volume][0])
        pygame.mixer.music.set_volume(vol[volume][1])

    def set_radio_button(self):
        main_path:str = self.app_icons.root_path(self, 'App_images')
        def func(button: qtw.QPushButton, img_name: str, radio_name: str, radio_info: str):
            button.setIcon(qtg.QIcon(f'{main_path}\\{img_name}'))
            button.setText(f'{radio_name}\n{radio_info}')
            button.setStyleSheet('QPushButton { text-align: left}')
        return func
    
    def radio_buttons(self):
        info = self.get_button_data('irish_top_20_buttons.json')
        buttons = self.set_radio_button()
        for x in range(1, 21):
            butt = self.sa_radios_scroll_content.children()[x].objectName()
            _, _, num = butt.split('_')
            buttons(getattr(self, butt),
                info[f'butt_{num}']['icon'], 
                info[f'butt_{num}']['name'], 
                info[f'butt_{num}']['desc']
            )

    def get_button_data(self, j_file):
        main_path = self.app_icons.root_path(self, 'App_main')
        f_path = os.path.join(main_path, j_file)
        with open(f_path, 'r') as f:
            btn = json.load(f)
            return btn
    
    def button_clicked(self, nb: int):
        main_path = self.app_icons.root_path(self, 'App_images')
        info: dict = self.get_button_data('irish_top_20_buttons.json')
        butt: str = self.sa_radios_scroll_content.children()[nb].objectName()
        _, _, num = butt.split('_')
        self.playing_num = num
        self.lb_le_now_listen.setText(info[f'butt_{num}']['name'])
        self.lb_radio_icon_big.setPixmap(
            qtg.QPixmap(os.path.join(main_path, info[f'butt_{num}']['icon']))
            )
    
    def connect_buttons(self):
        def func(pbr: qtw.QPushButton, nb:int):
            pbr.clicked.connect(lambda: [self.button_clicked(nb)])
        return func

    def button_clicked_connnect(self):
        nums:list[int] = [1, 10, 12, 3, 11, 19, 20, 16, 18, 2, 14, 8, 7, 6, 5, 9, 17, 4, 13, 15]
        buttons_clicked = self.connect_buttons()
        for x, y in zip(range(1, 21), nums):
            buttons_clicked(getattr(self, 'pb_radiostation_{}'.format(x)), y)
    
    def activate_process(self):
        if not self.radio_process:
            log.info('process not initialized')
            return False
        
        try:
            proc = psutil.Process(self.radio_process.pid)
            # proc_name = psutil.Process(self.radio_process.args)
            if proc.status() == psutil.STATUS_ZOMBIE:

                log.info('process is zombie')
                return False
            if proc.status() in [psutil.STATUS_RUNNING, psutil.STATUS_SLEEPING]:
                # print('process activated')
                log.info('process activated')
                return True
            # return False
        except (psutil.NoSuchProcess, Exception) as e:
            log.error('process not found while checking: {}'.format(e))
            return False
    
    def start_listening(self):
        try:
            if self.internet_connection:
                if len(self.lb_le_now_listen.text()):
                    if self.threadd is None or not self.threadd.is_alive():
                        self.threadd = Thread(target=self.listening)
                        self.threadd.start()
                        self.pb_start_radio.setEnabled(False)
                        self.lb_le_radio_status.setText('running')
                        lab_img = self.app_icons.setup_pixels(self, 'App_icons')
                        lab_img(
                            self.lb_le_radio_status_icon,
                            'listening_status_63x56.png')
                else:
                    Messages.no_radio_selected(self)      
            else:
                Messages.no_net(self)
        except:
            Messages.no_ffmpeg(self)
            
    def listening(self):
        info: dict = self.get_button_data('radio_web_format.json')
        filename: str = info[f'butt_{self.playing_num}']['web']
        channels: int = 2
        sample_rate: int = 44100
        self.dev = self.app_radio_audio.audio_device(self)
        self.radio_process = self.app_radio_audio.process_device(self,
            filename, channels, sample_rate
        )
        self.activate_process()
        self.stream = self.app_radio_audio.stream_signal(self, self.radio_process.stdout)
        next(self.stream)  # start the stream, stream.send()
    
        self.dev._device.masterVolumeFactor = self.radio_vol
        self.dev.start(self.stream)
        
    def stop_listening(self):
        if self.is_listening():
            self.dev.stop()
            self.stream.close()
            self.lb_le_radio_status.setText('stopped')
            self.pb_start_radio.setEnabled(True)
            lab_img = self.app_icons.setup_pixels(self, 'App_icons')
            lab_img(
                self.lb_le_radio_status_icon,
                'not_listening_status_63x56.png')
            
    def is_listening(self):
        # poll() returns None if not exited yet
        return self.radio_process is not None\
            and self.radio_process.poll() is None
    
    def initial_radio_volume_set(self):
        self.radio_vol: float = 0.5
        self.lcd_radio_vol.display('5')
        self.dl_radio_volume.setValue(5)
    
    def radio_volume_set(self):
        r_vol: int = self.dl_radio_volume.value()
        
        radio_vol_dict: dict = {
            0: ('0', 0.0), 1: ('1', 0.1), 2: ('2', 0.2), 3: ('3', 0.3),
            4: ('4', 0.4), 5: ('5', 0.5), 6: ('6', 0.6), 7: ('7', 0.7),
            8: ('8', 0.8), 9: ('9', 0.9), 10: ('10', 1.0),
            }
        self.lcd_radio_vol.display(radio_vol_dict[r_vol][0])
        self.radio_vol: float = radio_vol_dict[r_vol][1]
    
    def application_icons(self):
        main_path = self.app_icons.root_path(self, 'App_icons')

        tab = self.app_icons.setup_tabs(self, main_path)
        tab(self.tb_player, 'player_icon_button_117x64.png')
        tab(self.tb_radio, 'radio_icon_button_70x64.png')

        button = self.app_icons.setup_icons(self, main_path)
        button(self.pb_add_file, 'import_file_button_56x64.png')
        button(self.pb_add_folder, 'import_folder_button_49x64.png')
        button(self.pb_remove_all, 'remove_all_button_50x64.png')
        button(self.pb_start, 'play_button_64x64.png')
        button(self.pb_stop, 'stop_button_64x64.png')
        button(self.pb_pause, 'pause_unpause_button_89x64.png')
        button(self.pb_next, 'forward_button_64x54.png')
        button(self.pb_previous, 'backward_button_63x53.png')
        button(self.pb_start_radio, 'play_button_64x64.png')
        button(self.pb_stop_radio, 'stop_button_64x64.png')

        lab_img = self.app_icons.setup_pixels(self, main_path)
        lab_img(self.lb_le_radio_status_icon, 'not_listening_status_63x56.png')
        lab_img(self.lb_le_status_icon, 'stop_mp3_status_75x64.png')

class Messages(MainClass):

    def no_song_selected(self):
        self.lb_mp_message.setText('select song to play')
        self.lb_mp_message.setStyleSheet(
            'QLabel {color: rgb(255, 0, 0); font: 12pt "Comic Sans MS"}'
            )
    
    def no_radio_selected(self):
        self.lb_radio_message.setText('select radio to play')
        self.lb_radio_message.setStyleSheet(
            'QLabel {color: rgb(255, 0, 0); font: 12pt "Comic Sans MS"}'
            )
    
    def no_song(self):
        self.lb_mp_message.setText('there is no song to play')
        self.lb_mp_message.setStyleSheet(
                'QLabel {color: rgb(255, 0, 0); font: 12pt "Comic Sans MS"}'
                )
    
    def no_response(self):
        self.lb_radio_message.setText('Radio is not responsive')
        self.lb_radio_message.setStyleSheet(
            'QLabel {color: rgb(255, 0, 0); font: 12pt "Comic Sans MS"}'
        )
    
    def still_listening(self):
        self.lb_radio_message.setText('Radiostation is still working')
    
    def not_added(self):
        self.lb_mp_message.setText('There is nothing added to the list')
    
    def no_net(self):
        self.lb_radio_message.setText('No internet connection, establish connection and restart an app')
        self.lb_radio_message.setStyleSheet(
            'QLabel {color: rgb(255, 0, 0); font: 12pt "Comic Sans MS"}'
        )
    
    def no_ffmpeg(self):
        self.lb_radio_message.setText('You can\'t use radio. There is no FFmpeg installed on your computer')
        self.lb_radio_message.setStyleSheet(
            'QLabel {color: rgb(255, 0, 0); font: 12pt "Comic Sans MS"}'
        )



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec())