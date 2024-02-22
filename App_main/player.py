import json
import os
import pathlib
import subprocess
import sys
import time

import miniaudio
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
    playing_num: str = ''
    on_off: bool = False
    audio_device: miniaudio.PlaybackDevice  = miniaudio.PlaybackDevice(
        output_format=miniaudio.SampleFormat.SIGNED16,
        nchannels=2, sample_rate=44100)
    radio_process = None
    
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
        
        self.button_clicked_connnect()
        self.pb_start_radio.clicked.connect(self.start_listening)
        self.pb_stop_radio.clicked.connect(self.stop_listening)

    
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

    def root_path(self, destination_folder: str) -> str:
        root_path = r''.format(pathlib.Path(__file__).parent.absolute().parent)
        return os.path.join(root_path, destination_folder)

    def set_radio_button(self):
        main_path = self.root_path('App_images')
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
        main_path = self.root_path('App_main')
        f_path = os.path.join(main_path, j_file)
        with open(f_path, 'r') as f:
            btn = json.load(f)
            return btn
    
    def button_clicked(self, nb: int):
        main_path = self.root_path('App_images')
        info: json = self.get_button_data('irish_top_20_buttons.json')
        butt: str = self.sa_radios_scroll_content.children()[nb].objectName()
        _, _, num = butt.split('_')
        self.playing_num = num
        self.lb_le_now_listen.setText(info[f'butt_{num}']['name'])
        self.lb_radio_icon_big.setPixmap(
            qtg.QPixmap(os.path.join(main_path, info[f'butt_{num}']['icon']))
            )
        # print(nb, num, '\n',
        #       info[f'butt_{num}']['name'],'\n',
        #       info[f'butt_{num}']['desc'],'\n',
        #       os.path.join(main_path, info[f'butt_{num}']['icon']), '\n',
        #       main_path)
    
    def connect_buttons(self):
        def func(pbr: qtw.QPushButton, nb:int):
            pbr.clicked.connect(lambda: [self.button_clicked(nb)])
        return func

    def button_clicked_connnect(self):
        nums:list[int] = [1, 10, 12, 3, 11, 19, 20, 16, 18, 2, 14, 8, 7, 6, 5, 9, 17, 4, 13, 15]
        buttons_clicked = self.connect_buttons()
        for x, y in zip(range(1, 21), nums):
            buttons_clicked(getattr(self, 'pb_radiostation_{}'.format(x)), y)

    def stream_signal(self, source):
        channels = 2
        sample_width = 2  # 16 bit pcm
        required_frames = yield b""  # generator initialization
        while True:
            required_bytes = required_frames * channels * sample_width
            sample_data = source.read(required_bytes)
            if not sample_data:
                break
            # print(".", end="", flush=True)
            required_frames = yield sample_data
    
    def start_listening(self):
        info: json = self.get_button_data('radio_web_format.json')
        filename = info[f'butt_{self.playing_num}']['web']
        channels = 2
        sample_rate = 44100
        # miniaudio.PlaybackDevice(output_format=miniaudio.SampleFormat.SIGNED16,
        #                       nchannels=2, sample_rate=44100)
        with self.audio_device as dev:
            self.radio_process = subprocess.Popen(["ffmpeg", "-v", "fatal", "-hide_banner", "-nostdin",
                                        "-i", filename, "-f", "s16le", "-acodec", "pcm_s16le",
                                        "-ac", str(channels), "-ar", str(sample_rate), "-"],
                                    stdin=None, stdout=subprocess.PIPE)
            stream = self.stream_signal(self.radio_process.stdout)
            next(stream)  # start the generator
            dev.start(stream)
            self.get_execute_input()
            # input("Audio file playing in the background. Enter to stop playback: ")
            # self.radio_process.terminate()

    def stop_listening(self):
        if self.is_listening():
            self.radio_process.terminate()
            self.audio_device.stop()
            time.sleep(0.5)
            if self.is_listening():
                self.radio_process.kill()
                self.audio_device.close()
                
            self.radio_process = None
    
    def is_listening(self):
        # poll() returns None if not exited yet
        return self.radio_process is not None and self.radio_process.poll() is None
    
    def prompt(self):
        try:
            input()
        except RuntimeError:
            return None
    
    def force_prompt(self):
        close = None
        while close is None:
            close = self.prompt()
        return close
    
    def get_execute_input(self):
        close = self.force_prompt()
        try:
            self.execute(close)
        except CommandError as e:
            print(e)
    
    def execute(self, command):
        command = input()


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


class CommandError(Exception):
    pass

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec())