import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, QTime, Qt


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0 , 0, 0)  # hours, minutes, seconds, milliseconds
        self.time_label = QLabel("00:00:00.00", self)
        self.timer = QTimer(self)
        self.start = QPushButton("START", self)
        self.stop = QPushButton("STOP", self)
        self.reset = QPushButton("RESET", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("STOPWATCH")
        self.setWindowIcon(QIcon("STOPWATCH.png"))
        self.setStyleSheet("""
            QWidget {
                background-color: #f3f3f3;
            }
            QLabel {
                font-size: 100px;
                color: #333;
                background-color: #e1e1e1;
                border-radius: 20px;
                padding: 30px;
                margin-bottom: 20px;
            }
            QPushButton {
                font-size: 30px;
                color: white;
                background-color: #4CAF50;
                border: 2px solid #4CAF50;
                border-radius: 12px;
                padding: 15px;
                width: 120px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
            QVBoxLayout, QHBoxLayout {
                spacing: 10px;
            }
            QWidget {
                border-radius: 15px;
                padding: 30px;
            }
        """)

        self.start.setObjectName("start_button")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start)
        hbox.addWidget(self.stop)
        hbox.addWidget(self.reset)

        vbox.addLayout(hbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.setLayout(vbox)

        self.start.clicked.connect(self.start_watch)
        self.stop.clicked.connect(self.stop_watch)
        self.reset.clicked.connect(self.reset_watch)
        self.timer.timeout.connect(self.update_display)

    def start_watch(self):
        self.timer.start(10)
        self.start.setText("RESUME")

    def stop_watch(self):
        self.timer.stop()

    def reset_watch(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
        self.start.setText("START")

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)  # we are updating the time with 10 milliseconds
        self.time_label.setText(self.format_time(self.time))


def main():
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
