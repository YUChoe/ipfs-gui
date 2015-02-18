# -*- coding: UTF-8 -*-
__author__ = 'pp'


from PySide import QtGui
from PySide import QtCore
#import yaml
import sys

class MainWindow (QtGui.QWidget) :
    def __init__(self):
        super(MainWindow, self).__init__()
        self.codec = QtCore.QTextCodec.codecForName("UTF-8")
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ipfs-gui - beta')

        self.initButton = QtGui.QPushButton("init", self)
        self.initButton.move(10, 100)
        self.initButton.clicked.connect(self.do_init)
        self.setGeometry(300, 200, 275, 330)# position x, y , width, height
        self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())
        self.setFixedSize(self.size())
        palette = self.palette()
        #palette.setColor( self.backgroundRole(), QtGui.QColor(128,128,128))
        palette.setColor( self.backgroundRole(), QtGui.QColor(255,255,255))
        self.setPalette(palette)

        self.show()

    def do_init(self):
        print "do_init"

def main() :
  app = QtGui.QApplication(sys.argv)
  thisapp = MainWindow()
  sys.exit(app.exec_())

if __name__ == "__main__" :
  main()