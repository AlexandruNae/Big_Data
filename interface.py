import PyQt6
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, \
    QMessageBox
from PyQt6.QtCore import Qt, QTimer
from PyQt6.uic.properties import QtGui
from PyQt6 import QtCore
import main
import datetime
import sys


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.text = QLabel("No speech yet!")
        self.button = QPushButton("Start recording!")

        self.title = QLabel("Speech to text")
        self.title.setStyleSheet("""
                                color: #006325;
                                font-family: Titillium;
                                font-size: 25px;
                                """) #background-color: #262626;
        self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.seconds_text = QLabel("Please enter the number of seconds you "
                                   "want to record!")
        self.seconds_text.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.seconds = QLineEdit(self)
        self.seconds.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #self.timer = QTimer(self)
        #self.timer.setInterval(1000)
        #self.timer.timeout.connect(self.updateCounter)
        #self.timer_label = QLabel('Label')


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.seconds_text)
        self.layout.addWidget(self.seconds)
        #self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.button.clicked.connect(self.speech_to_text)

    def speech_to_text(self):
       path = r'D:\MASTER\IBD\proiect\audio\last_record.wav'
       seconds = self.seconds.text()

       if seconds == "":
           QMessageBox.about(self, "Alert", "You did not enter the number of "
                                        "seconds! ")
           return

       if not seconds.isnumeric():
           QMessageBox.about(self, "Alert", "You did not enter a valid number of seconds! ")
           return

       #self.timer.start()

       main.record(int(seconds), path)
       text = main.get_large_audio_transcription(path)
       if text=="":
           self.text.setText("There is no speech!")
       else:
           self.text.setText("Result: " + text)

       self.seconds.setText("")



    def time(self):
       self.curr_time = self.curr_time.addSecs(1)
       self.timer_label.setText(str(self.curr_time))

    def updateCounter(self):
        deadline = datetime.datetime(2018, 2, 21, 4, 59)
        remaining = deadline - datetime.datetime.utcnow()
        hours = int(remaining.seconds / 3600)
        mins = int((remaining.seconds - hours * 3600) / 60)
        secs = int(remaining.seconds % 60)
        self.timer_label.setText("%d days, %d:%02d:%02d remaining" % (
            remaining.days, hours, mins, secs))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(300,500)
    widget.show()
    app.exec()
