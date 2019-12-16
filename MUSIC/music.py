# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'music.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Player_Music(object):
    def setupUi(self, Player_Music):
        Player_Music.setObjectName("Player_Music")
        Player_Music.setEnabled(True)
        Player_Music.resize(541, 357)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Player_Music.sizePolicy().hasHeightForWidth())
        Player_Music.setSizePolicy(sizePolicy)
        Player_Music.setMinimumSize(QtCore.QSize(541, 357))
        Player_Music.setMaximumSize(QtCore.QSize(541, 357))
        Player_Music.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_music/headphone_app.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Player_Music.setWindowIcon(icon)
        Player_Music.setWindowOpacity(1.0)
        Player_Music.setToolTip("")
        Player_Music.setAutoFillBackground(False)
        Player_Music.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        Player_Music.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        Player_Music.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Player_Music)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 200, 541, 141))
        self.frame.setStyleSheet("background-color:rgb(56, 103, 164);\n"
"\n"
"margin-bottom:0;\n"
"padding-bottom:0;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalSlider = QtWidgets.QSlider(self.frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 90, 441, 41))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 3px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background:white;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(247, 94, 112);\n"
"    border: 2px solid black;\n"
"    width: 13px;\n"
"    margin:-7px 0;\n"
"    border-radius: 7px;\n"
"}")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_01 = QtWidgets.QLabel(self.frame)
        self.label_01.setEnabled(True)
        self.label_01.setGeometry(QtCore.QRect(500, 100, 31, 21))
        self.label_01.setAutoFillBackground(False)
        self.label_01.setStyleSheet("background-color: rgb(56, 103, 164);\n"
"color: rgb(255, 255, 255);")
        self.label_01.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_01.setObjectName("label_01")
        self.label_00 = QtWidgets.QLabel(self.frame)
        self.label_00.setGeometry(QtCore.QRect(10, 100, 31, 21))
        self.label_00.setStyleSheet("background-color: rgb(56, 103, 164);\n"
"color: rgb(255, 255, 255);")
        self.label_00.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_00.setObjectName("label_00")
        self.play_pause_pushButton = QtWidgets.QPushButton(self.frame)
        self.play_pause_pushButton.setGeometry(QtCore.QRect(220, 30, 51, 51))
        self.play_pause_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.play_pause_pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.play_pause_pushButton.setToolTip("Pause Song")
        self.play_pause_pushButton.setStyleSheet("QPushButton {\n"
"\n"
"border-radius:15px; }\n"
"\n"
"QPushButton:hover {\n"
"Border: 2px solid rgb(54, 40, 79);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(58, 67, 70);\n"
"Border: none;\n"
" }\n"
"\n"
"\n"
"\n"
" ")
        self.play_pause_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icon_music/play_btt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("Icon_music/stop_btt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.play_pause_pushButton.setIcon(icon1)
        self.play_pause_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.play_pause_pushButton.setCheckable(True)
        self.play_pause_pushButton.setFlat(False)
        self.play_pause_pushButton.setObjectName("play_pause_pushButton")
        self.Next_pushButton = QtWidgets.QPushButton(self.frame)
        self.Next_pushButton.setGeometry(QtCore.QRect(290, 30, 51, 51))
        self.Next_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Next_pushButton.setStyleSheet("QPushButton {\n"
"margin:5px;\n"
"border-radius:15px; }\n"
"\n"
"QPushButton:hover {\n"
"Border: 2px solid rgb(54, 40, 79);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(58, 67, 70);\n"
"Border: none;\n"
" }")
        self.Next_pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon_music/next_btt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next_pushButton.setIcon(icon2)
        self.Next_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.Next_pushButton.setFlat(True)
        self.Next_pushButton.setObjectName("Next_pushButton")
        self.previous_pushButton = QtWidgets.QPushButton(self.frame)
        self.previous_pushButton.setGeometry(QtCore.QRect(150, 30, 51, 51))
        self.previous_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.previous_pushButton.setStyleSheet("QPushButton {\n"
"margin:5px;\n"
"border-radius:15px; }\n"
"\n"
"QPushButton:hover {\n"
"Border: 2px solid rgb(54, 40, 79);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(58, 67, 70);\n"
"Border: none;\n"
" }")
        self.previous_pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icon_music/previous_btt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_pushButton.setIcon(icon3)
        self.previous_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.previous_pushButton.setAutoDefault(False)
        self.previous_pushButton.setFlat(False)
        self.previous_pushButton.setObjectName("previous_pushButton")
        self.Repeat_pushButton = QtWidgets.QPushButton(self.frame)
        self.Repeat_pushButton.setGeometry(QtCore.QRect(70, 30, 51, 51))
        self.Repeat_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Repeat_pushButton.setStyleSheet("QPushButton {\n"
"margin:4px;\n"
"border-radius:15px; }\n"
"\n"
"QPushButton:hover {\n"
"Border: 2px solid rgb(54, 40, 79);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(58, 67, 70);\n"
"Border: none;\n"
" }")
        self.Repeat_pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icon_music/NoRepeat_btt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("Icon_music/Repeat_btt.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Repeat_pushButton.setIcon(icon4)
        self.Repeat_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.Repeat_pushButton.setCheckable(True)
        self.Repeat_pushButton.setFlat(True)
        self.Repeat_pushButton.setObjectName("Repeat_pushButton")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(400, 40, 91, 31))
        self.horizontalSlider_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_2.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 2px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background:white;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(247, 94, 112);\n"
"    border: 2px solid black;\n"
"    width: 13px;\n"
"    margin:-8px 0;\n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.Voice_label = QtWidgets.QLabel(self.frame)
        self.Voice_label.setEnabled(True)
        self.Voice_label.setGeometry(QtCore.QRect(500, 40, 31, 31))
        self.Voice_label.setAutoFillBackground(False)
        self.Voice_label.setStyleSheet("background-color: rgb(56, 103, 164);\n"
"color: rgb(255, 255, 255);")
        self.Voice_label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Voice_label.setObjectName("Voice_label")
        self.volume = QtWidgets.QPushButton(self.frame)
        self.volume.setGeometry(QtCore.QRect(360, 40, 41, 31))
        self.volume.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.volume.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.volume.setToolTip("Mute")
        self.volume.setStyleSheet(" QPushButton {\n"
"\n"
"boder:none;\n"
"border-radius:23px; }\n"
"\n"
"")
        self.volume.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icon_music/volume_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("Icon_music/volume_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.volume.setIcon(icon5)
        self.volume.setIconSize(QtCore.QSize(25, 25))
        self.volume.setCheckable(True)
        self.volume.setFlat(False)
        self.volume.setObjectName("volume")
        self.Album = QtWidgets.QLabel(self.centralwidget)
        self.Album.setGeometry(QtCore.QRect(0, 0, 221, 201))
        self.Album.setMaximumSize(QtCore.QSize(221, 16777215))
        self.Album.setStyleSheet("")
        self.Album.setText("")
        self.Album.setScaledContents(True)
        self.Album.setWordWrap(False)
        self.Album.setObjectName("Album")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(216, 0, 331, 201))
        self.label_2.setStyleSheet("font: 87 12pt \"Arial\";\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.Album.raise_()
        self.frame.raise_()
        Player_Music.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Player_Music)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 21))
        self.menubar.setAcceptDrops(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setAutoFillBackground(False)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Player_Music.setMenuBar(self.menubar)
        self.actionOpen_File = QtWidgets.QAction(Player_Music)
        self.actionOpen_File.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionOpen_File.setVisible(True)
        self.actionOpen_File.setMenuRole(QtWidgets.QAction.NoRole)
        self.actionOpen_File.setPriority(QtWidgets.QAction.HighPriority)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_Folder = QtWidgets.QAction(Player_Music)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionInfo_Song = QtWidgets.QAction(Player_Music)
        self.actionInfo_Song.setObjectName("actionInfo_Song")
        self.actionExit = QtWidgets.QAction(Player_Music)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_Author = QtWidgets.QAction(Player_Music)
        self.actionAbout_Author.setObjectName("actionAbout_Author")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.actionInfo_Song)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_Author)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Player_Music)
        QtCore.QMetaObject.connectSlotsByName(Player_Music)

    def retranslateUi(self, Player_Music):
        _translate = QtCore.QCoreApplication.translate
        Player_Music.setWindowTitle(_translate("Player_Music", "Player Music"))
        self.label_01.setText(_translate("Player_Music", "0:00"))
        self.label_00.setText(_translate("Player_Music", "0:00"))
        self.Next_pushButton.setToolTip(_translate("Player_Music", "Next Song"))
        self.previous_pushButton.setToolTip(_translate("Player_Music", "Previous Song"))
        self.Repeat_pushButton.setToolTip(_translate("Player_Music", "Repeat All"))
        self.Voice_label.setText(_translate("Player_Music", "0:00"))
        self.menuFile.setTitle(_translate("Player_Music", "File"))
        self.menuHelp.setTitle(_translate("Player_Music", "Help"))
        self.actionOpen_File.setText(_translate("Player_Music", "Open File"))
        self.actionOpen_File.setShortcut(_translate("Player_Music", "Ctrl+O"))
        self.actionOpen_Folder.setText(_translate("Player_Music", "Open Folder"))
        self.actionOpen_Folder.setShortcut(_translate("Player_Music", "Ctrl+D"))
        self.actionInfo_Song.setText(_translate("Player_Music", "Info Song"))
        self.actionInfo_Song.setShortcut(_translate("Player_Music", "Ctrl+I"))
        self.actionExit.setText(_translate("Player_Music", "Exit "))
        self.actionExit.setShortcut(_translate("Player_Music", "Ctrl+E"))
        self.actionAbout_Author.setText(_translate("Player_Music", "About Author"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Player_Music = QtWidgets.QMainWindow()
    ui = Ui_Player_Music()
    ui.setupUi(Player_Music)
    Player_Music.show()
    sys.exit(app.exec_())

