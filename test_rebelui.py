#!/usr/bin/python
import sys, glob, re, resampling

import PyQt4.Qwt5 as Qwt
from PyQt4 import QtCore, QtGui, Qt
from rebelmaininterface import Ui_MainWindow

class FooBar(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.addDrawingArea()

	def addDrawingArea(self):
		graphTab = self.ui.graphWidgetArea
		graphCanvas = QtGui.QWidget(graphTab)
		print "%s x %s" % (graphTab.geometry().width(), graphTab.geometry().height())
		graphCanvas.setGeometry(10, 10, 530, 470)
		graphCanvas.setMinimumSize(QtCore.QSize(500, 0.5625*500))
		graphCanvas.setStyleSheet("background-color: rgb(255,255,255); border:1px solid rgb(128,128,128);")

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = FooBar()
	myapp.show()
	sys.exit(app.exec_())
