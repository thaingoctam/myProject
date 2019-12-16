# _*_ coding:utf-8 _*_
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
        self.ui.horizontalSlider.sliderMoved.connect(self.seekPosition)
        self.ui.horizontalSlider_2.sliderMoved.connect(self.volume)
        self.player.positionChanged.connect(self.qmp_positionChanged)
        self.player.audioAvailableChanged.connect(self.changeAlbum)
        self.player.durationChanged.connect(self.update_duration)
        self.timer=QTimer(self)
        self.show()

    def openFile(self):
        fileChoosen = QFileDialog.getOpenFileName(self, 'Open Music File', expanduser('~'), 'Audio (*.mp3 *.ogg *.wav)',
                                                  '*.mp3 *.ogg *.wav')
        if fileChoosen != None:
            self.currentPlaylist.addMedia(QMediaContent(QUrl.fromLocalFile(fileChoosen[0])))

    def folderOpen(self):
        folderAc = QAction('Open Folder', self)
        folderAc.setShortcut('Ctrl+D')
        folderAc.setStatusTip('Open Folder (Will add all the files in the folder) ')
        folderAc.triggered.connect(self.addFiles)
        return folderAc


    def addFiles(self):
        folderChoosen = QFileDialog.getExistingDirectory(self, 'Open Music Folder', expanduser('~'))                      # HÀM trả về đường dẫn hiện có được người dùng chỉ đinh
        if folderChoosen != None:
            it = QDirIterator(folderChoosen)          # QDirIterator trả về 1 list các file name và đường dẫn của file đó ,Interator là hàm duyệt qua từng phần tử
            it.next()                                 # Hàm trả về item hiện tại và di chuyển con trỏ dến item kế tiếp trong 1 trình vòng lặp
            while it.hasNext():                       # Hàm trả về True nếu Iterator còn Item kế tiếp Item đang duyệt
                if it.fileInfo().isDir() == False and it.filePath() != '.':            # QFileInfo::isDir()  trả về True nếu đối tượng trỏ tói đường dẫn, hoặc một liên kết. Ngược lại là False
                    fInfo = it.fileInfo()             #QDirIterator::fileInfo() const hàm trả về thông tin filename,đường dẫn của file
                    print(it.filePath(), fInfo.suffix())                                                                  # QFileInfo::suffix() const Hàm trả về phần mở rộng của File
                    if fInfo.suffix() in ('mp3', 'ogg', 'wav'):
                        print('added file ', fInfo.fileName())
                        self.currentPlaylist.addMedia(QMediaContent(QUrl.fromLocalFile(it.filePath()))) #currentPlaylist::addMedia(const QMediaContent &content) thêm media vào danh sách phát hiện tại(playlist tạo mới nếu dùng Qmedialplaylist) . trả về True nếu thành công, và False nếu ngược lại
                it.next()

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
                if self.currentPlaylist.mediaCount() == 0:  # mediaCount() Trả về số Item trong playlist
                    self.statusBar().show()
                    self.statusBar().showMessage('No song for play!')
                    self.timer.start(7000)
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
                self.player.setPosition(position)

    def volume(self, position):
        sender = self.sender()
        if isinstance(sender, QSlider):
            if self.ui.horizontalSlider.mouseReleaseEvent:
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

            self.ui.label_2.setText('Playing: %s' % self.player.metaData("Title"))
            self.ui.label_2.setAlignment(Qt.AlignRight)

            width = self.ui.label_2.fontMetrics().boundingRect(self.ui.label_2.text()).width()

            self.anim = QPropertyAnimation(self.ui.label_2, b"geometry")
            self.anim.setDuration(12000)
            self.anim.setLoopCount(-1)  # lặp lại vô tận
            self.anim.setKeyValueAt(0, QRect(220-width, 0, width + 2, 30))
            #self.anim.setKeyValueAt(0, QRect(230, 0, width+2, 30))
            #self.anim.setKeyValueAt(0.5, QRect(540-width, 0, width+2, 30))
            #self.anim.setKeyValueAt(1, QRect(230, 0, width+2, 30))
            self.anim.setKeyValueAt(1, QRect(550, 0, width + 2, 30))
            self.anim.start()




    def prevItemPlaylist(self):
        self.player.playlist().previous()

    def nextItemPlaylist(self):
        self.player.playlist().next()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())