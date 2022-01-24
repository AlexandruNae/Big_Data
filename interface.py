import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
import main
import sys
import random

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
                      "Hola Mundo", "Привет мир"]
        self.text2 = QLabel("No speech yet")
        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.text2)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.speech_to_text)

    def speech_to_text(self):
        path = r'D:\MASTER\IBD\proiect\audio\last_record.wav'
        main.record(5, path)
        text = main.get_large_audio_transcription(path)
        self.text2.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    app.exec()
