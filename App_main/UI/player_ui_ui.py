# Form implementation generated from reading ui file 'd:\Python_PORTFOLIO312\16_mp3_player_radio\App_main\UI\player_ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mw_main(object):
    def setupUi(self, mw_main):
        mw_main.setObjectName("mw_main")
        mw_main.resize(828, 825)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        mw_main.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=mw_main)
        self.centralwidget.setObjectName("centralwidget")
        self.tb_main = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tb_main.setGeometry(QtCore.QRect(20, 20, 791, 791))
        self.tb_main.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tb_main.setIconSize(QtCore.QSize(117, 64))
        self.tb_main.setObjectName("tb_main")
        self.tb_player = QtWidgets.QWidget()
        self.tb_player.setObjectName("tb_player")
        self.gb_now_play = QtWidgets.QGroupBox(parent=self.tb_player)
        self.gb_now_play.setGeometry(QtCore.QRect(10, 0, 771, 71))
        self.gb_now_play.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gb_now_play.setObjectName("gb_now_play")
        self.lb_le_now_play = QtWidgets.QLabel(parent=self.gb_now_play)
        self.lb_le_now_play.setGeometry(QtCore.QRect(10, 30, 751, 31))
        self.lb_le_now_play.setObjectName("lb_le_now_play")
        self.fr_add_rem_buttons = QtWidgets.QFrame(parent=self.tb_player)
        self.fr_add_rem_buttons.setGeometry(QtCore.QRect(10, 80, 171, 281))
        self.fr_add_rem_buttons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_add_rem_buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_add_rem_buttons.setObjectName("fr_add_rem_buttons")
        self.pb_add_folder = QtWidgets.QPushButton(parent=self.fr_add_rem_buttons)
        self.pb_add_folder.setGeometry(QtCore.QRect(10, 100, 151, 81))
        self.pb_add_folder.setIconSize(QtCore.QSize(49, 64))
        self.pb_add_folder.setObjectName("pb_add_folder")
        self.pb_add_file = QtWidgets.QPushButton(parent=self.fr_add_rem_buttons)
        self.pb_add_file.setGeometry(QtCore.QRect(10, 10, 151, 81))
        self.pb_add_file.setIconSize(QtCore.QSize(56, 64))
        self.pb_add_file.setObjectName("pb_add_file")
        self.pb_remove_all = QtWidgets.QPushButton(parent=self.fr_add_rem_buttons)
        self.pb_remove_all.setGeometry(QtCore.QRect(10, 190, 151, 81))
        self.pb_remove_all.setIconSize(QtCore.QSize(50, 64))
        self.pb_remove_all.setObjectName("pb_remove_all")
        self.gb_status = QtWidgets.QGroupBox(parent=self.tb_player)
        self.gb_status.setGeometry(QtCore.QRect(10, 380, 161, 161))
        self.gb_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gb_status.setObjectName("gb_status")
        self.lb_le_status = QtWidgets.QLabel(parent=self.gb_status)
        self.lb_le_status.setGeometry(QtCore.QRect(10, 120, 141, 31))
        self.lb_le_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_le_status.setObjectName("lb_le_status")
        self.lb_le_status_icon = QtWidgets.QLabel(parent=self.gb_status)
        self.lb_le_status_icon.setGeometry(QtCore.QRect(10, 30, 141, 81))
        self.lb_le_status_icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_le_status_icon.setObjectName("lb_le_status_icon")
        self.fr_play_buttons = QtWidgets.QFrame(parent=self.tb_player)
        self.fr_play_buttons.setGeometry(QtCore.QRect(180, 360, 601, 181))
        self.fr_play_buttons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_play_buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_play_buttons.setObjectName("fr_play_buttons")
        self.pb_start = QtWidgets.QPushButton(parent=self.fr_play_buttons)
        self.pb_start.setGeometry(QtCore.QRect(60, 10, 131, 81))
        self.pb_start.setIconSize(QtCore.QSize(64, 64))
        self.pb_start.setObjectName("pb_start")
        self.pb_pause = QtWidgets.QPushButton(parent=self.fr_play_buttons)
        self.pb_pause.setGeometry(QtCore.QRect(340, 10, 231, 81))
        self.pb_pause.setIconSize(QtCore.QSize(89, 64))
        self.pb_pause.setObjectName("pb_pause")
        self.pb_stop = QtWidgets.QPushButton(parent=self.fr_play_buttons)
        self.pb_stop.setGeometry(QtCore.QRect(200, 10, 131, 81))
        self.pb_stop.setIconSize(QtCore.QSize(64, 64))
        self.pb_stop.setObjectName("pb_stop")
        self.pb_previous = QtWidgets.QPushButton(parent=self.fr_play_buttons)
        self.pb_previous.setGeometry(QtCore.QRect(150, 100, 121, 71))
        self.pb_previous.setIconSize(QtCore.QSize(63, 53))
        self.pb_previous.setObjectName("pb_previous")
        self.pb_next = QtWidgets.QPushButton(parent=self.fr_play_buttons)
        self.pb_next.setGeometry(QtCore.QRect(280, 100, 131, 71))
        self.pb_next.setIconSize(QtCore.QSize(64, 54))
        self.pb_next.setObjectName("pb_next")
        self.frame = QtWidgets.QFrame(parent=self.tb_player)
        self.frame.setGeometry(QtCore.QRect(180, 80, 601, 271))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lw_songs = QtWidgets.QListWidget(parent=self.frame)
        self.lw_songs.setGeometry(QtCore.QRect(10, 10, 581, 251))
        self.lw_songs.setObjectName("lw_songs")
        self.fr_mp_message = QtWidgets.QFrame(parent=self.tb_player)
        self.fr_mp_message.setGeometry(QtCore.QRect(10, 660, 771, 51))
        self.fr_mp_message.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_mp_message.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_mp_message.setObjectName("fr_mp_message")
        self.lb_mp_message = QtWidgets.QLabel(parent=self.fr_mp_message)
        self.lb_mp_message.setGeometry(QtCore.QRect(16, 10, 741, 31))
        self.lb_mp_message.setObjectName("lb_mp_message")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tb_player)
        self.groupBox.setGeometry(QtCore.QRect(10, 540, 771, 111))
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.dl_song_volume = QtWidgets.QDial(parent=self.groupBox)
        self.dl_song_volume.setGeometry(QtCore.QRect(250, 20, 91, 81))
        self.dl_song_volume.setMaximum(10)
        self.dl_song_volume.setObjectName("dl_song_volume")
        self.lcd_song_volume = QtWidgets.QLCDNumber(parent=self.groupBox)
        self.lcd_song_volume.setGeometry(QtCore.QRect(360, 30, 171, 71))
        self.lcd_song_volume.setObjectName("lcd_song_volume")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Python_PORTFOLIO312\\16_mp3_player_radio\\App_main\\UI\\../../App_icons/player_icon_button_117x64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tb_main.addTab(self.tb_player, icon, "")
        self.tb_radio = QtWidgets.QWidget()
        self.tb_radio.setObjectName("tb_radio")
        self.gb_now_listen = QtWidgets.QGroupBox(parent=self.tb_radio)
        self.gb_now_listen.setGeometry(QtCore.QRect(10, 0, 761, 101))
        self.gb_now_listen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gb_now_listen.setObjectName("gb_now_listen")
        self.lb_le_now_listen = QtWidgets.QLabel(parent=self.gb_now_listen)
        self.lb_le_now_listen.setGeometry(QtCore.QRect(90, 20, 401, 61))
        self.lb_le_now_listen.setObjectName("lb_le_now_listen")
        self.lb_radio_icon_big = QtWidgets.QLabel(parent=self.gb_now_listen)
        self.lb_radio_icon_big.setGeometry(QtCore.QRect(10, 20, 71, 71))
        self.lb_radio_icon_big.setObjectName("lb_radio_icon_big")
        self.fr_radio_message = QtWidgets.QFrame(parent=self.tb_radio)
        self.fr_radio_message.setGeometry(QtCore.QRect(10, 660, 771, 51))
        self.fr_radio_message.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_radio_message.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_radio_message.setObjectName("fr_radio_message")
        self.lb_radio_message = QtWidgets.QLabel(parent=self.fr_radio_message)
        self.lb_radio_message.setGeometry(QtCore.QRect(16, 10, 741, 31))
        self.lb_radio_message.setObjectName("lb_radio_message")
        self.fr_radios = QtWidgets.QFrame(parent=self.tb_radio)
        self.fr_radios.setGeometry(QtCore.QRect(10, 230, 771, 271))
        self.fr_radios.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_radios.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_radios.setObjectName("fr_radios")
        self.fr_radio_buttons = QtWidgets.QFrame(parent=self.fr_radios)
        self.fr_radio_buttons.setGeometry(QtCore.QRect(10, 160, 491, 101))
        self.fr_radio_buttons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_radio_buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_radio_buttons.setObjectName("fr_radio_buttons")
        self.pb_start_radio = QtWidgets.QPushButton(parent=self.fr_radio_buttons)
        self.pb_start_radio.setGeometry(QtCore.QRect(40, 10, 201, 81))
        self.pb_start_radio.setIconSize(QtCore.QSize(64, 64))
        self.pb_start_radio.setObjectName("pb_start_radio")
        self.pb_stop_radio = QtWidgets.QPushButton(parent=self.fr_radio_buttons)
        self.pb_stop_radio.setGeometry(QtCore.QRect(250, 10, 191, 81))
        self.pb_stop_radio.setIconSize(QtCore.QSize(64, 64))
        self.pb_stop_radio.setObjectName("pb_stop_radio")
        self.radio_status = QtWidgets.QGroupBox(parent=self.tb_radio)
        self.radio_status.setGeometry(QtCore.QRect(520, 380, 251, 111))
        self.radio_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.radio_status.setObjectName("radio_status")
        self.lb_le_radio_status = QtWidgets.QLabel(parent=self.radio_status)
        self.lb_le_radio_status.setGeometry(QtCore.QRect(100, 30, 121, 71))
        self.lb_le_radio_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_le_radio_status.setObjectName("lb_le_radio_status")
        self.lb_le_radio_status_icon = QtWidgets.QLabel(parent=self.radio_status)
        self.lb_le_radio_status_icon.setGeometry(QtCore.QRect(10, 30, 91, 71))
        self.lb_le_radio_status_icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_le_radio_status_icon.setObjectName("lb_le_radio_status_icon")
        self.radio_volume = QtWidgets.QGroupBox(parent=self.tb_radio)
        self.radio_volume.setGeometry(QtCore.QRect(10, 540, 771, 111))
        self.radio_volume.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.radio_volume.setObjectName("radio_volume")
        self.dl_radio_volume = QtWidgets.QDial(parent=self.radio_volume)
        self.dl_radio_volume.setGeometry(QtCore.QRect(250, 20, 91, 81))
        self.dl_radio_volume.setMaximum(10)
        self.dl_radio_volume.setObjectName("dl_radio_volume")
        self.lcd_radio_vol = QtWidgets.QLCDNumber(parent=self.radio_volume)
        self.lcd_radio_vol.setGeometry(QtCore.QRect(360, 30, 171, 71))
        self.lcd_radio_vol.setObjectName("lcd_radio_vol")
        self.sa_radios_scroll = QtWidgets.QScrollArea(parent=self.tb_radio)
        self.sa_radios_scroll.setGeometry(QtCore.QRect(10, 120, 761, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(105)
        sizePolicy.setHeightForWidth(self.sa_radios_scroll.sizePolicy().hasHeightForWidth())
        self.sa_radios_scroll.setSizePolicy(sizePolicy)
        self.sa_radios_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.sa_radios_scroll.setWidgetResizable(True)
        self.sa_radios_scroll.setObjectName("sa_radios_scroll")
        self.sa_radios_scroll_content = QtWidgets.QWidget()
        self.sa_radios_scroll_content.setGeometry(QtCore.QRect(0, 0, 742, 792))
        self.sa_radios_scroll_content.setObjectName("sa_radios_scroll_content")
        self.gridLayout = QtWidgets.QGridLayout(self.sa_radios_scroll_content)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_radiostation_1 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/radio_icons/test_64x64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_radiostation_1.setIcon(icon1)
        self.pb_radiostation_1.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_1.setObjectName("pb_radiostation_1")
        self.gridLayout.addWidget(self.pb_radiostation_1, 0, 0, 1, 1)
        self.pb_radiostation_10 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_10.setIcon(icon1)
        self.pb_radiostation_10.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_10.setObjectName("pb_radiostation_10")
        self.gridLayout.addWidget(self.pb_radiostation_10, 5, 1, 1, 1)
        self.pb_radiostation_4 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_4.setIcon(icon1)
        self.pb_radiostation_4.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_4.setObjectName("pb_radiostation_4")
        self.gridLayout.addWidget(self.pb_radiostation_4, 1, 1, 1, 1)
        self.pb_radiostation_18 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_18.setIcon(icon1)
        self.pb_radiostation_18.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_18.setObjectName("pb_radiostation_18")
        self.gridLayout.addWidget(self.pb_radiostation_18, 12, 1, 1, 1)
        self.pb_radiostation_15 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_15.setIcon(icon1)
        self.pb_radiostation_15.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_15.setObjectName("pb_radiostation_15")
        self.gridLayout.addWidget(self.pb_radiostation_15, 6, 0, 1, 1)
        self.pb_radiostation_14 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_14.setIcon(icon1)
        self.pb_radiostation_14.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_14.setObjectName("pb_radiostation_14")
        self.gridLayout.addWidget(self.pb_radiostation_14, 8, 1, 1, 1)
        self.pb_radiostation_13 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_13.setIcon(icon1)
        self.pb_radiostation_13.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_13.setObjectName("pb_radiostation_13")
        self.gridLayout.addWidget(self.pb_radiostation_13, 8, 0, 1, 1)
        self.pb_radiostation_12 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_12.setIcon(icon1)
        self.pb_radiostation_12.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_12.setObjectName("pb_radiostation_12")
        self.gridLayout.addWidget(self.pb_radiostation_12, 11, 0, 1, 1)
        self.pb_radiostation_16 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_16.setIcon(icon1)
        self.pb_radiostation_16.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_16.setObjectName("pb_radiostation_16")
        self.gridLayout.addWidget(self.pb_radiostation_16, 6, 1, 1, 1)
        self.pb_radiostation_2 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_2.setIcon(icon1)
        self.pb_radiostation_2.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_2.setObjectName("pb_radiostation_2")
        self.gridLayout.addWidget(self.pb_radiostation_2, 0, 1, 1, 1)
        self.pb_radiostation_5 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_5.setIcon(icon1)
        self.pb_radiostation_5.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_5.setObjectName("pb_radiostation_5")
        self.gridLayout.addWidget(self.pb_radiostation_5, 2, 0, 1, 1)
        self.pb_radiostation_3 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_3.setIcon(icon1)
        self.pb_radiostation_3.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_3.setObjectName("pb_radiostation_3")
        self.gridLayout.addWidget(self.pb_radiostation_3, 1, 0, 1, 1)
        self.pb_radiostation_19 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_19.setIcon(icon1)
        self.pb_radiostation_19.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_19.setObjectName("pb_radiostation_19")
        self.gridLayout.addWidget(self.pb_radiostation_19, 13, 1, 1, 1)
        self.pb_radiostation_11 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_11.setIcon(icon1)
        self.pb_radiostation_11.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_11.setObjectName("pb_radiostation_11")
        self.gridLayout.addWidget(self.pb_radiostation_11, 11, 1, 1, 1)
        self.pb_radiostation_20 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_20.setIcon(icon1)
        self.pb_radiostation_20.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_20.setObjectName("pb_radiostation_20")
        self.gridLayout.addWidget(self.pb_radiostation_20, 13, 0, 1, 1)
        self.pb_radiostation_8 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_8.setIcon(icon1)
        self.pb_radiostation_8.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_8.setObjectName("pb_radiostation_8")
        self.gridLayout.addWidget(self.pb_radiostation_8, 4, 1, 1, 1)
        self.pb_radiostation_17 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_17.setIcon(icon1)
        self.pb_radiostation_17.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_17.setObjectName("pb_radiostation_17")
        self.gridLayout.addWidget(self.pb_radiostation_17, 12, 0, 1, 1)
        self.pb_radiostation_9 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_9.setIcon(icon1)
        self.pb_radiostation_9.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_9.setObjectName("pb_radiostation_9")
        self.gridLayout.addWidget(self.pb_radiostation_9, 5, 0, 1, 1)
        self.pb_radiostation_6 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_6.setIcon(icon1)
        self.pb_radiostation_6.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_6.setObjectName("pb_radiostation_6")
        self.gridLayout.addWidget(self.pb_radiostation_6, 2, 1, 1, 1)
        self.pb_radiostation_7 = QtWidgets.QPushButton(parent=self.sa_radios_scroll_content)
        self.pb_radiostation_7.setIcon(icon1)
        self.pb_radiostation_7.setIconSize(QtCore.QSize(64, 64))
        self.pb_radiostation_7.setObjectName("pb_radiostation_7")
        self.gridLayout.addWidget(self.pb_radiostation_7, 4, 0, 1, 1)
        self.sa_radios_scroll.setWidget(self.sa_radios_scroll_content)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\Python_PORTFOLIO312\\16_mp3_player_radio\\App_main\\UI\\../../App_icons/radio_icon_button_70x64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tb_main.addTab(self.tb_radio, icon2, "")
        mw_main.setCentralWidget(self.centralwidget)

        self.retranslateUi(mw_main)
        self.tb_main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mw_main)

    def retranslateUi(self, mw_main):
        _translate = QtCore.QCoreApplication.translate
        mw_main.setWindowTitle(_translate("mw_main", "Mp3 player and radio"))
        self.gb_now_play.setTitle(_translate("mw_main", "Now playing:"))
        self.pb_add_folder.setText(_translate("mw_main", " Add Folder"))
        self.pb_add_file.setText(_translate("mw_main", " Add Song"))
        self.pb_remove_all.setText(_translate("mw_main", " Remove all"))
        self.gb_status.setTitle(_translate("mw_main", "Status:"))
        self.lb_le_status.setText(_translate("mw_main", "song status"))
        self.lb_le_status_icon.setText(_translate("mw_main", "song status"))
        self.pb_start.setText(_translate("mw_main", "  Play"))
        self.pb_pause.setText(_translate("mw_main", "  Pause/Unpause"))
        self.pb_stop.setText(_translate("mw_main", " Stop"))
        self.pb_previous.setText(_translate("mw_main", "  Prev"))
        self.pb_next.setText(_translate("mw_main", "  Next"))
        self.groupBox.setTitle(_translate("mw_main", "Volume"))
        self.tb_main.setTabText(self.tb_main.indexOf(self.tb_player), _translate("mw_main", " Mp3 Player"))
        self.gb_now_listen.setTitle(_translate("mw_main", "Now listening:"))
        self.pb_start_radio.setText(_translate("mw_main", "  Start listening"))
        self.pb_stop_radio.setText(_translate("mw_main", "  Stop listening"))
        self.radio_status.setTitle(_translate("mw_main", "Status"))
        self.lb_le_radio_status.setText(_translate("mw_main", "not running"))
        self.lb_le_radio_status_icon.setText(_translate("mw_main", "radio status"))
        self.radio_volume.setTitle(_translate("mw_main", "Volume"))
        self.pb_radiostation_1.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_10.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_4.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_18.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_15.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_14.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_13.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_12.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_16.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_2.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_5.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_3.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_19.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_11.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_20.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_8.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_17.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_9.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_6.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.pb_radiostation_7.setText(_translate("mw_main", "Radiostation\n"
"Breakfast with Liam and Venetia"))
        self.tb_main.setTabText(self.tb_main.indexOf(self.tb_radio), _translate("mw_main", " Online radio"))
