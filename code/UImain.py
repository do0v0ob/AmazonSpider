# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_spiderTools(object):
    def setupUi(self, spiderTools):
        spiderTools.setObjectName("spiderTools")
        spiderTools.resize(733, 312)
        self.label = QtWidgets.QLabel(spiderTools)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.goods_et = QtWidgets.QLineEdit(spiderTools)
        self.goods_et.setGeometry(QtCore.QRect(200, 20, 291, 31))
        self.goods_et.setObjectName("goods_et")
        self.label_2 = QtWidgets.QLabel(spiderTools)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.page_start_et = QtWidgets.QLineEdit(spiderTools)
        self.page_start_et.setGeometry(QtCore.QRect(160, 60, 41, 31))
        self.page_start_et.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.page_start_et.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.page_start_et.setInputMask("")
        self.page_start_et.setReadOnly(False)
        self.page_start_et.setObjectName("page_start_et")
        self.label_3 = QtWidgets.QLabel(spiderTools)
        self.label_3.setGeometry(QtCore.QRect(210, 60, 41, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.page_end_et = QtWidgets.QLineEdit(spiderTools)
        self.page_end_et.setGeometry(QtCore.QRect(240, 60, 41, 31))
        self.page_end_et.setObjectName("page_end_et")
        self.page_flags_cb = QtWidgets.QCheckBox(spiderTools)
        self.page_flags_cb.setGeometry(QtCore.QRect(290, 70, 91, 19))
        self.page_flags_cb.setObjectName("page_flags_cb")
        self.groupBox = QtWidgets.QGroupBox(spiderTools)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 691, 61))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 601, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_flags_cb = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.title_flags_cb.setObjectName("title_flags_cb")
        self.horizontalLayout.addWidget(self.title_flags_cb)
        self.price_flags_cb = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.price_flags_cb.setObjectName("price_flags_cb")
        self.horizontalLayout.addWidget(self.price_flags_cb)
        self.comment_flags_cb = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.comment_flags_cb.setObjectName("comment_flags_cb")
        self.horizontalLayout.addWidget(self.comment_flags_cb)
        self.comdetail_flags_cb = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.comdetail_flags_cb.setObjectName("comdetail_flags_cb")
        self.horizontalLayout.addWidget(self.comdetail_flags_cb)
        self.groupBox_2 = QtWidgets.QGroupBox(spiderTools)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 170, 491, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 471, 101))
        self.textEdit.setObjectName("textEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(spiderTools)
        self.groupBox_3.setGeometry(QtCore.QRect(520, 170, 141, 41))
        self.groupBox_3.setObjectName("groupBox_3")
        self.csv_rb = QtWidgets.QRadioButton(self.groupBox_3)
        self.csv_rb.setGeometry(QtCore.QRect(10, 20, 115, 19))
        self.csv_rb.setChecked(True)
        self.csv_rb.setObjectName("csv_rb")
        self.text_cb = QtWidgets.QRadioButton(self.groupBox_3)
        self.text_cb.setGeometry(QtCore.QRect(80, 20, 115, 19))
        self.text_cb.setChecked(False)
        self.text_cb.setObjectName("text_cb")
        self.pushButton = QtWidgets.QPushButton(spiderTools)
        self.pushButton.setGeometry(QtCore.QRect(660, 210, 51, 81))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_4 = QtWidgets.QGroupBox(spiderTools)
        self.groupBox_4.setGeometry(QtCore.QRect(520, 220, 131, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.path_tb = QtWidgets.QPushButton(self.groupBox_4)
        self.path_tb.setGeometry(QtCore.QRect(100, 30, 31, 21))
        self.path_tb.setObjectName("path_tb")
        self.path_ed = QtWidgets.QLineEdit(self.groupBox_4)
        self.path_ed.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.path_ed.setObjectName("path_ed")

        self.retranslateUi(spiderTools)
        QtCore.QMetaObject.connectSlotsByName(spiderTools)

    def retranslateUi(self, spiderTools):
        _translate = QtCore.QCoreApplication.translate
        spiderTools.setWindowTitle(_translate("spiderTools", "Form"))
        self.label.setText(_translate("spiderTools", "请输入爬取的商品名:"))
        self.label_2.setText(_translate("spiderTools", "请输入爬取页数:"))
        self.label_3.setText(_translate("spiderTools", "一"))
        self.page_flags_cb.setText(_translate("spiderTools", "全部页数"))
        self.groupBox.setTitle(_translate("spiderTools", "爬取属性"))
        self.title_flags_cb.setText(_translate("spiderTools", "标题"))
        self.price_flags_cb.setText(_translate("spiderTools", "价格"))
        self.comment_flags_cb.setText(_translate("spiderTools", "评论条数"))
        self.comdetail_flags_cb.setText(_translate("spiderTools", "评论详情"))
        self.groupBox_2.setTitle(_translate("spiderTools", "输出信息"))
        self.textEdit.setHtml(_translate("spiderTools", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_3.setTitle(_translate("spiderTools", "保存方式"))
        self.csv_rb.setText(_translate("spiderTools", "csv"))
        self.text_cb.setText(_translate("spiderTools", "text"))
        self.pushButton.setText(_translate("spiderTools", "开始"))
        self.groupBox_4.setTitle(_translate("spiderTools", "保存到"))
        self.path_tb.setText(_translate("spiderTools", "..."))