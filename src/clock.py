import sys
import os
import requests
import tempfile
import urllib.request
import shutil
import zipfile
import traceback
import subprocess

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, Qt, QRunnable, QThread, QThreadPool
from PyQt6 import QtGui
from pathlib import Path

class UI(QObject):
    majorVersion = 1
    minorVersion = 0
    build = 12
    version = {}

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)    
    # Instatitate objects
    ui = UI()
    
    engine = QQmlApplicationEngine()
    # Bind objects to the QML
    engine.rootContext().setContextProperty("ui",ui)
    engine.quit.connect(app.quit)    
    path = os.path.dirname(os.path.abspath(__file__))
    qml = os.path.join(path,'qml','main.qml')
    
    icon = os.path.join(path, 'icon', 'org.kde.plasma.analogclock.ico')
    app.setWindowIcon(QtGui.QIcon(icon))
    
    engine.load(qml)
    sys.exit(app.exec())