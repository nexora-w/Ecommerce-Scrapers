from PyQt5.QtCore import pyqtSignal, QObject

class Signals(QObject):
    inactivity_detected = pyqtSignal() 