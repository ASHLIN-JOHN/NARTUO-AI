import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtGui
from mainGUIFile import Ui_Dialog

class mainfile(QDialog):
    def __init__(self):
        super(mainfile, self).__init__()
        print("SETTING UP GUI")
        self.firstUI = Ui_Dialog()
        self.firstUI.setupUi(self)

        self.firstUI.movie = QtGui.QMovie("D:\\NARUTO AI\\LOGO\\uzumkai logo.gif")
        self.firstUI.uzumakilogo.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()

        self.firstUI.loginbutton.clicked.connect(self.connectloginwin)
        self.firstUI.exitbutton.clicked.connect(self.close)

    def connectloginwin(self):
        from subprocess import call
        self.close()
        call(["python", "loginwindowmain.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainfile()
    ui.show()
    sys.exit(app.exec_())
