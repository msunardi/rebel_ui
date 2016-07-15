# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rebel.ui'
#
# Created: Fri Jul 15 13:20:03 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(801, 649)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 801, 491))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.graphWidgetArea = QtGui.QWidget(self.verticalLayoutWidget)
        self.graphWidgetArea.setEnabled(True)
        self.graphWidgetArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphWidgetArea.setObjectName(_fromUtf8("graphWidgetArea"))
        self.horizontalLayout_2.addWidget(self.graphWidgetArea)
        self.widget_4 = QtGui.QWidget(self.verticalLayoutWidget)
        self.widget_4.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.widget_4)
        self.groupBox_2.setGeometry(QtCore.QRect(9, -1, 241, 481))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 231, 461))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget_5 = QtGui.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(0, 499, 801, 91))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.groupBox = QtGui.QGroupBox(self.widget_5)
        self.groupBox.setGeometry(QtCore.QRect(10, 9, 781, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 30, 621, 41))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(640, 30, 131, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.centralwidget.setLayout(self.verticalLayout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox", None))
        self.groupBox.setTitle(_translate("MainWindow", "Expression", None))
        self.pushButton.setText(_translate("MainWindow", "Evaluate", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

