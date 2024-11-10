# runmain.py
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QStackedWidget
import webbrowser
import subprocess

from main1 import Ui_MainWindow  # 确保main.py在同一目录下

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化UI


        # 如果需要，可以在这里连接信号和槽函数
        # 例如，为pushButton连接一个槽函数:
        # self.pushButton.clicked.connect(self.on_pushButton_clicked)

    # 示例槽函数
    def on_pushButton_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        print("pass")

    def on_pushButton_2_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        print("pass")
    def on_pushButton_3_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        print("pass")
    def on_pushButton_4_clicked(self):
        self.stackedWidget.setCurrentIndex(3)
        print("pass")
    def on_web_clicked(self):
        webbrowser.open("https://www.bilibili.com/video/BV1he4y1w7wB/?spm_id_from=333.337.search-card.all.click&vd_source=85ad3a4aa06d461610573d998426894b")
        print("pass")
    def on_mulanshell_clicked(self):
        subprocess.Popen(['start', 'Python3.8.exe'], shell=True)
        print("pass")
    def on_waixinren_clicked(self):
        subprocess.Popen(['start', 'waixinren.exe'], shell=True)
        print("pass")
    def on_dnyouxuanshuxueti_clicked(self):
        subprocess.Popen(['start', 'tu.exe'], shell=True)
        print("pass")

    def on_pushButton_5_clicked(self):
        subprocess.Popen(['start', 'englishai.exe'], shell=True)
        print("pass")
    def on_dnyouxuanyuwenti_clicked(self):
        subprocess.Popen(['start', 'gushici.exe'], shell=True)
        print("pass")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
