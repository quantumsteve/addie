# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/step1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_8.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.diamond_background = QtWidgets.QLineEdit(self.groupBox_5)
        self.diamond_background.setToolTip("")
        self.diamond_background.setStatusTip("")
        self.diamond_background.setAccessibleDescription("")
        self.diamond_background.setInputMask("")
        self.diamond_background.setPlaceholderText("")
        self.diamond_background.setObjectName("diamond_background")
        self.gridLayout.addWidget(self.diamond_background, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sample_background = QtWidgets.QLineEdit(self.groupBox_5)
        self.sample_background.setToolTip("")
        self.sample_background.setStatusTip("")
        self.sample_background.setAccessibleDescription("")
        self.sample_background.setInputMask("")
        self.sample_background.setPlaceholderText("")
        self.sample_background.setObjectName("sample_background")
        self.gridLayout.addWidget(self.sample_background, 4, 1, 1, 1)
        self.vanadium = QtWidgets.QLineEdit(self.groupBox_5)
        self.vanadium.setToolTip("")
        self.vanadium.setStatusTip("")
        self.vanadium.setAccessibleDescription("")
        self.vanadium.setInputMask("")
        self.vanadium.setPlaceholderText("")
        self.vanadium.setObjectName("vanadium")
        self.gridLayout.addWidget(self.vanadium, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.vanadium_background = QtWidgets.QLineEdit(self.groupBox_5)
        self.vanadium_background.setToolTip("")
        self.vanadium_background.setStatusTip("")
        self.vanadium_background.setAccessibleDescription("")
        self.vanadium_background.setInputMask("")
        self.vanadium_background.setPlaceholderText("")
        self.vanadium_background.setObjectName("vanadium_background")
        self.gridLayout.addWidget(self.vanadium_background, 3, 1, 1, 1)
        self.diamond = QtWidgets.QLineEdit(self.groupBox_5)
        self.diamond.setToolTip("")
        self.diamond.setStatusTip("")
        self.diamond.setAccessibleDescription("")
        self.diamond.setInputMask("")
        self.diamond.setPlaceholderText("")
        self.diamond.setObjectName("diamond")
        self.gridLayout.addWidget(self.diamond, 0, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_21.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_5.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_5.addWidget(self.label_22)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)
        self.last_scan = QtWidgets.QLineEdit(self.centralwidget)
        self.last_scan.setObjectName("last_scan")
        self.gridLayout_3.addWidget(self.last_scan, 1, 1, 1, 1)
        self.first_scan = QtWidgets.QLineEdit(self.centralwidget)
        self.first_scan.setObjectName("first_scan")
        self.gridLayout_3.addWidget(self.first_scan, 0, 1, 1, 1)
        self.frequency = QtWidgets.QComboBox(self.centralwidget)
        self.frequency.setObjectName("frequency")
        self.frequency.addItem("")
        self.frequency.addItem("")
        self.gridLayout_3.addWidget(self.frequency, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(120, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.recalibration_yes = QtWidgets.QRadioButton(self.groupBox_2)
        self.recalibration_yes.setObjectName("recalibration_yes")
        self.horizontalLayout.addWidget(self.recalibration_yes)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(120, 0))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.renormalization_yes = QtWidgets.QRadioButton(self.groupBox_3)
        self.renormalization_yes.setObjectName("renormalization_yes")
        self.horizontalLayout_2.addWidget(self.renormalization_yes)
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_10.setChecked(True)
        self.radioButton_10.setObjectName("radioButton_10")
        self.horizontalLayout_2.addWidget(self.radioButton_10)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(120, 0))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.autotemplate_yes = QtWidgets.QRadioButton(self.groupBox_4)
        self.autotemplate_yes.setChecked(True)
        self.autotemplate_yes.setObjectName("autotemplate_yes")
        self.horizontalLayout_3.addWidget(self.autotemplate_yes)
        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_12.setChecked(False)
        self.radioButton_12.setObjectName("radioButton_12")
        self.horizontalLayout_3.addWidget(self.radioButton_12)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.comments = QtWidgets.QLineEdit(self.centralwidget)
        self.comments.setObjectName("comments")
        self.horizontalLayout_10.addWidget(self.comments)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.auto_manual_folder = QtWidgets.QRadioButton(self.groupBox)
        self.auto_manual_folder.setChecked(True)
        self.auto_manual_folder.setObjectName("auto_manual_folder")
        self.verticalLayout_4.addWidget(self.auto_manual_folder)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.manual_output_folder = QtWidgets.QRadioButton(self.groupBox)
        self.manual_output_folder.setObjectName("manual_output_folder")
        self.horizontalLayout_8.addWidget(self.manual_output_folder)
        self.manual_output_folder_field = QtWidgets.QLineEdit(self.groupBox)
        self.manual_output_folder_field.setEnabled(False)
        self.manual_output_folder_field.setObjectName("manual_output_folder_field")
        self.horizontalLayout_8.addWidget(self.manual_output_folder_field)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.run_autonom_script = QtWidgets.QPushButton(self.centralwidget)
        self.run_autonom_script.setEnabled(False)
        self.run_autonom_script.setObjectName("run_autonom_script")
        self.verticalLayout_3.addWidget(self.run_autonom_script)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.diamond.editingFinished.connect(MainWindow.diamond_edited)
        self.diamond_background.editingFinished.connect(MainWindow.diamond_background_edited)
        self.vanadium.editingFinished.connect(MainWindow.vanadium_edited)
        self.vanadium_background.editingFinished.connect(MainWindow.vanadium_background_edited)
        self.sample_background.editingFinished.connect(MainWindow.sample_background_edited)
        self.auto_manual_folder.clicked.connect(MainWindow.output_folder_radio_buttons)
        self.manual_output_folder.clicked.connect(MainWindow.output_folder_radio_buttons)
        self.manual_output_folder_field.editingFinished.connect(MainWindow.manual_output_folder_field_edited)
        self.run_autonom_script.clicked.connect(MainWindow.run_autonom)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.diamond, self.diamond_background)
        MainWindow.setTabOrder(self.diamond_background, self.vanadium)
        MainWindow.setTabOrder(self.vanadium, self.vanadium_background)
        MainWindow.setTabOrder(self.vanadium_background, self.sample_background)
        MainWindow.setTabOrder(self.sample_background, self.first_scan)
        MainWindow.setTabOrder(self.first_scan, self.last_scan)
        MainWindow.setTabOrder(self.last_scan, self.frequency)
        MainWindow.setTabOrder(self.frequency, self.recalibration_yes)
        MainWindow.setTabOrder(self.recalibration_yes, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.renormalization_yes)
        MainWindow.setTabOrder(self.renormalization_yes, self.radioButton_10)
        MainWindow.setTabOrder(self.radioButton_10, self.autotemplate_yes)
        MainWindow.setTabOrder(self.autotemplate_yes, self.radioButton_12)
        MainWindow.setTabOrder(self.radioButton_12, self.run_autonom_script)
        MainWindow.setTabOrder(self.run_autonom_script, self.auto_manual_folder)
        MainWindow.setTabOrder(self.auto_manual_folder, self.manual_output_folder)
        MainWindow.setTabOrder(self.manual_output_folder, self.manual_output_folder_field)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Scan Numbers  (ex: 1234, 1300-1305, 1310)"))
        self.label_8.setText(_translate("MainWindow", "*"))
        self.label_7.setText(_translate("MainWindow", "Vanadium background"))
        self.diamond_background.setText(_translate("MainWindow", "65456"))
        self.label.setText(_translate("MainWindow", "Diamond"))
        self.sample_background.setText(_translate("MainWindow", "65472"))
        self.vanadium.setText(_translate("MainWindow", "65458"))
        self.label_5.setText(_translate("MainWindow", "Vanadium"))
        self.label_4.setText(_translate("MainWindow", "*"))
        self.label_2.setText(_translate("MainWindow", "*"))
        self.label_6.setText(_translate("MainWindow", "*"))
        self.label_10.setText(_translate("MainWindow", "*"))
        self.label_3.setText(_translate("MainWindow", "Diamond background"))
        self.label_9.setText(_translate("MainWindow", "Sample background"))
        self.vanadium_background.setText(_translate("MainWindow", "65470"))
        self.diamond.setText(_translate("MainWindow", "65454"))
        self.label_21.setText(_translate("MainWindow", "*"))
        self.label_22.setText(_translate("MainWindow", ": Mandatory field"))
        self.label_18.setText(_translate("MainWindow", "First scan to be analyzed"))
        self.label_20.setText(_translate("MainWindow", "Frequency (Hz)"))
        self.label_19.setText(_translate("MainWindow", "Last scan to be analyzed"))
        self.last_scan.setText(_translate("MainWindow", "65452"))
        self.first_scan.setText(_translate("MainWindow", "65450"))
        self.frequency.setItemText(0, _translate("MainWindow", "60"))
        self.frequency.setItemText(1, _translate("MainWindow", "30"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Recalibration"))
        self.recalibration_yes.setText(_translate("MainWindow", "Yes"))
        self.radioButton_2.setText(_translate("MainWindow", "No"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Renormalization"))
        self.renormalization_yes.setText(_translate("MainWindow", "Yes"))
        self.radioButton_10.setText(_translate("MainWindow", "No"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Autotemplate"))
        self.autotemplate_yes.setText(_translate("MainWindow", "Yes"))
        self.radioButton_12.setText(_translate("MainWindow", "No"))
        self.label_12.setText(_translate("MainWindow", "Comments:"))
        self.groupBox.setTitle(_translate("MainWindow", "Name of Output Folder"))
        self.auto_manual_folder.setText(_translate("MainWindow", "Automatic (autoNOM_##)"))
        self.manual_output_folder.setText(_translate("MainWindow", "Manual"))
        self.run_autonom_script.setText(_translate("MainWindow", "Run autoNOM script"))

