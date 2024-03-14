# radio-mp3-player
The mp3 player with radio application made in Python 3.11  with help of pyqt6, pygame and miniaudio 

in choosing radiostation, radio is played in threads to not interfere with each other and
with program and allow program to execute other tasks in parallel


### ui example:

<p align="middle">
  <img src="https://github.com/piotrekgelert/radio-mp3-player/blob/main/images/mp3_player.png" width="45%"/>
  <img src="https://github.com/piotrekgelert/radio-mp3-player/blob/main/images/online_radio.png" width="45%"/>
</p>

### notes
- mp3 player
    - songs can be added by one or from folder
    - informations about songs are taken from tags, if not available from title of the file
- online radio
    - radio is played in threads to not interfere with program thanks to what is not heavy for the system
    - choice of 20 the most popular radiostations in Ireland


### online radio advice
if you want to change volume in radio:
- stop listening radio
- change volume 
- start listening radio

### icons
- [creatives-stall-premium on flaticon.com](https://www.flaticon.com/authors/creative-stall-premium)
- [creatives-stall-premium on freepik.com](https://www.freepik.com/author/creatives-stall-premium/icons?t=f)

### used packages:
- [PyQt6 6.6.1](https://www.riverbankcomputing.com/software/pyqt/)
- [tinytag-1.10.1](https://github.com/devsnd/tinytag)
- [pygame 2.5.2](https://www.pygame.org/news)
- [miniaudio 1.59](https://github.com/irmen/pyminiaudio)
- [python-ffmpeg 2.0.10](https://github.com/jonghwanhyeon/python-ffmpeg)

### running the project
App opens from `player.py` file or use exe file.

### installing  FFmpeg
FFmpeg is required for this program to work correctly.
Install FFmpeg by following these steps:
- download and install FFMPEG [https://ffmpeg.org/download.html],
- add to the PATH on windows eg: `C:\ffmpeg\bin`, 
- restart computer and done

### adding to the Path (Windows 10)
- right-click on the Start Button
- select “System” from the context menu.
- click “Advanced system settings”
- go to the “Advanced” tab
- click “Environment Variables…”
- click variable called “Path” and click “Edit…”
- click “New”
- paste eg: `C:\ffmpeg\bin`

## licence
This project is licensed under the [MIT] License - see [Licence.md](LICENSE) file for details.