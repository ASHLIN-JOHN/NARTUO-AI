import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from loginwindow import Ui_loginWindowClass
from PyQt5 import QtGui

class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        print("SETTING UP GUI")
        self.loginUI = Ui_loginWindowClass()
        self.loginUI.setupUi(self)

        self.loginUI.accessdenied.hide()
        self.loginUI.password.setEchoMode(QLineEdit.Password)

        self.loginUI.accessdeniedMovie = QtGui.QMovie("D:\\NARUTO AI\\QT\\loginWindowClass\\GUI KEYS\\ACCDSS DEN.gif")
        self.loginUI.accessdenied.setMovie(self.loginUI.accessdeniedMovie)

        self.loginUI.exitbutton.clicked.connect(self.close)
        self.loginUI.retrybutton.clicked.connect(self.retryButton)
        self.loginUI.loginbutton.clicked.connect(self.validatelogin)


    def startMovie(self):
        self.loginUI.accessdenied.show()
        self.loginUI.accessdeniedMovie.start()

    def stopMovie(self):
        self.loginUI.accessdenied.hide()
        self.loginUI.accessdeniedMovie.start()

    def retryButton(self):
        self.loginUI.username.clear()
        self.loginUI.password.clear()
        self.stopMovie()

    def validatelogin(self):
        username = self.loginUI.username.text()
        password = self.loginUI.password.text()
        if username == "ashlin" and password == "!@#$":
            self.close()
            self.naruto()
        else:
            self.startMovie()

    def naruto(self):
        from NARUTO import Naruto
        self.loginUI.loginbutton.clicked.connect(Naruto)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LoginWindow()
    ui.show()
    sys.exit(app.exec_())
