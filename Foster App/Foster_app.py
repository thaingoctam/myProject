# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Settingwindown import *
from Mainwindown import *
from Arduino import*
from DrawRect import *
from os.path import expanduser
import cv2
import sys
import serial
import threading
import time
import serial.tools.list_ports
import sqlite3

class Foster_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.isCapturing = False
        self.workThread = WorkThread()
        self.pix=QtGui.QPixmap("Icon/demo.jpg")
        self.imageforprocess=cv2.imread("Icon/demo.jpg")
        self.ui.actionParameter.triggered.connect(self.setting_parameter)
        self.ui.actionArduino_Uno.triggered.connect(self.Arduino_setting)
        self.ui.pushButton_cameraON.clicked.connect(self.Startcam)
        self.ui.pushButton_cameraOFF.clicked.connect(self.Stopcam)
        self.ui.pushButton_cameraOFF.clicked.connect(self.Stopcam)
        #self.ui.actionExits.triggered.connect(self.deleteLater)
        self.ui.pushButton_connectArduino.clicked.connect(self.Serial)
        self.workThread.trigger.connect(self.capturesetting)
        self.workThread.Error.connect(self.ErrorEvent)
        self.pix1 = QtGui.QPixmap("Icon/Nocam.jpg")
        self.ui.label_videocam.setPixmap(self.pix1)
        self.show()

    def Startcam(self):
        self.isCapturing = True
        self.fps = 24
        self.cap = cv2.VideoCapture(0)
        self.ith_frame = 1
        self.Starttimmer()
        self.show()

    def Starttimmer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Displayframe)
        self.timer.start(1000./self.fps)

    def Displayframe(self):
        ret, self.frame= self.cap.read()
        self.imageforprocess=self.frame
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        img = QtGui.QImage(self.frame, self.frame.shape[1],self.frame.shape[0], QtGui.QImage.Format_RGB888)
        self.pix = QtGui.QPixmap.fromImage(img)
        self.ui.label_videocam.setPixmap(self.pix)

    def Stopcam(self):
        if self.isCapturing:
           self.isCapturing= False
           self.cap.release()
           self.timer.stop()
           cv2.destroyAllWindows()
           self.ui.label_videocam.setPixmap(self.pix1)

    def capturesetting(self):
            if self.ui.lineEdit.text() != None:
                cv2.imwrite(str(self.folderChoosen) + '/img_%s_%d.jpg' % (self.ui.lineEdit.text(),self.ith_frame), self.frame)
            else:
                cv2.imwrite(str(self.folderChoosen) + '/img_%d.jpg' % self.ith_frame, self.frame)
            self.ith_frame += 1

    def setting_parameter(self):
        self.setting = Setting_Windown(self.pix,self.imageforprocess)

    def Serial(self):
        self.workThread.start()

    def deleteLater(self):
        if self.isCapturing:
           self.cap.release()
           super(QWidget, self).deleteLater()
        else:
            self.close()

    @pyqtSlot()
    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self,
                                               "QUIT CAM",
                                               "Are you sure want Exist ?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def ErrorEvent(self):
        msg = QMessageBox()
        msg.setWindowTitle("Arduino UNO not found")
        msg.setText(" Please Connect Arduino UNO to Computer! ")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Retry)
        x = msg.exec_()
    def Arduino_setting(self):
        widget = QDialog(self)
        self.ui=Ui_Dialog()
        self.ui.setupUi(widget)
        widget.exec_()


