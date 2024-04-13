import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from contactsfile import Ui_ContactFile
from PyQt5 import QtGui

class ContactWindow(QWidget):
    def __init__(self):
        super(ContactWindow, self).__init__()
        print("SETTING UP GUI")
        self.contactUI = Ui_ContactFile()
        self.contactUI.setupUi(self)

        self.contactUI.cancelbutton.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactWindow()
    window.show()
    sys.exit(app.exec_())