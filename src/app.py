import sys
import os
from PyQt5.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from monitor import InactivityMonitor

class InactivityApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inactivity Monitor")
        self.setGeometry(100, 100, 300, 200)
        
        self.setup_tray_icon()
        
        self.monitor = InactivityMonitor()
        self.monitor.signals.inactivity_detected.connect(self.show_inactivity_alert)
        
        self.hide()
    
    def setup_tray_icon(self):
        self.tray_icon = QSystemTrayIcon(self)
        
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
        self.tray_icon.setIcon(QIcon(icon_path))
        self.tray_icon.setToolTip("Inactivity Monitor")
        
        tray_menu = QMenu()
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        tray_menu.addAction(exit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
    
    def show_inactivity_alert(self):
        alert = QMessageBox()
        alert.setWindowTitle("Inactivity Alert")
        alert.setText("No activity detected for 1 minute!")
        alert.setIcon(QMessageBox.Warning)
        alert.setWindowFlags(Qt.WindowStaysOnTopHint)
        alert.exec_()
    
    def closeEvent(self, event):
        self.monitor.stop()
        self.tray_icon.hide()
        event.accept() 