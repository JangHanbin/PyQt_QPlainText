import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtWidgets import QPlainTextEdit

alertHtml = "<font color=\"DeepPink\">";
notifyHtml = "<font color=\"Lime\">";
infoHtml = "<font color=\"Aqua\">";
endHtml = "</font><br>";


class my_app(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt QPlaintext Example')


        self.log_window()


        # self.resize(1280, 800)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def log_window(self):
        widget = QPlainTextEdit(self)
        widget.setReadOnly(True)
        widget.appendPlainText('Simple Test')

        widget.appendHtml(alertHtml + 'Alert Test')
        widget.appendHtml(notifyHtml + 'Notify Test')
        widget.appendHtml(infoHtml + 'Info Test')
        widget.appendHtml(endHtml + 'Endhtml')
        widget.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = my_app()
    sys.exit(app.exec_())

