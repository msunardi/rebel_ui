#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MiniUI.ui'
#
# Created: Wed Sep  9 12:51:13 2009
#	  by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt4 import QtCore
from PyQt4.QtGui import *
from plotter import MyPlot
import PyQt4.Qwt5 as Qwt
from PyQt4.QtCore import Qt


class CentralWidget(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.h_layout = QHBoxLayout()

	def addWidget(self, widget):
		self.h_layout.addWidget(widget)
		self.setLayout(self.h_layout)


class Ui_MainWindow(object):
# class Ui_MainWindow(QMainWindow):
	def setupUi(self, MainWindow):
	# def __init__(self, parent=None):
		# super(Ui_MainWindow, self).__init__(parent)
		# MainWindow = self
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(840, 700)
		
		self.h_layout = QHBoxLayout()
		self.centralwidget = CentralWidget(MainWindow)
		# self.centralwidget = QWidget(MainWindow)
		# self.centralwidget = QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		# self.v_layout = QVBoxLayout(self.centralwidget)
		# self.v_layout.addWidget(self.centralwidget)
		self.exit = QAction(QIcon('/usr/share/icons/Tango/24x24/actions/exit.png'), 'Exit', MainWindow)
		self.exit.setShortcut('Ctrl+Q')
		self.exit.setStatusTip('Exit application')
		self.toolbar = MainWindow.addToolBar('Exit')
		self.toolbar.addAction(self.exit)
		# self.setLayout(self.v_layout)
		# self.centralwidget.setLayout(self.v_layout)
	
		font0 = QFont()
		font0.setBold(True)
		font0.setPointSize(14)
		font1 = QFont()
		font1.setBold(True)
		font1.setPointSize(12)
		font2 = QFont()
		font2.setBold(False)
		font2.setPointSize(10)
		
		self.mainTab = QTabWidget(self.centralwidget)
		self.mainTab.setObjectName("maintab")
		# self.mainTab.setGeometry(QtCore.QRect(3, 0, 650, 550))
		self.mainTab.setTabShape(QTabWidget.Rounded)
		self.mainTab_Chat = QWidget()
		self.mainTab_Chat.setObjectName("maintab_chat")
		# self.mainTab.addTab(self.mainTab_Chat, "")
		self.mainTab_SignalProcessing = QWidget()
		self.mainTab_SignalProcessing.setObjectName("maintab_signalprocessing")
		self.centralwidget.addWidget(self.mainTab)
		
		# 
		# self.hboxLayout = QHBoxLayout(self.mainTab_SignalProcessing)
		# # self.hboxLayout.setMargin(3)
		# self.hboxLayout.addStretch(1)
		# self.hboxLayout.setObjectName("hboxLayout")
		gridLayout = QGridLayout(self.mainTab_SignalProcessing)
		gridLayout.setSpacing(10)


		self.motionTabs = QTabWidget()
		self.motionTabs.setObjectName("motionTabs")

		graphTab = QWidget()
		graphTab.setObjectName("graphTab")
		self.motionTabs.addTab(graphTab, "Graph")
		graphCanvas = QWidget(graphTab)
		graphCanvas.setGeometry(10, 10, 500, 200)
		graphCanvas.setMinimumSize(QtCore.QSize(500, 0.5625*500))
		graphCanvas.setStyleSheet("background-color: rgb(255,255,255); border:1px solid rgb(128,128,128);")

		self.tab = QWidget()
		self.tab.setObjectName("tab")
		
		self.motionPlotWidget = QWidget(self.tab)
		self.motionPlot = MyPlot(self.motionPlotWidget)
		self.motionPlot.setGeometry(QtCore.QRect(10, 0, 570, 230))
		self.motionPlot.setObjectName("motionPlot")
		self.motionTabs.addTab(self.tab, "Motion Plot")
		# self.motionPlot.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum))
		# self.gridLayout.addWidget(self.motionPlot, 0, 0, 1, 1)
		

		# --- Widgets in Motion Signal Processing tab
		# self.gridChannelVisibility = QWidget(self.mainTab_SignalProcessing)
		#self.gridChannelVisibility = QWidget(self.centralwidget)
		# self.gridChannelVisibility.setGeometry(QtCore.QRect(530, 0, 130, 251))
		# self.gridChannelVisibility.setObjectName("gridChannelVisibility")
		# self.hboxLayout = QGridLayout(self.gridChannelVisibility)
		self.channelWidget = QWidget()
		# self.channelGroup = QGroupBox(self.gridChannelVisibility)
		self.channelGroup = QGroupBox(self.channelWidget)
		self.channelGroup.setObjectName("channelGroup")
		self.channelScrollArea = QScrollArea(self.channelGroup)
		self.channelScrollArea.setGeometry(QtCore.QRect(0, 20, 107, 500))
		self.channelScrollArea.setFrameShape(QFrame.WinPanel)
		self.channelScrollArea.setFrameShadow(QFrame.Sunken)
		self.channelScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.channelScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.channelScrollArea.setWidgetResizable(False)
		self.channelScrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.channelScrollArea.setObjectName("channelScrollArea")
		self.scrollAreaWidgetContents = QWidget(self.channelScrollArea)
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 100))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")		
		self.channelScrollArea.setWidget(self.scrollAreaWidgetContents)
		self.scrollAreaWidgetContents.scrollarea = self.channelScrollArea
		self.channelsAffectProcessingCheck = QCheckBox(self.channelGroup)		
		self.channelsAffectProcessingCheck.setText('Affect processing')
		self.channelsAffectProcessingCheck.setAccessibleName('chAffect')
		self.channelsAffectProcessingCheck.setGeometry(QtCore.QRect(0, 220, 110, 30))
		# self.hboxLayout.addWidget(self.motionTabs)
		# self.hboxLayout.addWidget(self.channelGroup)
		gridLayout.addWidget(self.motionTabs, 1, 0)
		gridLayout.addWidget(self.channelGroup, 1, 1, 2, 1)
		
		# self.gridLayoutWidget = QWidget(self.mainTab_SignalProcessing)
		# self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 511, 251))
		# self.gridLayoutWidget.setObjectName("gridLayoutWidget")
		# self.gridLayout = QGridLayout(self.gridLayoutWidget)
		# self.gridLayout.setMargin(3)
		# self.gridLayout.setObjectName("gridLayout")
		# self.tab = QWidget()
		# self.tab.setObjectName("tab")
		
		# self.gridLayoutWidget_4 = QWidget(self.mainTab_SignalProcessing)
		# self.gridLayoutWidget_4.setGeometry(QtCore.QRect(450, 400, 191, 91))
		# self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
		# self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
		# self.gridLayout_5.setMargin(3)
		# self.gridLayout_5.setObjectName("gridLayout_5")
		# self.controlsGroup = QGroupBox(self.gridLayoutWidget_4)
		# self.controlsGroup.setObjectName("controlsGroup")
		
		self.gridLayoutWidget_5 = QWidget(self.mainTab_SignalProcessing)
		#self.gridLayoutWidget_5 = QWidget(self.centralwidget)
		self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 290, 531, 191))
		self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
		
		self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
		# self.gridLayout_6.setMargin(3)
		self.gridLayout_6.setObjectName("gridLayout_6")		
		self.motionToolTabs = QTabWidget(self.gridLayoutWidget_5)
		self.motionToolTabs.setObjectName("motionToolTabs")
		
		self.initToolTabs()

		# vboxLayout = QVBoxLayout()
		# vboxLayout.addStretch(1)
		# vboxLayout.addLayout(self.hboxLayout)
		# self.hboxLayout.addWidget(self.gridLayoutWidget_5)
		gridLayout.addWidget(self.gridLayoutWidget_5, 2, 0)
				
		self.mainTab.addTab(self.mainTab_SignalProcessing, "")
		self.mainTab.setCurrentIndex(0)
		#self.mainTab.adjustSize()
		#self.gridLayout_6.addWidget(self.motionToolTabs, 0, 0, 1, 1)
		
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 22))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		
		self.retranslateUi(MainWindow)
		self.motionToolTabs.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		# self.centralwidget.setLayout(vboxLayout)
		self.centralwidget.setLayout(gridLayout)

		# UNUSED
		# --- Widgets in Chat UI tab
		# # --- Chat UI > Chat section
		# self.chatFrame = QFrame(self.mainTab_Chat)
		# self.chatFrame.setGeometry(QtCore.QRect(5,5,420,480))
		# self.chatFrame.setObjectName("chatframe")
		# self.chatFrame.setFrameShape(QFrame.StyledPanel)
		# self.chatFrame.setFrameShadow(QFrame.Raised)
		
		# self.chatOutputGroup = QGroupBox(self.chatFrame)
		# self.chatOutputGroup.setGeometry(QtCore.QRect(10,10,410,280))
		# self.chatOutputGroup.setObjectName('chatOutputgroup')
		
		# self.chatAreaLabel = QLabel(self.chatOutputGroup)
		# self.chatAreaLabel.setGeometry(QtCore.QRect(0,0,120,25))
		# self.chatAreaLabel.setObjectName("chatarealabel")		
		# self.chatAreaLabel.setFont(font0)
		# self.chatAreaLabel.setText("Chat History")
		
		# self.chatArea = QTextBrowser(self.chatOutputGroup)
		# self.chatArea.setGeometry(QtCore.QRect(0, 30, 400, 250))
		# self.chatArea.setObjectName("chatarea")
		
		# self.chatInputGroup = QGroupBox(self.chatFrame)
		# self.chatInputGroup.setGeometry(QtCore.QRect(10,290,410,100))
		# self.chatInputGroup.setObjectName('chatinputgroup')
		
		# self.chatInputLabel = QLabel(self.chatInputGroup)
		# self.chatInputLabel.setGeometry(QtCore.QRect(0, 10, 200, 25))
		# self.chatInputLabel.setObjectName("chatinputlabel")
		# self.chatInputLabel.setFont(font0)
		# self.chatInputLabel.setText("Your response:")
		# self.chatInput = QLineEdit(self.chatInputGroup)
		# self.chatInput.setGeometry(QtCore.QRect(0, 38, 400, 25))
		# self.chatInput.setObjectName("chatinput")
		# self.chatInput.setFocus()
				
		# self.chatInputEnterButton = QPushButton(self.chatInputGroup)
		# self.chatInputEnterButton.setGeometry(QtCore.QRect(0,68,230,30))
		# self.chatInputEnterButton.setObjectName("chatinputenterbutton")
		# self.chatInputEnterButton.setFont(font1)
		# self.chatInputEnterButton.setText("Enter")
		
		# self.chatInputClearButton = QPushButton(self.chatInputGroup)
		# self.chatInputClearButton.setGeometry(QtCore.QRect(270,68,130,30))
		# self.chatInputClearButton.setObjectName("chatinputclearbutton")
		# self.chatInputClearButton.setFont(font1)
		# self.chatInputClearButton.setText("Clear")
		
		# self.chatContextGroup = QGroupBox(self.chatFrame)
		# self.chatContextGroup.setGeometry(QtCore.QRect(10,395,410,100))
		# self.chatContextGroup.setObjectName('chatcontextgroup')
		
		# self.chatContextLabel = QLabel(self.chatContextGroup)
		# self.chatContextLabel.setGeometry(QtCore.QRect(0,0,100,25))
		# self.chatContextLabel.setObjectName('chatcontextlabel')
		# self.chatContextLabel.setFont(font1)
		# self.chatContextLabel.setText('Chat Context')
		
		# self.chatContextCheckbox = QCheckBox(self.chatContextGroup)
		# self.chatContextCheckbox.setGeometry(QtCore.QRect(120,0,100,25))
		# self.chatContextCheckbox.setObjectName('chatcontextcheckbox')
		# self.chatContextCheckbox.setText('show/hide')
		# self.chatContextCheckbox.setChecked(True)
		
		# self.chatContextGroupin = QGroupBox(self.chatContextGroup)
		# self.chatContextGroupin.setGeometry(QtCore.QRect(0,27,410,100))
		# self.chatContextGroupin.setObjectName('chatcontextgroupin')
		
		# self.chatContextVerbLabel = QLabel(self.chatContextGroupin)
		# self.chatContextVerbLabel.setGeometry(QtCore.QRect(0,0,30,20))
		# self.chatContextVerbLabel.setObjectName('chatcontextverblabel')
		# #self.chatContextVerbLabel.setFont(font2)
		# self.chatContextVerbLabel.setText('Verb:')
		
		# self.chatContextVerb = QLineEdit(self.chatContextGroupin)
		# self.chatContextVerb.setGeometry(QtCore.QRect(30,0,100,20))
		# self.chatContextVerb.setObjectName('chatcontextverb')
		# self.chatContextVerb.setEnabled(False)
		
		# self.chatContextEmoLabel = QLabel(self.chatContextGroupin)
		# self.chatContextEmoLabel.setGeometry(QtCore.QRect(150,0,50,20))
		# self.chatContextEmoLabel.setObjectName('chatcontextemolabel')
		# #self.chatContextEmoLabel.setFont(font2)
		# self.chatContextEmoLabel.setText('Emotive:')
		
		# self.chatContextEmo = QLineEdit(self.chatContextGroupin)
		# self.chatContextEmo.setGeometry(QtCore.QRect(200,0,100,20))
		# self.chatContextEmo.setObjectName('chatcontextemo')
		# self.chatContextEmo.setEnabled(False)
		
		
		# # --- Chat UI > Robot State section
		# self.stateFrame = QFrame(self.mainTab_Chat)
		# self.stateFrame.setGeometry(QtCore.QRect(435,5,204,340))
		# self.stateFrame.setObjectName("stateframe")
		# self.stateFrame.setFrameShape(QFrame.StyledPanel)
		# self.stateFrame.setFrameShadow(QFrame.Raised)
		
		# self.stateLabel = QLabel(self.stateFrame)
		# self.stateLabel.setGeometry(QtCore.QRect(5,5,100,30))
		# self.stateLabel.setObjectName("statelabel")
		# self.stateLabel.setFont(font1)
		# self.stateLabel.setText("Robot State")
		
		# self.stateShowCheckBox = QCheckBox(self.stateFrame)
		# self.stateShowCheckBox.setGeometry(QtCore.QRect(5,30,100,30))
		# self.stateShowCheckBox.setAccessibleName('stateshowcheckbox')
		# self.stateShowCheckBox.setText('show/hide')
		# self.stateShowCheckBox.setChecked(True)
		
		# self.useWillingnessCheckBox = QCheckBox(self.stateFrame)
		# self.useWillingnessCheckBox.setGeometry(QtCore.QRect(95,30,100,30))
		# self.useWillingnessCheckBox.setAccessibleName('usewillingnesscheckbox')
		# self.useWillingnessCheckBox.setText('Use willingness')
		# self.useWillingnessCheckBox.setChecked(True)
		
		# self.stateGroup = QGroupBox(self.stateFrame)
		# self.stateGroup.setGeometry(QtCore.QRect(5,65,195,400))
		# self.stateGroup.setObjectName('stategroup')
				
		# self.robotMoodLabel = QLabel(self.stateGroup)
		# self.robotMoodLabel.setGeometry(QtCore.QRect(0,0,85,25))
		# self.robotMoodLabel.setObjectName('robotmoodlabel')
		# self.robotMoodLabel.setFont(font2)
		# self.robotMoodLabel.setText("Robot mood:")
		# self.robotMood = QLineEdit(self.stateGroup)
		# self.robotMood.setGeometry(QtCore.QRect(95,0,100,25))
		# self.robotMood.setEnabled(False)
		
		# self.robotActionLabel = QLabel(self.stateGroup)
		# self.robotActionLabel.setGeometry(QtCore.QRect(0,30,85,25))
		# self.robotActionLabel.setObjectName('robotactionlabel')
		# self.robotActionLabel.setFont(font2)
		# self.robotActionLabel.setText("Robot action:")
		# self.robotAction = QLineEdit(self.stateGroup)
		# self.robotAction.setGeometry(QtCore.QRect(95,30,100,25))
		# self.robotAction.setEnabled(False)
		
		# self.happyLevelLabel = QLabel(self.stateGroup)
		# self.happyLevelLabel.setGeometry(QtCore.QRect(0,80,85,25))
		# self.happyLevelLabel.setObjectName('happylevellabel')
		# self.happyLevelLabel.setFont(font2)
		# self.happyLevelLabel.setText("Happy level:")
		# #self.happyLevel = QLineEdit(self.stateGroup)
		# self.happyLevel = Qwt.QwtThermo(self.stateGroup)
		# self.happyLevel.setOrientation(Qt.Horizontal, Qwt.QwtThermo.TopScale)
		# self.happyLevel.setGeometry(QtCore.QRect(95,60,100,45))
		# self.happyLevel.setEnabled(False)
		
		# self.fearLevelLabel = QLabel(self.stateGroup)
		# self.fearLevelLabel.setGeometry(QtCore.QRect(0,110,85,25))
		# self.fearLevelLabel.setObjectName('fearlevellabel')
		# self.fearLevelLabel.setFont(font2)
		# self.fearLevelLabel.setText("Fear level:")
		# #self.fearLevel = QLineEdit(self.stateGroup)
		# self.fearLevel = Qwt.QwtThermo(self.stateGroup)
		# self.fearLevel.setOrientation(Qt.Horizontal, Qwt.QwtThermo.TopScale)
		# self.fearLevel.setGeometry(QtCore.QRect(95,110,100,25))
		# self.fearLevel.setEnabled(False)
		
		# self.sadnessLevelLabel = QLabel(self.stateGroup)
		# self.sadnessLevelLabel.setGeometry(QtCore.QRect(0,140,85,25))
		# self.sadnessLevelLabel.setObjectName('sadnesslevellabel')
		# self.sadnessLevelLabel.setFont(font2)
		# self.sadnessLevelLabel.setText("Sadness level:")
		# #self.sadnessLevel = QLineEdit(self.stateGroup)
		# self.sadnessLevel = Qwt.QwtThermo(self.stateGroup)
		# self.sadnessLevel.setOrientation(Qt.Horizontal, Qwt.QwtThermo.TopScale)
		# self.sadnessLevel.setGeometry(QtCore.QRect(95,140,100,25))
		# self.sadnessLevel.setEnabled(False)
		
		# self.angerLevelLabel = QLabel(self.stateGroup)
		# self.angerLevelLabel.setGeometry(QtCore.QRect(0,170,85,25))
		# self.angerLevelLabel.setObjectName('angerlevellabel')
		# self.angerLevelLabel.setFont(font2)
		# self.angerLevelLabel.setText("Anger level:")
		# #self.angerLevel = QLineEdit(self.stateGroup)
		# self.angerLevel = Qwt.QwtThermo(self.stateGroup)
		# self.angerLevel.setOrientation(Qt.Horizontal, Qwt.QwtThermo.TopScale)
		# self.angerLevel.setGeometry(QtCore.QRect(95,170,100,25))
		# self.angerLevel.setEnabled(False)
		
		# self.willingnessLabel = QLabel(self.stateGroup)
		# self.willingnessLabel.setGeometry(QtCore.QRect(0,200,85,25))
		# self.willingnessLabel.setObjectName('willingnesslabel')
		# self.willingnessLabel.setFont(font2)
		# self.willingnessLabel.setText("Willingness:")
		# #self.willingness = QLineEdit(self.stateGroup)
		# self.willingness = Qwt.QwtThermo(self.stateGroup)
		# self.willingness.setOrientation(Qt.Horizontal, Qwt.QwtThermo.TopScale)
		# self.willingness.setGeometry(QtCore.QRect(95,200,100,25))
		# self.willingness.setEnabled(False)
		
		# self.usernameLabel = QLabel(self.stateGroup)
		# self.usernameLabel.setGeometry(QtCore.QRect(0,230,85,25))
		# self.usernameLabel.setObjectName('usernamelabel')
		# self.usernameLabel.setFont(font2)
		# self.usernameLabel.setText("User's name:")
		# self.username = QLineEdit(self.stateGroup)
		# self.username.setGeometry(QtCore.QRect(95,230,100,25))
		# self.username.setEnabled(False)
		
		# # --- Chat UI > Vision section
		# self.visionFrame = QFrame(self.mainTab_Chat)
		# self.visionFrame.setGeometry(QtCore.QRect(435,353,204,132))
		# self.visionFrame.setObjectName("visionframe")
		# self.visionFrame.setFrameShape(QFrame.StyledPanel)
		# self.visionFrame.setFrameShadow(QFrame.Raised)
		
		# self.visionLabel = QLabel(self.visionFrame)
		# self.visionLabel.setGeometry(QtCore.QRect(5,5,100,30))
		# self.visionLabel.setObjectName("visionlabel")
		# self.visionLabel.setFont(font1)
		# self.visionLabel.setText("Robot Vision")				
		
		# self.visionGroup = QGroupBox(self.visionFrame)
		# self.visionGroup.setGeometry(QtCore.QRect(5,35,195,400))
		# self.visionGroup.setObjectName('visiongroup')
		
		# self.visionAutoRadioButton = QRadioButton(self.visionGroup)
		# self.visionAutoRadioButton.setGeometry(QtCore.QRect(0,0,125,30))
		# self.visionAutoRadioButton.setAccessibleName('visionautoradiobutton')
		# self.visionAutoRadioButton.setFont(font2)
		# self.visionAutoRadioButton.setText('Auto mode')
		# self.visionAutoRadioButton.setChecked(True)
		
		# self.visionRecognizeRadioButton = QRadioButton(self.visionGroup)
		# self.visionRecognizeRadioButton.setGeometry(QtCore.QRect(0,30,125,30))
		# self.visionRecognizeRadioButton.setAccessibleName('visionrecognizeradiobutton')
		# self.visionRecognizeRadioButton.setFont(font2)
		# self.visionRecognizeRadioButton.setText('Recognize mode')
		
		# self.visionLearnRadioButton = QRadioButton(self.visionGroup)
		# self.visionLearnRadioButton.setGeometry(QtCore.QRect(0,60,125,30))
		# self.visionLearnRadioButton.setAccessibleName('visionlearnradiobutton')
		# self.visionLearnRadioButton.setFont(font2)
		# self.visionLearnRadioButton.setText('Learn new face')
		

	# Populating the list of channel/servo checkboxes  in the channelScrollArea
	def populateChannelList(self, numOfChannels=24, robot='KHR1'):
		self.channels = {}		# Store the checkboxes
		chDimX = 100
		chDimY = 25
		
		if robot == 'KHR1':
			numOfChannels = 24
			for i in range(numOfChannels):
				self.channels[str(i)] = QCheckBox(self.scrollAreaWidgetContents)
				#self.channels.append(QCheckBox)
				#self.channels[i] = QCheckBox(self.scrollAreaWidgetContents)
				self.channels[str(i)].setText('ch'+str(i))
				self.channels[str(i)].setAccessibleName(str(i))
				self.channels[str(i)].setGeometry(QtCore.QRect(3, i*30, chDimX, chDimY))
			
				if i in [3,4,9,10,11,17,23]:
					self.channels[str(i)].setEnabled(False)		# Disable the unused channels/servos
				else:
					self.channels[str(i)].setEnabled(True)		# Enable all the used channels/servos
					self.channels[str(i)].setChecked(True)		# visible=True by default for all used channels/servos
		
		self.scrollAreaWidgetContents.adjustSize()	# Allow the scrollarea widget to automatically adjust its size to fit the contents
		#print self.channels
	
	def populateKhr1MotionBox(self):
		self.khr1MotionComboBox.addItems([str(i) for i in range(40)])
	
	def populateMotionBox(self, motionList, defaultIndex=None):
		self.motionComboBox.addItems(motionList)
		if defaultIndex is None:
			self.motionComboBox.setCurrentIndex(1)
		   #self.ui.comboBoxMotionSignal.setCurrentIndex(4)
		else:
			self.motionComboBox.setCurrentIndex(defaultIndex)
			
	def addGainSliders(self, how_many):		
		#self.initToolTabs()	# <<< this is done in case we are re-loading a new motion
		self.gainLabels = [x for x in range(how_many)]
		self.gainSliders = []
		self.gainLineEdits = []
		
		self.mrfScrollArea = QScrollArea(self.mrfFrame)
		self.mrfScrollArea.setGeometry(QtCore.QRect(100, 3, 300, 133))
		# self.mrfScrollArea.setFrameShape(QFrame.WinPanel)
		# self.mrfScrollArea.setFrameShadow(QFrame.Sunken)
		self.mrfScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.mrfScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.mrfScrollArea.setWidgetResizable(False)
		self.mrfScrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.mrfScrollArea.setObjectName("mrfScrollArea")
		self.mrfScrollAreaWidgetContents = QWidget(self.mrfScrollArea)
		self.mrfScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 123))
		self.mrfScrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")		
		self.mrfScrollArea.setWidget(self.mrfScrollAreaWidgetContents)
		
		for i in range(how_many):
			
			#=== Create labels for each gain
			self.gainLabels.append(QLabel)
			self.gainLabels[i] = QLabel(self.mrfScrollAreaWidgetContents)
			self.gainLabels[i].setGeometry(QtCore.QRect(i*60, 0, 54, 18))
			self.gainLabels[i].setAlignment(QtCore.Qt.AlignCenter)
			self.gainLabels[i].setObjectName("band"+str(i))
			self.gainLabels[i].setText("Band "+str(i))			

			#=== Create sliders for each gain
			self.gainSliders.append(QSlider(self.mrfScrollAreaWidgetContents))
			self.gainSliders[i].setGeometry(QtCore.QRect(20 + i*60 , 40, 20, 70))
			self.gainSliders[i].setAccessibleName(str(i))
			self.gainSliders[i].setMaximum(50)
			self.gainSliders[i].setMinimum(-50)
			self.gainSliders[i].setSliderPosition(10)

			#=== Create Line Edit objects for each gain
			self.gainLineEdits.append(QLineEdit)
			self.gainLineEdits[i] = QLineEdit(self.mrfScrollAreaWidgetContents)
			self.gainLineEdits[i].setGeometry(QtCore.QRect(10 + i*60, 20, 41, 20))
			self.gainLineEdits[i].setObjectName("gainLineEdit")
			self.gainLineEdits[i].setText(str(self.gainSliders[i].value()*0.1))
			self.gainLineEdits[i].setAccessibleName(str(i))
		
		self.mrfScrollAreaWidgetContents.adjustSize()
	
	def initToolTabs(self):
		print "initToolTabs()"
		self.motionToolTabs.clear()
		#self.motionToolTabs = QTabWidget(self.gridLayoutWidget_5)
		#self.motionToolTabs.setObjectName("motionToolTabs")
		#self.tab_3 = QWidget()
		#self.tab_3.setObjectName("tab_3")
		#self.motionToolTabs.addTab(self.tab_3, "")
		self.tabInterp = QWidget()
		self.tabInterp.setObjectName("tabInterp")
				
		self.interpFrame = QFrame(self.tabInterp)
		self.interpFrame.setGeometry(QtCore.QRect(5, 5, 410, 140))
		# self.interpFrame.setFrameShape(QFrame.StyledPanel)
		# self.interpFrame.setFrameShadow(QFrame.Plain)
		# self.interpFrame.setLineWidth(3)
		self.interpFrame.setObjectName("interpFrame")
		self.interpTensionLabel = QLabel(self.interpFrame)
		self.interpTensionLabel.setGeometry(QtCore.QRect(20, 10, 80, 25))
		self.interpTensionLabel.setText("Tension")
		self.interpTensionSpinBox = QSpinBox(self.interpFrame)
		self.interpTensionSpinBox.setGeometry(QtCore.QRect(100, 10, 50, 25))
		self.interpTensionSpinBox.setMinimum(-50)
		self.interpTensionSpinBox.setMaximum(50)
		self.interpTensionSpinBox.setAccessibleName("tension")
		self.interpBiasLabel = QLabel(self.interpFrame)
		self.interpBiasLabel.setGeometry(QtCore.QRect(20, 40, 80, 25))
		self.interpBiasLabel.setText("Bias")
		self.interpBiasSpinBox = QSpinBox(self.interpFrame)
		self.interpBiasSpinBox.setGeometry(QtCore.QRect(100, 40, 50, 25))
		self.interpBiasSpinBox.setMinimum(-50)
		self.interpBiasSpinBox.setMaximum(50)
		self.interpBiasSpinBox.setAccessibleName("bias")
		self.interpContinuityLabel = QLabel(self.interpFrame)
		self.interpContinuityLabel.setGeometry(QtCore.QRect(20, 70, 80, 25))
		self.interpContinuityLabel.setText("Continuity")
		self.interpContinuitySpinBox = QSpinBox(self.interpFrame)
		self.interpContinuitySpinBox.setGeometry(QtCore.QRect(100, 70, 50, 25))
		self.interpContinuitySpinBox.setMinimum(-50)
		self.interpContinuitySpinBox.setMaximum(50)
		self.interpContinuitySpinBox.setAccessibleName("continuity")
		self.interpButton = QPushButton(self.interpFrame)
		self.interpButton.setGeometry(QtCore.QRect(10, 105, 130, 25))
		self.interpButton.setText("Interpolate!")
		self.interpButton.setStatusTip('Interpolate raw (from file) motion data')
		
		self.motionToolTabs.addTab(self.tabInterp, "Interpolation")
		
		self.tabResample = QWidget()
		self.tabResample.setObjectName("tabResample")
		self.motionToolTabs.addTab(self.tabResample, "")
		self.resampFrame = QFrame(self.tabResample)
		self.resampFrame.setGeometry(QtCore.QRect(5, 5, 410, 140))
		# self.resampFrame.setFrameShape(QFrame.StyledPanel)
		# self.resampFrame.setFrameShadow(QFrame.Plain)
		# self.resampFrame.setLineWidth(3)
		self.resampFrame.setObjectName("resampFrame")
		self.resampRateLabel = QLabel(self.resampFrame)
		self.resampRateLabel.setGeometry(QtCore.QRect(20, 10, 80, 25))
		self.resampRateLabel.setText("Sampling rate")
		self.resampRateSpinBox = QSpinBox(self.resampFrame)
		self.resampRateSpinBox.setGeometry(QtCore.QRect(100, 10, 50, 25))
		self.resampRateSpinBox.setMinimum(1)
		self.resampRateSpinBox.setMaximum(8)
		self.resampRateSpinBox.setAccessibleName("rate")		
		self.resampButton = QPushButton(self.resampFrame)
		self.resampButton.setGeometry(QtCore.QRect(10, 105, 130, 25))
		self.resampButton.setText("Resample!")
		self.resampButton.setStatusTip('Resample interpolated motion data')
		self.motionToolTabs.addTab(self.tabResample, "Resample")
		
		self.tabMrf = QWidget()
		self.tabMrf.setObjectName("tabMrf")
		self.motionToolTabs.addTab(self.tabMrf, "")
		self.mrfFrame = QFrame(self.tabMrf)
		self.mrfFrame.setGeometry(QtCore.QRect(5, 5, 410, 140))
		# self.mrfFrame.setFrameShape(QFrame.StyledPanel)
		# self.mrfFrame.setFrameShadow(QFrame.Plain)
		# self.mrfFrame.setLineWidth(3)
		self.mrfFrame.setObjectName("mrfFrame")		
		self.mrfButton = QPushButton(self.mrfFrame)
		self.mrfButton.setGeometry(QtCore.QRect(10, 105, 80, 25))
		self.mrfButton.setText("MultiresFiltering!")
		self.mrfButton.setStatusTip('Apply multiresolution filtering')
		self.motionToolTabs.addTab(self.tabMrf, "Mrf")		
		
		self.gridLayout_6.addWidget(self.motionToolTabs, 0, 0, 1, 1)
		print "Done!"
	
	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QApplication.translate("MainWindow", "Something-something UI", None, QApplication.UnicodeUTF8))
		self.channelGroup.setTitle(QApplication.translate("MainWindow", "Channel visibility:", None, QApplication.UnicodeUTF8))
		# self.motionFileGroup.setTitle(QApplication.translate("MainWindow", "Motion File:", None, QApplication.UnicodeUTF8))
		# self.motionLoadButton.setText(QApplication.translate("MainWindow", "Load Motion", None, QApplication.UnicodeUTF8))
		# self.motionTabs.setTabText(self.motionTabs.indexOf(self.tab), QApplication.translate("MainWindow", "Tab 1", None, QApplication.UnicodeUTF8))
		#self.motionTabs.setTabText(self.motionTabs.indexOf(self.tab_2), QApplication.translate("MainWindow", "Tab 2", None, QApplication.UnicodeUTF8))
		# self.khr1MotionGroup.setTitle(QApplication.translate("MainWindow", "KHR-1 Motion Control:", None, QApplication.UnicodeUTF8))
		# self.controlsGroup.setTitle(QApplication.translate("MainWindow", "Motion Controls:", None, QApplication.UnicodeUTF8))
		# self.khr1MotionRunButton.setText(QApplication.translate("MainWindow", "Run", None, QApplication.UnicodeUTF8))
		# self.motionPlayButton.setText(QApplication.translate("MainWindow", "...", None, QApplication.UnicodeUTF8))
		# self.motionResetButton.setText(QApplication.translate("MainWindow", "Reset Data", None, QApplication.UnicodeUTF8))
		# self.motionStopButton.setText(QApplication.translate("MainWindow", "...", None, QApplication.UnicodeUTF8))
		# self.motionRewButton.setText(QApplication.translate("MainWindow", "...", None, QApplication.UnicodeUTF8))
		# self.motionFwdButton.setText(QApplication.translate("MainWindow", "...", None, QApplication.UnicodeUTF8))
		#self.motionToolTabs.setTabText(self.motionToolTabs.indexOf(self.tab_3), QApplication.translate("MainWindow", "Tab 1", None, QApplication.UnicodeUTF8))
		self.motionToolTabs.setTabText(self.motionToolTabs.indexOf(self.tabInterp), QApplication.translate("MainWindow", "Interpolation", None, QApplication.UnicodeUTF8))
		self.motionToolTabs.setTabText(self.motionToolTabs.indexOf(self.tabResample), QApplication.translate("MainWindow", ")Re(Sample", None, QApplication.UnicodeUTF8))
		self.mainTab.setTabText(self.mainTab.indexOf(self.mainTab_Chat), QApplication.translate("MainWindow", "Chat UI", None, QApplication.UnicodeUTF8))
		self.mainTab.setTabText(self.mainTab.indexOf(self.mainTab_SignalProcessing), QApplication.translate("MainWindow", "Motion Signal Processing", None, QApplication.UnicodeUTF8))

from PyQt4.Qwt5 import QwtPlot

# def main():
	
# 	app = QApplication(sys.argv)
# 	ex = Ui_MainWindow()
# 	ex.show()
# 	# q = QMainWindow()
# 	# ex.setupUi(q)
# 	# ex.populateChannelList()
# 	# q.show()
# 	sys.exit(app.exec_())


# if __name__ == '__main__':
# 	main()