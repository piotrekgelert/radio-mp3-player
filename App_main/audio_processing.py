
import subprocess

import miniaudio
import pygame


class FFmpegProcess:

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
    
    def audio_device(self):
        return miniaudio.PlaybackDevice(
            output_format=miniaudio.SampleFormat.SIGNED16,
            nchannels=2, 
            sample_rate=44100)
    
    def process_device(self, filename, channels, sample_rate):
        return subprocess.Popen(
            ["ffmpeg", "-v", "fatal", "-hide_banner", "-nostdin",
            "-i", filename, "-f",
            "s16le", "-acodec", "pcm_s16le",
            "-ac", str(channels), "-ar", str(sample_rate), "-"],
            stdin=None, stdout=subprocess.PIPE
        )
    

class PygameProcess:
    
    def pygame_init(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.0)
    
    def music_start(self, song):
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

    def music_stop(self):
        pygame.mixer.music.stop()
    
    def music_is_running(self):
        return pygame.mixer.music.get_busy()

    def music_pause(self):
        pygame.mixer.music.pause()
    
    def music_unpause(self):
        pygame.mixer.music.unpause()
    
    def set_volume(self, vol):
        pygame.mixer.music.set_volume(vol)
    
    def get_time(self):
        return pygame.mixer.music.get_pos()