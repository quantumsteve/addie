# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/ui_mass_density.ui'
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
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(462, 363)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setModal(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.mass_density_radio_button = QtGui.QRadioButton(Dialog)
        self.mass_density_radio_button.setChecked(True)
        self.mass_density_radio_button.setObjectName(_fromUtf8("mass_density_radio_button"))
        self.horizontalLayout_6.addWidget(self.mass_density_radio_button)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.mass_density_line_edit = QtGui.QLineEdit(self.frame)
        self.mass_density_line_edit.setObjectName(_fromUtf8("mass_density_line_edit"))
        self.horizontalLayout_3.addWidget(self.mass_density_line_edit)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(112, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_6.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.mass_density_error_message = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mass_density_error_message.sizePolicy().hasHeightForWidth())
        self.mass_density_error_message.setSizePolicy(sizePolicy)
        self.mass_density_error_message.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.mass_density_error_message.setObjectName(_fromUtf8("mass_density_error_message"))
        self.horizontalLayout_9.addWidget(self.mass_density_error_message)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setMinimumSize(QtCore.QSize(30, 30))
        self.label_7.setMaximumSize(QtCore.QSize(30, 30))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_9.addWidget(self.label_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.number_density_radio_button = QtGui.QRadioButton(Dialog)
        self.number_density_radio_button.setObjectName(_fromUtf8("number_density_radio_button"))
        self.horizontalLayout_7.addWidget(self.number_density_radio_button)
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.number_density_line_edit = QtGui.QLineEdit(self.frame_2)
        self.number_density_line_edit.setObjectName(_fromUtf8("number_density_line_edit"))
        self.horizontalLayout_4.addWidget(self.number_density_line_edit)
        self.number_density_units = QtGui.QLabel(self.frame_2)
        self.number_density_units.setObjectName(_fromUtf8("number_density_units"))
        self.horizontalLayout_4.addWidget(self.number_density_units)
        spacerItem2 = QtGui.QSpacerItem(69, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_7.addWidget(self.frame_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.number_density_error_message = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_density_error_message.sizePolicy().hasHeightForWidth())
        self.number_density_error_message.setSizePolicy(sizePolicy)
        self.number_density_error_message.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.number_density_error_message.setObjectName(_fromUtf8("number_density_error_message"))
        self.horizontalLayout_10.addWidget(self.number_density_error_message)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setMinimumSize(QtCore.QSize(30, 30))
        self.label_10.setMaximumSize(QtCore.QSize(30, 30))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_10.addWidget(self.label_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.mass_geometry_radio_button = QtGui.QRadioButton(Dialog)
        self.mass_geometry_radio_button.setText(_fromUtf8(""))
        self.mass_geometry_radio_button.setObjectName(_fromUtf8("mass_geometry_radio_button"))
        self.horizontalLayout_8.addWidget(self.mass_geometry_radio_button)
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.frame_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.mass_line_edit = QtGui.QLineEdit(self.frame_3)
        self.mass_line_edit.setObjectName(_fromUtf8("mass_line_edit"))
        self.horizontalLayout.addWidget(self.mass_line_edit)
        self.label_4 = QtGui.QLabel(self.frame_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.frame_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.geometry_label = QtGui.QLabel(self.frame_3)
        self.geometry_label.setObjectName(_fromUtf8("geometry_label"))
        self.horizontalLayout_2.addWidget(self.geometry_label)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_8.addWidget(self.frame_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        spacerItem6 = QtGui.QSpacerItem(20, 32, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Mass Density / Number Density / ...", None))
        self.mass_density_radio_button.setText(_translate("Dialog", "Mass Density", None))
        self.label.setText(_translate("Dialog", "g/cc", None))
        self.mass_density_error_message.setText(_translate("Dialog", "Missing Chemical Formula to update Mass Density!", None))
        self.number_density_radio_button.setText(_translate("Dialog", "Number Density", None))
        self.number_density_units.setText(_translate("Dialog", "atom/A", None))
        self.number_density_error_message.setText(_translate("Dialog", "Missing Chemical Formula to update Number Density!", None))
        self.label_3.setText(_translate("Dialog", "Mass", None))
        self.label_4.setText(_translate("Dialog", "g", None))
        self.label_5.setText(_translate("Dialog", "geometry:", None))
        self.geometry_label.setText(_translate("Dialog", "cylindrical", None))

