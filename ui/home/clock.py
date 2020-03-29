import PyQt5.QtCore
import PyQt5.QtWidgets

import utils.qtext
import utils.layout


class DigitalClock(utils.qtext.QText):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        timer = PyQt5.QtCore.QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)

        self.show_time()

    # TODO: should probably convert this to datetime
    def show_time(self):
        time = PyQt5.QtCore.QTime.currentTime()
        self.setText(time.toString("hh:mm"))