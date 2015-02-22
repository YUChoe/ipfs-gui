# -*- coding: UTF-8 -*-
__author__ = 'https://github.com/YUChoe'


from PySide import QtGui
from PySide import QtCore
#import yaml
import os
import sys
import logging

class MainWindow (QtGui.QWidget) :
    def __init__(self):
        super(MainWindow, self).__init__()
        self.codec = QtCore.QTextCodec.codecForName("UTF-8")
        self.UIbuttons = []
        self.features = ['resume', 'install', 'init', 'add', 'cat', 'ls', 'quit']

        self.initUI()

    def initUI(self):
        self.setWindowTitle('ipfs-gui - beta')

        self.sub_left_initUI()

        self.setGeometry(300, 200, 275, 330)# position x, y , width, height
        self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())
        self.setFixedSize(self.size())
        palette = self.palette()
        #palette.setColor( self.backgroundRole(), QtGui.QColor(128,128,128))
        palette.setColor( self.backgroundRole(), QtGui.QColor(255,255,255))
        self.setPalette(palette)

        self.show()
        self.activateWindow()


    def sub_left_initUI(self):
        _x = 2
        _y_start_point = 2
        _height = 22
        for bname in self.features :
            obtn = QtGui.QPushButton(bname, self)
            _y = (self.features.index(bname) * _height) + _y_start_point
            obtn.move(_x, _y)
            obtn.setFixedWidth(100)

            obtn.clicked.connect(self.evnt_clicked(str(bname)))
            #obtn.clicked.connect(lambda: self.evnt_clicked(str(bname)))
            #obtn.clicked.connect(partial(self.evnt_clicked), bname)
            #obtn.clicked.connect(self.evnt_clicked, [bname])

            print self.features.index(bname), str(bname), _x, _y
            self.UIbuttons.append(obtn)
            #del obtn
        self.show()

    def evnt_clicked(self, bname):
        fname = sys._getframe().f_code.co_name
        def _evnt_clicked():
            _debug(fname, bname)
            if bname not in self.features :
                return False
            # 'resume', 'install', 'init', 'add', 'cat', 'ls', 'quit']
            if bname == "resume" :
                if os.path.isfile("") != True :
                    pass
            elif bname == 'quit' :
                sys.exit()

        return _evnt_clicked

# --- EOC ---

def _debug(fname, str) :
    logging.debug("%s %s" %(fname, str))

def main() :
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    app = QtGui.QApplication(sys.argv)
    thisapp = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__" :
    main()