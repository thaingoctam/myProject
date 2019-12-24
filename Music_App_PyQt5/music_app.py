
# _*_ coding:utf-8 _*_
# App play music on PC, and im studying QT_FrameWork
# I hope you like this APP !

import sys
from mutagen import File as MutaFile
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from  PyQt5 import *
from music import *
#from PyQt5.QtWebEngineWidgets import *
class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Player_Music()
        self.ui.setupUi(self)
        self.currentPlaylist = QMediaPlaylist()
        self.player = QMediaPlayer()
        self.ui.actionOpen_File.triggered.connect(self.openFile)
        self.ui.actionOpen_Folder.triggered.connect(self.addFiles)
        self.ui.play_pause_pushButton.clicked.connect(self.btnplaystate)
        self.ui.previous_pushButton.clicked.connect(self.prevItemPlaylist)
        self.ui.Next_pushButton.clicked.connect(self.nextItemPlaylist)
        self.ui.volume.clicked.connect(self.volumestate)
        # set up initial volume
        self.ui.horizontalSlider_2.setValue(50)
        self.volume(50)
        self.ui.horizontalSlider.sliderMoved.connect(self.seekPosition)
        self.ui.horizontalSlider.press_slide.connect(self.seekPosition)
        self.ui.horizontalSlider_2.press_slide.connect(self.volume)
        self.ui.horizontalSlider_2.valueChanged.connect(self.volume)
        self.ui.actionAbout_Author.triggered.connect(self.Author)
        self.ui.Repeat_pushButton.clicked.connect(self.btnrepeatstate)
        self.player.positionChanged.connect(self.qmp_positionChanged)
        self.player.audioAvailableChanged.connect(self.changeAlbum)
        self.player.durationChanged.connect(self.update_duration)
        # timer for display starus Bar
        self.timer=QTimer(self)
        self.show()

# function open File audio
    def openFile(self):
        fileChoosen = QFileDialog.getOpenFileName(self, 'Open Music File', expanduser('~'), 'Audio (*.mp3 *.ogg *.wav)',
                                                  '*.mp3 *.ogg *.wav')
        if fileChoosen != None:
            self.currentPlaylist.addMedia(QMediaContent(QUrl.fromLocalFile(fileChoosen[0])))
# Function open Folder
    def folderOpen(self):
        folderAc = QAction('Open Folder', self)
        folderAc.setShortcut('Ctrl+D')
        folderAc.setStatusTip('Open Folder (Will add all the files in the folder) ')
        folderAc.triggered.connect(self.addFiles)
        return folderAc
    def addFiles(self):
        folderChoosen = QFileDialog.getExistingDirectory(self, 'Open Music Folder', expanduser('~'))
        if folderChoosen != None:
            it = QDirIterator(folderChoosen)
            it.next()
            while it.hasNext():
                if it.fileInfo().isDir() == False and it.filePath() != '.':
                    fInfo = it.fileInfo()             #
                    print(it.filePath(), fInfo.suffix())
                    if fInfo.suffix() in ('mp3', 'ogg', 'wav'):
                        print('added file ', fInfo.fileName())
                        self.currentPlaylist.addMedia(QMediaContent(QUrl.fromLocalFile(it.filePath())))
                it.next()
