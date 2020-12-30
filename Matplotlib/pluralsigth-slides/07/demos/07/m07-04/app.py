import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QComboBox
from PyQt5.QtCore import QSize, QRect 

import numpy as np

from matplotlib.figure import Figure 
from matplotlib.backends.qt_compat import QtCore, QtWidgets, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar

import helper

class MPLDemoWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(800, 600))    
        self.setWindowTitle("Matplotlib Demo") 

        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)

        layout = QtWidgets.QVBoxLayout(centralWidget)
        layout.setGeometry(QRect(80, 20, 640, 480))

        self.canvas = FigureCanvas(Figure(figsize=(6, 4)))
        layout.addWidget(self.canvas)

        self.ax = self.canvas.figure.subplots()
        year = 2013
        heights = [month[1] for month in helper.precip_sums_for_year(year)]
        self.ax.bar(np.arange(len(heights)), heights)
        self.ax.set_xticks(np.arange(len(helper.MONTHS)))
        self.ax.set_xticklabels(helper.MONTHS)

        self.yearsBox = QComboBox(centralWidget)
        self.yearsBox.setGeometry(QRect(40, 560, 720, 31))
        self.yearsBox.setObjectName(("yearsBox"))
        self.yearsBox.addItem("2013")
        self.yearsBox.addItem("2014")
        self.yearsBox.addItem("2015")
        self.yearsBox.addItem("2016")
        self.yearsBox.addItem("2017")
        self.yearsBox.addItem("2018")


        self.yearsBox.currentIndexChanged.connect(self.show_precip_for_year)

    def show_precip_for_year(self, i):
        year = 2013 + i
        heights = [month[1] for month in helper.precip_sums_for_year(year)]
        self.ax.clear()
        self.ax.bar(np.arange(len(heights)), heights)
        self.ax.set_xticks(np.arange(len(helper.MONTHS)))
        self.ax.set_xticklabels(helper.MONTHS)
        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MPLDemoWindow()
    mainWin.show()
    sys.exit( app.exec_() )