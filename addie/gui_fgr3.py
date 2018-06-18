# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/gui_fgr3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(750, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../d5o/useful_scripts/bg/me2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnLoadSQ = QtGui.QPushButton(self.centralwidget)
        self.btnLoadSQ.setObjectName(_fromUtf8("btnLoadSQ"))
        self.horizontalLayout.addWidget(self.btnLoadSQ)
        self.comboRecipType = QtGui.QComboBox(self.centralwidget)
        self.comboRecipType.setObjectName(_fromUtf8("comboRecipType"))
        self.comboRecipType.addItem(_fromUtf8(""))
        self.comboRecipType.addItem(_fromUtf8(""))
        self.comboRecipType.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboRecipType)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelQmin = QtGui.QLabel(self.centralwidget)
        self.labelQmin.setObjectName(_fromUtf8("labelQmin"))
        self.verticalLayout.addWidget(self.labelQmin)
        self.doubleSpinBoxQmin = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxQmin.setMinimum(0.01)
        self.doubleSpinBoxQmin.setMaximum(10.0)
        self.doubleSpinBoxQmin.setSingleStep(0.01)
        self.doubleSpinBoxQmin.setObjectName(_fromUtf8("doubleSpinBoxQmin"))
        self.verticalLayout.addWidget(self.doubleSpinBoxQmin)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelQmax = QtGui.QLabel(self.centralwidget)
        self.labelQmax.setObjectName(_fromUtf8("labelQmax"))
        self.verticalLayout_2.addWidget(self.labelQmax)
        self.doubleSpinBoxQmax = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxQmax.setMinimum(1.0)
        self.doubleSpinBoxQmax.setMaximum(50.0)
        self.doubleSpinBoxQmax.setSingleStep(0.5)
        self.doubleSpinBoxQmax.setObjectName(_fromUtf8("doubleSpinBoxQmax"))
        self.verticalLayout_2.addWidget(self.doubleSpinBoxQmax)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnGenerateGR = QtGui.QPushButton(self.centralwidget)
        self.btnGenerateGR.setObjectName(_fromUtf8("btnGenerateGR"))
        self.horizontalLayout_2.addWidget(self.btnGenerateGR)
        self.btnSaveGR = QtGui.QPushButton(self.centralwidget)
        self.btnSaveGR.setObjectName(_fromUtf8("btnSaveGR"))
        self.horizontalLayout_2.addWidget(self.btnSaveGR)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelRmin = QtGui.QLabel(self.centralwidget)
        self.labelRmin.setObjectName(_fromUtf8("labelRmin"))
        self.verticalLayout_3.addWidget(self.labelRmin)
        self.doubleSpinBoxRmin = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRmin.setMinimum(0.1)
        self.doubleSpinBoxRmin.setMaximum(4.0)
        self.doubleSpinBoxRmin.setSingleStep(0.1)
        self.doubleSpinBoxRmin.setObjectName(_fromUtf8("doubleSpinBoxRmin"))
        self.verticalLayout_3.addWidget(self.doubleSpinBoxRmin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.labelRmax = QtGui.QLabel(self.centralwidget)
        self.labelRmax.setObjectName(_fromUtf8("labelRmax"))
        self.verticalLayout_4.addWidget(self.labelRmax)
        self.doubleSpinBoxRmax = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRmax.setMinimum(5.0)
        self.doubleSpinBoxRmax.setMaximum(100.0)
        self.doubleSpinBoxRmax.setProperty("value", 20.0)
        self.doubleSpinBoxRmax.setObjectName(_fromUtf8("doubleSpinBoxRmax"))
        self.verticalLayout_4.addWidget(self.doubleSpinBoxRmax)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.labeldelR = QtGui.QLabel(self.centralwidget)
        self.labeldelR.setObjectName(_fromUtf8("labeldelR"))
        self.verticalLayout_5.addWidget(self.labeldelR)
        self.doubleSpinBoxDelR = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxDelR.setMinimum(0.01)
        self.doubleSpinBoxDelR.setMaximum(1.0)
        self.doubleSpinBoxDelR.setSingleStep(0.01)
        self.doubleSpinBoxDelR.setProperty("value", 0.1)
        self.doubleSpinBoxDelR.setObjectName(_fromUtf8("doubleSpinBoxDelR"))
        self.verticalLayout_5.addWidget(self.doubleSpinBoxDelR)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_6.addWidget(self.progressBar)
        self.top_plot = MPLWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_plot.sizePolicy().hasHeightForWidth())
        self.top_plot.setSizePolicy(sizePolicy)
        self.top_plot.setObjectName(_fromUtf8("top_plot"))
        self.verticalLayout_6.addWidget(self.top_plot)
        self.bottom_plot = MPLWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_plot.sizePolicy().hasHeightForWidth())
        self.bottom_plot.setSizePolicy(sizePolicy)
        self.bottom_plot.setObjectName(_fromUtf8("bottom_plot"))
        self.verticalLayout_6.addWidget(self.bottom_plot)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboRecipType.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "FastGR", None))
        self.btnLoadSQ.setText(_translate("MainWindow", "Load SQ", None))
        self.comboRecipType.setItemText(0, _translate("MainWindow", "Plot S(Q)", None))
        self.comboRecipType.setItemText(1, _translate("MainWindow", "Plot S(Q)-1", None))
        self.comboRecipType.setItemText(2, _translate("MainWindow", "Plot Q[S(Q)-1]", None))
        self.labelQmin.setText(_translate("MainWindow", "Qmin", None))
        self.labelQmax.setText(_translate("MainWindow", "Qmax", None))
        self.btnGenerateGR.setText(_translate("MainWindow", "Generate GR", None))
        self.btnSaveGR.setText(_translate("MainWindow", "Save GR", None))
        self.labelRmin.setText(_translate("MainWindow", "Rmin", None))
        self.labelRmax.setText(_translate("MainWindow", "Rmax", None))
        self.labeldelR.setText(_translate("MainWindow", "deltaR", None))

from mplwidget import MPLWidget
import icons_rc