# Function check status of button play/pause
    def btnplaystate(self):
        if self.ui.play_pause_pushButton.isChecked():
             self.playHandler()
        else:
             self.pauseHandler()

    def playHandler(self):
        self.userAction = 1
        if self.player.state() == QMediaPlayer.StoppedState:
            if self.player.mediaStatus() == self.player.NoMedia:
                # self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.currentFile)))
                if self.currentPlaylist.mediaCount() == 0:
                    self.statusBar().show()
                    self.statusBar().showMessage('No song for play!')
                    self.timer.start(6000)
                    self.timer.timeout.connect(self.PlotUpdate)
                if self.currentPlaylist.mediaCount() != 0:
                    self.player.setPlaylist(self.currentPlaylist)
            elif self.player.mediaStatus() == QMediaPlayer.LoadedMedia:
                self.player.play()
            elif self.player.mediaStatus() == QMediaPlayer.BufferedMedia:
                self.player.play()
        elif self.player.state() == QMediaPlayer.PlayingState:
            pass
        elif self.player.state() == QMediaPlayer.PausedState:
            self.player.play()

    def pauseHandler(self):
        self.userAction = 2
        self.player.pause()
        self.timer.stop()

    def volumestate(self):
        if self.ui.volume.isChecked():
            self.player.setMuted(True)
            self.ui.Voice_label.setText('Muted')
        else:
            self.player.setMuted(False)
            self.ui.Voice_label.setText('%d' % (int(self.ui.horizontalSlider_2.value())))

    def PlotUpdate(self):
        self.statusBar().clearMessage()
        self.statusBar().hide()

    def seekPosition(self, position):
        sender = self.sender()
        if isinstance(sender, QSlider):
            if self.player.isSeekable():
                if self.ui.horizontalSlider.mouseReleaseEvent:
                    self.player.setPosition(position)

    def volume(self, position):
        #sender = self.sender()
        #if isinstance(sender, QSlider):
            #if self.ui.horizontalSlider_2.mouseReleaseEvent:
               self.player.setVolume(position)
               self.ui.Voice_label.setText('%d' % (int(position)))

    def qmp_mediaStatusChanged(self):
        if self.player.mediaStatus() == QMediaPlayer.LoadedMedia and self.userAction == 1:
            durationT = self.player.duration()
            self.ui.horizontalSlider.setRange(0, durationT)
            self.ui.label_01.setText(
                '%d:%02d' % (int(durationT / 60000), int((durationT / 1000) % 60)))
            self.player.play()

    def update_duration(self):

            durationT = self.player.duration()
            self.ui.horizontalSlider.setRange(0, durationT)
            self.ui.label_01.setText(
                '%d:%02d' % (int(durationT / 60000), int((durationT / 1000) % 60)))
            self.player.play()


    def qmp_positionChanged(self, position, senderType=False):
        if senderType == False:
            self.ui.horizontalSlider.setValue(position)
            # update the text label
        self.ui.label_00.setText('%d:%02d' % (int(position / 60000), int((position / 1000) % 60)))

# Function display Art Album and animation Text
    def changeAlbum(self):
        if self.player.isAudioAvailable():
            pixmap = QtGui.QPixmap()
            art_album=self.player.currentMedia().canonicalUrl().toString()
            url_return= art_album.replace("file:///",'')
            metadata = MutaFile(url_return)
            for tag in metadata.tags.values():
                if tag.FrameID == 'APIC':
                   pixmap.loadFromData(tag.data)
            self.ui.Album.setPixmap(pixmap)

            self.ui.label_2.setText('Playing: %s \n\nSinger: %s' % (self.player.metaData("Title"),self.player.metaData("AlbumArtist")))
            self.ui.label_2.setAlignment(Qt.AlignLeft)

            width = self.ui.label_2.fontMetrics().boundingRect(self.ui.label_2.text()).width()

            self.anim = QPropertyAnimation(self.ui.label_2, b"geometry")
            self.anim.setDuration(10000)
            self.anim.setLoopCount(-1)  # lặp lại vô tận
            self.anim.setKeyValueAt(0, QRect(220-width, 0, width + 2, 60))
#            self.anim.setKeyValueAt(0, QRect(230, 0, width+2, 30))
#            self.anim.setKeyValueAt(0.5, QRect(540-width, 0, width+2, 30))
#            self.anim.setKeyValueAt(1, QRect(230, 0, width+2, 30))
            self.anim.setKeyValueAt(1, QRect(550, 0, width + 2, 60))
            self.anim.start()


    def prevItemPlaylist(self):
        if self.currentPlaylist.mediaCount() != 0:
           self.player.playlist().previous()

    def nextItemPlaylist(self):
        if self.currentPlaylist.mediaCount() != 0:
           self.player.playlist().next()

    def Author(self):
        infoBox = QMessageBox(self)
        infoBox.setWindowTitle('About Author')
        infoBox.setTextFormat(Qt.RichText)
        infoBox.setText('<tr><td>This is the first App of me.</td></tr> <tr><td>Thank You have use this App.</td></tr>  '
                        '<tr><td>If you like Please contact with me on:</td></tr> '
                        '<tr><td>FaceBook: https://www.facebook.com/tam.thaingoc </td></tr> '
                        '<tr><td>Or Gmail: Thaingoctam11cdt2@gmail.com!</td></tr>')
        infoBox.addButton('OK', QMessageBox.AcceptRole)
        infoBox.show()

# Function repeat the song
    def btnrepeatstate(self):
        if self.ui.Repeat_pushButton.isChecked():
             self.currentPlaylist.setPlaybackMode(QtMultimedia.QMediaPlaylist.CurrentItemInLoop)
        else:
            self.currentPlaylist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())