import sys
from PyQt5.QtWidgets import QApplication
from app import InactivityApp

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    
    _ = InactivityApp()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 