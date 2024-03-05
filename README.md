# radio-mp3-player
The mp3 player with radio application made in Python 3.12  with help of pygame and pyqt6

in choosing radiostation, radio is played in threads to not interfere with each other and
with program and allow program to execute other tasks in parallel



tinytag-1.10.1 [https://github.com/devsnd/tinytag]
pygame 2.5.2
miniaudio 1.59 [https://github.com/irmen/pyminiaudio]
python-ffmpeg 2.0.10 [https://github.com/jonghwanhyeon/python-ffmpeg]
for AAC streaming download FFMPEG [https://ffmpeg.org/download.html],
next add to the PATH on windows eg: `C:\ffmpeg\bin`, restart computer and done
Python Core Audio Windows Library (pycaw 20240210) [https://github.com/AndreMiras/pycaw]

to set audio volume in miniaudio


    import miniaudio
    stream = miniaudio.stream_file("inc/xm/Toni Leys - Through A Cardboard World.mp3")
    device = miniaudio.PlaybackDevice()
    device._device.masterVolumeFactor = 0.2 # <--device.start(stream)

It supports both a volume factor (0..1) and gain in decibels 
(0 is full volume, < 0 reduces the volume).

### progress
- [x] bla
- [x] gla
- [ ] kla
- - [x] plo
- - [ ] fla

if you want to change volume in radio:
- stop listening radio if you already started
- change volume 
- start listening radio