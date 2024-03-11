# radio-mp3-player
The mp3 player with radio application made in Python 3.11  with help of pyqt6, pygame and miniaudio 

in choosing radiostation, radio is played in threads to not interfere with each other and
with program and allow program to execute other tasks in parallel



tinytag-1.10.1 [https://github.com/devsnd/tinytag]
pygame 2.5.2 [https://www.pygame.org/news]
miniaudio 1.59 [https://github.com/irmen/pyminiaudio]
python-ffmpeg 2.0.10 [https://github.com/jonghwanhyeon/python-ffmpeg]

### Installing  FFmpeg
FFmpeg is required for this program to work correctly.
Install FFmpeg by following these steps:
- download and install FFMPEG [https://ffmpeg.org/download.html],
- add to the PATH on windows eg: `C:\ffmpeg\bin`, 
- restart computer and done

### Adding to the path (Windows 10)
- right-click on the Start Button
- select “System” from the context menu.
- click “Advanced system settings”
- go to the “Advanced” tab
- click “Environment Variables…”
- click variable called “Path” and click “Edit…”
- click “New”
- paste eg: `C:\ffmpeg\bin`



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
- stop listening radio
- change volume 
- start listening radio

### icons
[creatives-stall-premium](https://www.flaticon.com/authors/creative-stall-premium)