# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/ui_import_from_database.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(856, 756)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.toolBox = QtGui.QToolBox(Dialog)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 838, 639))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout = QtGui.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ipts_radio_button = QtGui.QRadioButton(self.page)
        self.ipts_radio_button.setChecked(True)
        self.ipts_radio_button.setObjectName(_fromUtf8("ipts_radio_button"))
        self.horizontalLayout_2.addWidget(self.ipts_radio_button)
        self.ipts_combobox = QtGui.QComboBox(self.page)
        self.ipts_combobox.setMinimumSize(QtCore.QSize(150, 0))
        self.ipts_combobox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.ipts_combobox.setObjectName(_fromUtf8("ipts_combobox"))
        self.horizontalLayout_2.addWidget(self.ipts_combobox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ipts_label = QtGui.QLabel(self.page)
        self.ipts_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ipts_label.setObjectName(_fromUtf8("ipts_label"))
        self.horizontalLayout_2.addWidget(self.ipts_label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.error_message = QtGui.QLabel(self.page)
        self.error_message.setAlignment(QtCore.Qt.AlignCenter)
        self.error_message.setObjectName(_fromUtf8("error_message"))
        self.horizontalLayout_2.addWidget(self.error_message)
        self.label_3 = QtGui.QLabel(self.page)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.ipts_lineedit = QtGui.QLineEdit(self.page)
        self.ipts_lineedit.setMinimumSize(QtCore.QSize(100, 0))
        self.ipts_lineedit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ipts_lineedit.setObjectName(_fromUtf8("ipts_lineedit"))
        self.horizontalLayout_2.addWidget(self.ipts_lineedit)
        self.clear_ipts = QtGui.QPushButton(self.page)
        self.clear_ipts.setMinimumSize(QtCore.QSize(25, 20))
        self.clear_ipts.setMaximumSize(QtCore.QSize(25, 16777215))
        self.clear_ipts.setText(_fromUtf8(""))
        self.clear_ipts.setObjectName(_fromUtf8("clear_ipts"))
        self.horizontalLayout_2.addWidget(self.clear_ipts)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.run_radio_button = QtGui.QRadioButton(self.page)
        self.run_radio_button.setObjectName(_fromUtf8("run_radio_button"))
        self.horizontalLayout.addWidget(self.run_radio_button)
        self.run_number_lineedit = QtGui.QLineEdit(self.page)
        self.run_number_lineedit.setObjectName(_fromUtf8("run_number_lineedit"))
        self.horizontalLayout.addWidget(self.run_number_lineedit)
        self.clear_run = QtGui.QPushButton(self.page)
        self.clear_run.setMinimumSize(QtCore.QSize(25, 20))
        self.clear_run.setMaximumSize(QtCore.QSize(25, 16777215))
        self.clear_run.setText(_fromUtf8(""))
        self.clear_run.setObjectName(_fromUtf8("clear_run"))
        self.horizontalLayout.addWidget(self.clear_run)
        self.run_number_label = QtGui.QLabel(self.page)
        self.run_number_label.setObjectName(_fromUtf8("run_number_label"))
        self.horizontalLayout.addWidget(self.run_number_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 481, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 838, 639))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.splitter = QtGui.QSplitter(self.page_2)
        self.splitter.setFrameShape(QtGui.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtGui.QFrame.Plain)
        self.splitter.setLineWidth(4)
        self.splitter.setMidLineWidth(9)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(14)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tableWidget = QtGui.QTableWidget(self.widget)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 141, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.remove_criteria_button = QtGui.QPushButton(self.widget)
        self.remove_criteria_button.setEnabled(False)
        self.remove_criteria_button.setMaximumSize(QtCore.QSize(30, 30))
        self.remove_criteria_button.setObjectName(_fromUtf8("remove_criteria_button"))
        self.horizontalLayout_4.addWidget(self.remove_criteria_button)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.add_criteria_button = QtGui.QPushButton(self.widget)
        self.add_criteria_button.setEnabled(False)
        self.add_criteria_button.setMaximumSize(QtCore.QSize(30, 30))
        self.add_criteria_button.setObjectName(_fromUtf8("add_criteria_button"))
        self.horizontalLayout_4.addWidget(self.add_criteria_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.global_rule_label = QtGui.QLabel(self.widget)
        self.global_rule_label.setEnabled(False)
        self.global_rule_label.setObjectName(_fromUtf8("global_rule_label"))
        self.horizontalLayout_6.addWidget(self.global_rule_label)
        self.global_rule_lineedit = QtGui.QLineEdit(self.widget)
        self.global_rule_lineedit.setEnabled(False)
        self.global_rule_lineedit.setReadOnly(True)
        self.global_rule_lineedit.setObjectName(_fromUtf8("global_rule_lineedit"))
        self.horizontalLayout_6.addWidget(self.global_rule_lineedit)
        self.global_rule_button = QtGui.QPushButton(self.widget)
        self.global_rule_button.setEnabled(False)
        self.global_rule_button.setObjectName(_fromUtf8("global_rule_button"))
        self.horizontalLayout_6.addWidget(self.global_rule_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.filter_result_label = QtGui.QLabel(self.widget1)
        self.filter_result_label.setEnabled(False)
        self.filter_result_label.setObjectName(_fromUtf8("filter_result_label"))
        self.verticalLayout_2.addWidget(self.filter_result_label)
        self.tableWidget_filter_result = QtGui.QTableWidget(self.widget1)
        self.tableWidget_filter_result.setEnabled(False)
        self.tableWidget_filter_result.setAlternatingRowColors(True)
        self.tableWidget_filter_result.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget_filter_result.setObjectName(_fromUtf8("tableWidget_filter_result"))
        self.tableWidget_filter_result.setColumnCount(0)
        self.tableWidget_filter_result.setRowCount(0)
        self.tableWidget_filter_result.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_filter_result.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget_filter_result)
        self.verticalLayout_5.addWidget(self.splitter)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.toolBox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.import_button = QtGui.QPushButton(Dialog)
        self.import_button.setEnabled(False)
        self.import_button.setObjectName(_fromUtf8("import_button"))
        self.horizontalLayout_3.addWidget(self.import_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(1)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.cancel_button_clicked)
        QtCore.QObject.connect(self.import_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.import_button_clicked)
        QtCore.QObject.connect(self.ipts_radio_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.radio_button_changed)
        QtCore.QObject.connect(self.run_radio_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.radio_button_changed)
        QtCore.QObject.connect(self.ipts_combobox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), Dialog.ipts_selection_changed)
        QtCore.QObject.connect(self.run_number_lineedit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), Dialog.run_number_return_pressed)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.change_user_clicked)
        QtCore.QObject.connect(self.ipts_lineedit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.ipts_text_changed)
        QtCore.QObject.connect(self.clear_ipts, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.clear_ipts)
        QtCore.QObject.connect(self.clear_run, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.clear_run)
        QtCore.QObject.connect(self.remove_criteria_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.remove_criteria_clicked)
        QtCore.QObject.connect(self.add_criteria_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.add_criteria_clicked)
        QtCore.QObject.connect(self.run_number_lineedit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.run_number_text_changed)
        QtCore.QObject.connect(self.toolBox, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), Dialog.toolbox_changed)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.import_button, self.ipts_combobox)
        Dialog.setTabOrder(self.ipts_combobox, self.ipts_lineedit)
        Dialog.setTabOrder(self.ipts_lineedit, self.run_number_lineedit)
        Dialog.setTabOrder(self.run_number_lineedit, self.cancel_button)
        Dialog.setTabOrder(self.cancel_button, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.run_radio_button)
        Dialog.setTabOrder(self.run_radio_button, self.ipts_radio_button)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.ipts_radio_button.setText(_translate("Dialog", "Select IPTS", None))
        self.ipts_label.setText(_translate("Dialog", "or", None))
        self.error_message.setText(_translate("Dialog", "IPTS # Does Not Exist !", None))
        self.label_3.setText(_translate("Dialog", "IPTS-", None))
        self.run_radio_button.setText(_translate("Dialog", "Run(s) #", None))
        self.run_number_label.setText(_translate("Dialog", "1,3-5,10", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Dialog", "Select Runs to Import", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Rule #", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Keyword", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Criteria", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Values", None))
        self.remove_criteria_button.setText(_translate("Dialog", "-", None))
        self.add_criteria_button.setText(_translate("Dialog", "+", None))
        self.global_rule_label.setText(_translate("Dialog", "Global Rule:", None))
        self.global_rule_button.setText(_translate("Dialog", "Edit ...", None))
        self.filter_result_label.setText(_translate("Dialog", "Filter + Rule Result", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Dialog", "Filters and Rules", None))
        self.pushButton.setText(_translate("Dialog", "Change User ...", None))
        self.cancel_button.setText(_translate("Dialog", "Close", None))
        self.import_button.setText(_translate("Dialog", "Import", None))

