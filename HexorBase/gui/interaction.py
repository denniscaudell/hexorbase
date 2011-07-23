import os
from PyQt4 import QtGui,QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

try:
    from PyQt4 import Qsci
except:pass

class interaction_dialog(object):
    def setupUi(self, interaction_dialog):
        interaction_dialog.setObjectName(_fromUtf8("interaction_dialog"))
        interaction_dialog.resize(1000, 641)
        self.verticalLayout_4 = QtGui.QVBoxLayout(interaction_dialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(interaction_dialog)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("%s/Icons/Database.png"%(os.getcwd()))))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.interact_server_name = QtGui.QLabel(interaction_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.interact_server_name.setFont(font)
        self.interact_server_name.setObjectName(_fromUtf8("interact_server_name"))
        self.verticalLayout.addWidget(self.interact_server_name)
        self.interact_server_connection = QtGui.QLabel(interaction_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.interact_server_connection.setFont(font)
        self.interact_server_connection.setObjectName(_fromUtf8("interact_server_connection"))
        self.verticalLayout.addWidget(self.interact_server_connection)
        self.label_4 = QtGui.QLabel(interaction_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.interact_comboBox = QtGui.QComboBox(interaction_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.interact_comboBox.setFont(font)
        self.interact_comboBox.setObjectName(_fromUtf8("interact_comboBox"))
        self.verticalLayout_2.addWidget(self.interact_comboBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(interaction_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.interact_browse = QtGui.QPushButton(interaction_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.interact_browse.setFont(font)
        self.interact_browse.setObjectName(_fromUtf8("interact_browse"))
        self.horizontalLayout_2.addWidget(self.interact_browse)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.groupBox = QtGui.QGroupBox(interaction_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.response_table = QtGui.QTableWidget(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.response_table.setFont(font)
        self.response_table.setObjectName(_fromUtf8("response_table"))
        self.response_table.setColumnCount(0)
        self.response_table.setRowCount(0)
        self.horizontalLayout_7.addWidget(self.response_table)
        spacerItem1 = QtGui.QSpacerItem(0, 241, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.interact_textBrowser = QtGui.QTextBrowser(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interact_textBrowser.sizePolicy().hasHeightForWidth())
        self.interact_textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.interact_textBrowser.setFont(font)
        self.interact_textBrowser.setObjectName(_fromUtf8("interact_textBrowser"))
        self.horizontalLayout_8.addWidget(self.interact_textBrowser)
        spacerItem2 = QtGui.QSpacerItem(0, 47, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(interaction_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.sqleditor = Qsci.QsciScintilla(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqleditor.sizePolicy().hasHeightForWidth())
        self.sqleditor.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.sqleditor.setFont(font)
        self.sqleditor.setToolTip(_fromUtf8(""))
        self.sqleditor.setWhatsThis(_fromUtf8(""))
        self.sqleditor.setObjectName(_fromUtf8("sqleditor"))
        self.horizontalLayout_11.addWidget(self.sqleditor)
        spacerItem3 = QtGui.QSpacerItem(0, 123, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem4 = QtGui.QSpacerItem(0, 32, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.execute_sql_button = QtGui.QPushButton(interaction_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.execute_sql_button.sizePolicy().hasHeightForWidth())
        self.execute_sql_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.execute_sql_button.setFont(font)
        self.execute_sql_button.setObjectName(_fromUtf8("execute_sql_button"))
        self.horizontalLayout_4.addWidget(self.execute_sql_button)
        self.tables_button = QtGui.QPushButton(interaction_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tables_button.sizePolicy().hasHeightForWidth())
        self.tables_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tables_button.setFont(font)
        self.tables_button.setObjectName(_fromUtf8("tables_button"))
        self.horizontalLayout_4.addWidget(self.tables_button)
        self.save_report_button = QtGui.QPushButton(interaction_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_report_button.sizePolicy().hasHeightForWidth())
        self.save_report_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.save_report_button.setFont(font)
        self.save_report_button.setObjectName(_fromUtf8("save_report_button"))
        self.horizontalLayout_4.addWidget(self.save_report_button)
        self.close_interact_button = QtGui.QPushButton(interaction_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_interact_button.sizePolicy().hasHeightForWidth())
        self.close_interact_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.close_interact_button.setFont(font)
        self.close_interact_button.setObjectName(_fromUtf8("close_interact_button"))
        self.horizontalLayout_4.addWidget(self.close_interact_button)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.retranslateUi(interaction_dialog)
        QtCore.QMetaObject.connectSlotsByName(interaction_dialog)

    def retranslateUi(self, interaction_dialog):
        interaction_dialog.setWindowTitle(QtGui.QApplication.translate("interaction_dialog", "Database Interaction", None, QtGui.QApplication.UnicodeUTF8))
        self.interact_server_name.setText(QtGui.QApplication.translate("interaction_dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.interact_server_connection.setText(QtGui.QApplication.translate("interaction_dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("interaction_dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.interact_browse.setText(QtGui.QApplication.translate("interaction_dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("interaction_dialog", "SQL Server Response", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("interaction_dialog", "SQL Query  (Press F5 to execute)", None, QtGui.QApplication.UnicodeUTF8))
        self.execute_sql_button.setText(QtGui.QApplication.translate("interaction_dialog", "Execute SQL Script", None, QtGui.QApplication.UnicodeUTF8))
        self.tables_button.setText(QtGui.QApplication.translate("interaction_dialog", "Show Tables", None, QtGui.QApplication.UnicodeUTF8))
        self.save_report_button.setText(QtGui.QApplication.translate("interaction_dialog", "Save Report", None, QtGui.QApplication.UnicodeUTF8))
        self.close_interact_button.setText(QtGui.QApplication.translate("interaction_dialog", "Close Connection", None, QtGui.QApplication.UnicodeUTF8))
