import sys
import time
import os
import threading

from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt5 import QtCore
from UImain import Ui_spiderTools
import spider

WARNING_FLAG = ""  # 用于记录弹框内容


class MyUi(Ui_spiderTools, QMainWindow):
    valueChanged = pyqtSignal()  # 自定义信号

    def __init__(self, parent=None):
        self.filepath = ""  # 用于保存文本路径

        super(MyUi, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())  # 设置窗口不能最大化和拉伸
        self.path_ed.setFocusPolicy(QtCore.Qt.NoFocus)  # 设置文本框不可编辑
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)  # 设置打印框不可编辑

        self.setWindowTitle('亚马逊爬取工具')  # 设置窗口标题

        self.intV = QIntValidator(0, 9999)  # 限制页数输入框输入类型
        self.page_start_et.setValidator(self.intV)  # 设置限制输入类型
        self.page_end_et.setValidator(self.intV)
        self.page_flags_cb.stateChanged.connect(self.et_setattr)  # 页数复选框点击事件
        self.pushButton.clicked.connect(self.on_check)  # 提交开始爬虫
        self.path_tb.clicked.connect(self.open_path)  # 选择保存位置

    # 获取保存路径
    def open_path(self):
        paths = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", None)  # 获取文本保路径
        if self.csv_rb.isChecked():
            print_format = self.csv_rb.text()
        else:
            print_format = self.text_cb.text()
        filename = "".join(time.strftime("%Y%m%d%X", time.localtime()).split(":")) + "." + print_format  # 文件名为本地时间
        self.filepath = os.path.join(paths, filename)
        self.path_ed.setText(self.filepath)  # 显示在文本框上

    # 开启线程处理爬虫模块
    def do(self, context, page_start, page_end, **kwargs):
        thread1 = threading.Thread(target=self.start_spider, args=(context, page_start, page_end),
                                   kwargs=(kwargs)).start()

    # 后台逻辑处理
    def on_check(self):
        global WARNING_FLAG
        if self.goods_et.text().strip() is "":  # 判断商品名是否为空
            WARNING_FLAG = "请输入要爬取的商品名称！"
        if not self.page_flags_cb.isChecked():
            if self.page_start_et.text() is "" or self.page_end_et.text() is "":  # 判断爬取的页数是否为空
                WARNING_FLAG = "爬取页数不能为空！"
        if not self.title_flags_cb.isChecked() and not self.price_flags_cb.isChecked():  # 判断爬取的属性是否为空
            if not self.comment_flags_cb.isChecked() and not self.comdetail_flags_cb.isChecked():
                WARNING_FLAG = "要爬取的内容属性不能为空！"
        if self.path_ed.text() == "":
            WARNING_FLAG = "请选择保存路径！"
        if WARNING_FLAG != "":
            reply = self.warning(WARNING_FLAG)
            if reply == 1024:
                WARNING_FLAG = ""
        else:
            context = self.goods_et.text().strip()
            if self.page_flags_cb.isChecked():
                page_start = 1
                page_end = "whole"
            else:
                page_start = self.page_start_et.text()
                page_end = self.page_end_et.text()
                if int(page_start) > int(page_end):
                    page_start, page_end = page_end, page_start
            check_flag = {"title": 0, "price": 0, "comment": 0, "comdetail": 0}  # 用于记录爬取哪些属性内容
            if self.title_flags_cb.isChecked():
                check_flag["title"] = 1
            if self.price_flags_cb.isChecked():
                check_flag["price"] = 1
            if self.comment_flags_cb.isChecked():
                check_flag["comment"] = 1
            if self.comdetail_flags_cb.isChecked():
                check_flag["comdetail"] = 1
            self.pushButton.setEnabled(False)  # 当点击提交时提交按钮不可再点击
            self.do(context, page_start, page_end, **check_flag)

    # 爬虫逻辑模块
    def start_spider(self, context, page_start, page_end, **kwargs):
        html = spider.my_requests(context, page_start)
        max_page = spider.get_max_page(html)
        if max_page is None:
            self.textEdit.append(f"未找到商品:{context},请检查..")
        else:
            self.textEdit.append(f"已找到商品:{context},共{max_page}页, 从{page_start}页开始爬取....")

            spider.my_spider(html, self.filepath, **kwargs)
            time.sleep(2)
            if page_start == page_end:
                self.textEdit.append("爬虫已完成!")
                self.valueChanged.connect(self.about)
                self.valueChanged.emit()
            elif page_end == "whole":
                for i in range(int(page_start) + 1, max_page + 1):
                    self.textEdit.append(f"第{i - 1}页爬取成功,开始爬取下一页!")
                    time.sleep(1)
                    html = spider.my_requests(context, i)
                    spider.my_spider(html, self.filepath, **kwargs)
                    if i == max_page:
                        self.textEdit.append(f"第{i}页爬取成功,爬虫已完成!")
                        self.valueChanged.connect(self.about)
                        self.valueChanged.emit()
            elif int(page_start) < int(page_end):
                if int(page_end) < max_page:
                    for i in range(int(page_start) + 1, int(page_end) + 1):
                        self.textEdit.append(f"第{i - 1}页爬取成功,开始爬取下一页!")
                        time.sleep(1)
                        html = spider.my_requests(context, i)
                        spider.my_spider(html, self.filepath, **kwargs)
                        if i == int(page_end):
                            self.textEdit.append(f"第{i}页爬取成功,爬虫已完成!")
                            self.valueChanged.connect(self.about)
                            self.valueChanged.emit()
        self.pushButton.setEnabled(True)  # 完成爬虫操作后，提交按钮可点击
        self.path_ed.setText("")  # 完成爬虫操作后，擦除之前的路径

    # 爬虫完成时弹窗
    def about(self):
        QMessageBox.about(self, "完成", "爬取完成")

    # 填写信息非法时弹窗
    def warning(self, msg):
        reply = QMessageBox.warning(self, "警告", f"{msg}")
        return reply

    # 属性修改模块
    def et_setattr(self):
        """
        当选中全部爬取时，触发
        """
        if self.page_flags_cb.isChecked():
            self.page_start_et.setFocusPolicy(QtCore.Qt.NoFocus)  # 将输入框设置为不可输入
            self.page_end_et.setFocusPolicy(QtCore.Qt.NoFocus)
            self.page_start_et.setCursor(QtCore.Qt.ArrowCursor)  # 将输入框鼠标设置为箭头
            self.page_end_et.setCursor(QtCore.Qt.ArrowCursor)
            self.page_start_et.setStyleSheet("background-color:gray")  # 将输入框背景颜色设置为灰色
            self.page_end_et.setStyleSheet("background-color:gray")
        else:
            self.page_start_et.setFocusPolicy(QtCore.Qt.StrongFocus)  # 将输入框设置为可输入
            self.page_end_et.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.page_start_et.setCursor(QtCore.Qt.IBeamCursor)  # 将输入框鼠标设置为可输入
            self.page_end_et.setCursor(QtCore.Qt.IBeamCursor)
            self.page_start_et.setStyleSheet("background-color:#ffffff")  # 将输入框背景颜色设置为白色
            self.page_end_et.setStyleSheet("background-color:#ffffff")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyUi()
    ui.show()
    sys.exit(app.exec_())
