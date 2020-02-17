import PySide2
from PySide2.QtWidgets import QMainWindow, QAction, QCheckBox, QHBoxLayout, QWidget, QPushButton, QVBoxLayout

from PySide2.QtCharts import QtCharts

import pyqtgraph as plt

class MainWindow(QMainWindow):

    __slots__ = ['menu', 'status']
    def __init__(self):

        QMainWindow.__init__(self)
        self.setWindowTitle("Easy Spectogram")
        self.menu = self.menuBar()

        self.status_bar()
        self.exit_menu()
        self.central()

    def graph(self):

        chart = QtCharts.QChart()

        chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        chart_view = QtCharts.QChartView(chart)

        return chart_view

    def central(self):


        widget = QWidget()

        layout = QHBoxLayout(widget)

        box = self.box()

        layout.addWidget(box)
        #layout.addWidget(self.graph())
        self.setCentralWidget(widget)

    def status_bar(self):
        self.status = self.statusBar()
        self.status.showMessage('placeholder')

    def exit_menu(self):

        self.exit_menu = self.menu.addMenu("Exit")

        exit_action = QAction("Exit without saving", self)
        exit_action.triggered.connect(self.close)
        
        self.exit_menu.addAction(exit_action)

    def box(self):

        widget = QWidget()

        layout = QVBoxLayout(widget)

        layout.addWidget(QPushButton("Butterworth"))
        layout.addWidget(QPushButton("Chebyshev"))
        layout.addWidget(QPushButton("Elliptic"))

        return widget

        
        return widget
