from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutMain = QtGui.QVBoxLayout()
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")
        self.horizontalLayoutLoad = QtGui.QHBoxLayout()
        self.horizontalLayoutLoad.setObjectName("horizontalLayoutLoad")
        self.verticalLayoutOk = QtGui.QVBoxLayout()
        self.verticalLayoutOk.setObjectName("verticalLayoutOk")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayoutOk.addItem(spacerItem)
        self.labelKey = QtGui.QLabel(Form)
        self.labelKey.setAlignment(QtCore.Qt.AlignCenter)
        self.labelKey.setObjectName("labelKey")
        self.verticalLayoutOk.addWidget(self.labelKey)
        self.lineEditKey = QtGui.QLineEdit(Form)
        self.lineEditKey.setObjectName("lineEditKey")
        self.verticalLayoutOk.addWidget(self.lineEditKey)
        self.pushButtonOpen = QtGui.QPushButton(Form)
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.verticalLayoutOk.addWidget(self.pushButtonOpen)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayoutOk.addItem(spacerItem1)
        self.verticalLayoutOk.setStretch(0, 2)
        self.verticalLayoutOk.setStretch(1, 1)
        self.verticalLayoutOk.setStretch(2, 1)
        self.verticalLayoutOk.setStretch(4, 2)
        self.horizontalLayoutLoad.addLayout(self.verticalLayoutOk)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayoutLoad.addWidget(self.listWidget)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton.setShortcut("")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutLoad.addWidget(self.pushButton)
        self.horizontalLayoutLoad.setStretch(0, 1)
        self.horizontalLayoutLoad.setStretch(1, 5)
        self.verticalLayoutMain.addLayout(self.horizontalLayoutLoad)
        self.plainTextEditLetter = QtGui.QPlainTextEdit(Form)
        self.plainTextEditLetter.setObjectName("plainTextEditLetter")
        self.verticalLayoutMain.addWidget(self.plainTextEditLetter)
        self.horizontalLayoutCopy = QtGui.QHBoxLayout()
        self.horizontalLayoutCopy.setObjectName("horizontalLayoutCopy")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutCopy.addItem(spacerItem2)
        self.labelName = QtGui.QLabel(Form)
        self.labelName.setFrameShape(QtGui.QFrame.NoFrame)
        self.labelName.setObjectName("labelName")
        self.horizontalLayoutCopy.addWidget(self.labelName)
        self.lineEditName = QtGui.QLineEdit(Form)
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayoutCopy.addWidget(self.lineEditName)
        self.pushButtonCopy = QtGui.QPushButton(Form)
        self.pushButtonCopy.setObjectName("pushButtonCopy")
        self.horizontalLayoutCopy.addWidget(self.pushButtonCopy)
        self.verticalLayoutMain.addLayout(self.horizontalLayoutCopy)
        self.horizontalLayoutSave = QtGui.QHBoxLayout()
        self.horizontalLayoutSave.setObjectName("horizontalLayoutSave")
        self.labelKeysSave = QtGui.QLabel(Form)
        self.labelKeysSave.setObjectName("labelKeysSave")
        self.horizontalLayoutSave.addWidget(self.labelKeysSave)
        self.lineEditKeysSave = QtGui.QLineEdit(Form)
        self.lineEditKeysSave.setObjectName("lineEditKeysSave")
        self.horizontalLayoutSave.addWidget(self.lineEditKeysSave)
        self.pushButtonSave = QtGui.QPushButton(Form)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayoutSave.addWidget(self.pushButtonSave)
        self.verticalLayoutMain.addLayout(self.horizontalLayoutSave)
        self.verticalLayoutMain.setStretch(0, 1)
        self.verticalLayoutMain.setStretch(1, 10)
        self.horizontalLayout.addLayout(self.verticalLayoutMain)
        self.horizontalLayout.setStretch(0, 10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "LetterSaver", None, QtGui.QApplication.UnicodeUTF8))
        self.labelKey.setText(QtGui.QApplication.translate("Form", "Enter key", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOpen.setText(QtGui.QApplication.translate("Form", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "DEL", None, QtGui.QApplication.UnicodeUTF8))
        self.labelName.setText(QtGui.QApplication.translate("Form", "Copy letter with name", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCopy.setText(QtGui.QApplication.translate("Form", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.labelKeysSave.setText(QtGui.QApplication.translate("Form", "Enter keys and press save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSave.setText(QtGui.QApplication.translate("Form", "Save", None, QtGui.QApplication.UnicodeUTF8))

