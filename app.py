import sys
import pyttsx3
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.windowTitle = "Lazy Boy 2000"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.windowTitle)

        self.setFixedHeight(200)
        self.setFixedWidth(200)

        speak = QPushButton(self)
        speak.setText("Speak")
        speak.setGeometry(75, 75, 50, 50)
        speak.clicked.connect(self.speakLoud)

    def speakLoud(self):
        engine = pyttsx3.init()
        engine.say("Yes Sir")
        engine.runAndWait()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())
