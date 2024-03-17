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
FFmpeg is required for this program to work correctly.
- mp3 player
    - songs can be added by one or from folder
    - informations about songs are taken from tags, if not available from title of the file
    - songs are played with help of multithreading, thanks to what are light for the system
- online radio
    - radio is played with help of multithreading
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
- [FFmpeg](https://ffmpeg.org/)

### running the project
App opens from `player.py` file or use exe file.

### installing  FFmpeg
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

## problems
- [x] add one song, is wrongly listed