class Arduino_UNO(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

class Setting_Windown(QMainWindow):
    def __init__(self,image,frame):
        super().__init__()
        self.ui = Ui_Setting()
        self.ui.setupUi(self)
        self.items=[]
        self.frame=frame
        self.image=image
        self.imageoutside=False
        self.conn = sqlite3.connect("Data_parameter.db")
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 640, 480)
        self.scene.addPixmap(QPixmap(self.image))
        self.grview = QGraphicsView(self.scene, self.ui.label_ImageSetting)
        self.grview.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.valueslide=self.ui.horizontalSlider_Rcolor.value()
        self.initiateRect()
        self.ui.pushButton_DrawRect.clicked.connect(self.drawrect)
        self.ui.pushButton_RemoveRect.clicked.connect(self.removerect)
        self.ui.pushButton_Saveallparameter.clicked.connect(self.SaveData)
        self.ui.pushButton_OpenImage.clicked.connect(self.openImage)
        self.ui.pushButton_testSample_Area.clicked.connect(self.GetResult)
        self.grview.clickItems.connect(self.showParameter)
        self.grview.moveItems.connect(self.move)
        self.ui.doubleSpinBox_Maxvalue_RGB_01.editingFinished.connect(self.UpdateDataOnList)
        self.ui.doubleSpinBox_Minvalue_RGB_01.editingFinished.connect(self.UpdateDataOnList)
        self.ui.horizontalSlider_Rcolor.sliderMoved.connect(self.UpdateDataOnList)
        self.ui.horizontalSlider_Gcolor.sliderMoved.connect(self.UpdateDataOnList)
        self.ui.horizontalSlider_Bcolor.sliderMoved.connect(self.UpdateDataOnList)
        self.scene.entered.connect(self.SaveDataOnList)
        self.show()

    def move(self):
        for i in range(len(self.items)):
            if self.items[i][0].isSelected():
                self.GetDataFromRect(self.items,i)
                self.threadProcessImage(self.x,self.y,self.width,self.height)

    @pyqtSlot()
    def SaveData(self):
        conn = sqlite3.connect('Data_parameter.db')
        conn.execute( "DELETE FROM  PARAMETER")
        for i in range(len(self.items)):
            self.GetDataFromRect(self.items,i)
            conn.execute("INSERT INTO  PARAMETER (Max_value, Min_value, Slide_valueR, Slide_valueG, Slide_valueB, x0, y0, Width, Height) VALUES (?,?,?,?,?,?,?,?,?);",
                         (self.maxvalue, self.minvalue, self.slidevalue_R,self.slidevalue_G,self.slidevalue_B, self.x, self.y, self.width, self.height))
            conn.commit()
        self.conn.close()

    def SaveDataOnList(self):
        for i in range(len(self.items)):
            if self.items[i][0].isSelected():
                self.GetDataFromRect(self.items,i)
                self.items[i]=(self.itemRect,self.maxvalue, self.minvalue, self.slidevalue_R,self.slidevalue_G,self.slidevalue_B, self.x, self.y, self.width, self.height,self.Pixitem)
                self.threadProcessImage(self.x,self.y,self.width,self.height)

    def GetDataFromRect(self,items,i):
        self.Pixitem=self.items[i][10]
        self.itemRect=self.items[i][0]
        self.x= items[i][0].sceneBoundingRect().left() + 4
        self.y= items[i][0].sceneBoundingRect().top() + 4
        self.width= items[i][0].sceneBoundingRect().width() - 8
        self.height=items[i][0].sceneBoundingRect().height() - 8
        self.maxvalue=items[i][1]
        self.minvalue=items[i][2]
        self.slidevalue_R=items[i][3]
        self.slidevalue_G=items[i][4]
        self.slidevalue_B=items[i][5]

    @pyqtSlot()
    def initiateRect(self):
        self.conn = sqlite3.connect('Data_parameter.db')
        cursor = self.conn.execute("SELECT count(*) as Quatity from PARAMETER")
        for row in cursor:
            quality=row[0]
        if quality!=0:
            cursor = self.conn.execute("SELECT * from PARAMETER")
            for row in cursor:
                self.value = GraphicsRectItem(row[6], row[7], row[8], row[9])
                self.value.setZValue(2)
                self.items.append((self.value,row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],None))
                self.scene.addItem(self.value)
        self.conn.close()

    @pyqtSlot()
    def drawrect(self):
            self.value = GraphicsRectItem(0, 0, 100, 50)
            self.value.setZValue(2)
            self.Pixmapitem=QGraphicsPixmapItem()
            self.Pixmapitem.setZValue(1)
            self.items.append((self.value,0,0,0,0,0,0,0,100,50,self.Pixmapitem))
            self.scene.addItem(self.value)

    @pyqtSlot()
    def removerect(self):
        for i in self.items:
            if i[0].isSelected():
                self.scene.removeItem(i[0])
                self.scene.removeItem(i[10])
                self.items.remove(i)

    @pyqtSlot()
    def showParameter(self):
        count=0
        for i in range(0,len(self.items)):
            if self.items[i][0].isSelected():
                self.ui.doubleSpinBox_Maxvalue_RGB_01.setEnabled(True)
                self.ui.doubleSpinBox_Maxvalue_RGB_01.setValue(self.items[i][1])
                self.ui.doubleSpinBox_Minvalue_RGB_01.setEnabled(True)
                self.ui.doubleSpinBox_Minvalue_RGB_01.setValue(self.items[i][2])
                self.ui.horizontalSlider_Rcolor.setEnabled(True)
                self.ui.horizontalSlider_Rcolor.setValue(self.items[i][3])
                self.ui.horizontalSlider_Gcolor.setEnabled(True)
                self.ui.horizontalSlider_Gcolor.setValue(self.items[i][4])
                self.ui.horizontalSlider_Bcolor.setEnabled(True)
                self.ui.horizontalSlider_Bcolor.setValue(self.items[i][5])
                self.GetDataFromRect(self.items,i)
                self.threadProcessImage(self.x,self.y,self.width,self.height)
                count=1
            if count==0:
                self.lockParameter()

    @pyqtSlot()
    def lockParameter(self):
        self.ui.doubleSpinBox_Maxvalue_RGB_01.setEnabled(False)
        self.ui.doubleSpinBox_Minvalue_RGB_01.setEnabled(False)
        self.ui.horizontalSlider_Rcolor.setEnabled(False)
        self.ui.horizontalSlider_Gcolor.setEnabled(False)
        self.ui.horizontalSlider_Bcolor.setEnabled(False)

    @pyqtSlot()
    def UpdateDataOnList(self):
        for i in range(len(self.items)):
            if self.items[i][0].isSelected():
                self.GetDataFromRect(self.items, i)
                maxvalue=self.ui.doubleSpinBox_Maxvalue_RGB_01.value()
                minvalue = self.ui.doubleSpinBox_Minvalue_RGB_01.value()
                slidevalue_R = self.ui.horizontalSlider_Rcolor.value()
                slidevalue_G = self.ui.horizontalSlider_Gcolor.value()
                slidevalue_B = self.ui.horizontalSlider_Bcolor.value()
                self.ui.label_value_sliderchangeR.setText(str(slidevalue_R)+ "%")
                self.ui.label_value_sliderchangeG.setText(str(slidevalue_G) + "%")
                self.ui.label_value_sliderchangeB.setText(str(slidevalue_B) + "%")
                self.items[i]=(self.items[i][0],maxvalue,minvalue,slidevalue_R,slidevalue_G,slidevalue_B,self.x, self.y, self.width, self.height,self.Pixitem)
        self.threadProcessImage(self.x,self.y,self.width,self.height)

    @pyqtSlot()
    def threadProcessImage(self,x,y,width,height):
        if self.imageoutside:
            self.imageforprocess=self.imageopen1
        else:
            self.imageforprocess=self.frame
        gray = cv2.cvtColor(self.imageforprocess, cv2.COLOR_BGR2GRAY)
        ret, self.processedImage = cv2.threshold(gray[int(y):int(y+height), int(x):int(x+width)], self.ui.horizontalSlider_Rcolor.value(),255, cv2.THRESH_BINARY)
        self.displayImage(x,y)

    def displayImage(self,x,y):
        qformat = QImage.Format_Indexed8
        if len(self.processedImage.shape) == 3:  # rows[0],cols[1],channels[2]
            print(self.processedImage.shape)
            if (self.processedImage.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.processedImage, self.processedImage.shape[1], self.processedImage.shape[0],self.processedImage.strides[0], qformat)
        img = img.rgbSwapped()
        self.pixm = QtGui.QPixmap.fromImage(img)
        self.CreateListPixmapIterm(self.pixm,x,y)

    def CreateListPixmapIterm(self,pix,x,y):
        for i in range(len(self.items)):
            if self.items[i][0].isSelected():
                self.scene.removeItem(self.items[i][10])
                self.pixmapiterm = QGraphicsPixmapItem(pix)
                self.pixmapiterm .setPos(x, y)
                self.pixmapiterm .setZValue(1)
                self.scene.addItem(self.pixmapiterm)
                self.GetDataFromRect(self.items, i)
                self.items[i] = (self.itemRect, self.maxvalue, self.minvalue, self.slidevalue_R, self.slidevalue_G, self.slidevalue_B, self.x, self.y, self.width, self.height,self.pixmapiterm)

    def openImage(self):
        fileChoosen = QFileDialog.getOpenFileName(self, 'Open Files', 'D:\\', "Image Files (*.jpg *.png)")
        print(fileChoosen)
        if fileChoosen[0] != '':
            imagepath=fileChoosen[0]
            self.image=QPixmap(imagepath)
            self.scene.addPixmap(self.image)
            self.imageopen1 = cv2.imread(fileChoosen[0])
            self.imageopen = self.image.copy()
            self.imageoutside = True
        else:
            pass

    def GetResult(self):
        gettotalResult=0
        for i in range(len(self.items)):
            if self.items[i][0].isSelected():
                cal=self.Calculate_area(i)
                if cal:
                    self.ui.label_Result_test.setText("OK One")
                    return True
                else:
                    self.ui.label_Result_test.setText("NG One")
                    return False

        for i in range(len(self.items)):
            cal=self.Calculate_area(i)
            if cal:
                gettotalResult+=1
        if gettotalResult==len(self.items):
            text= "OK Total: %d / %d" %(gettotalResult,len(self.items))
            self.ui.label_Result_test.setText(text)
            return True
        else:
            text= "NG Total: %d / %d" %(gettotalResult,len(self.items))
            self.ui.label_Result_test.setText(text)
            return False





    def Calculate_area(self,count):
        if self.imageoutside:
            self.imageforprocess = self.imageopen1
        else:
            self.imageforprocess = self.frame
        self.GetDataFromRect(self.items, count)
        gray = cv2.cvtColor(self.imageforprocess, cv2.COLOR_BGR2GRAY)
        ret, self.processedImage = cv2.threshold(gray[int(self.y):int(self.y + self.height), int(self.x):int(self.x + self.width)], self.slidevalue_R, 255,cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(self.processedImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        c = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(c) / 100
        #print(area)
        if area >= self.minvalue and area <= self.maxvalue:
            return True
        else:
            return False


class QGraphicsView(QGraphicsView):
    clickItems = pyqtSignal()
    moveItems = pyqtSignal()
    def __init__(self,*args):
        super().__init__(*args)
    def mousePressEvent(self,event):
        super().mousePressEvent(event)
        self.clickItems.emit()
    def mouseMoveEvent(self,event):
        super().mouseMoveEvent(event)
        self.moveItems.emit()

class WorkThread(QThread):
    trigger = pyqtSignal()
    Error = pyqtSignal()
    def __init__(self):
        super().__init__()
    def run(self):
        ports = serial.tools.list_ports.comports(include_links=False)
        if len(ports)!=0:
           for port in ports:
               ser = serial.Serial(port.device)
           if ser.isOpen():
               ser.close()
               ser = serial.Serial(port.device, 9600)
           while (1):
               data = ser.readline().decode("utf-8").strip('\n').strip('\r')
               time.sleep(0.1)
               if data == "Cam ON":
                   print("Fail")
               else:
                   print("Succed")
                   self.trigger.emit()
        else:
            self.Error.emit()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Foster_app()
    w.show()
    sys.exit(app.exec_())