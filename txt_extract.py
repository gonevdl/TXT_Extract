import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Extract(QWidget):
    def __init__(self):
        super(Extract, self).__init__()

        self.setFont(QFont("楷体"))
        self.setWindowTitle("TXT提取")
        self.setMinimumWidth(1000)

        self.label1 = QLabel("目标文件")
        self.label2 = QLabel("提取字符")

        self.linedit1 = QLineEdit()
        self.linedit2 = QLineEdit()

        self.btn1 = QPushButton('…')
        self.btn2 = QPushButton('确定')
        self.btn1.setMaximumWidth(60)
        self.btn1.setFont(QFont('kaiti', 6))
        self.btn1.setMaximumHeight(37)
        self.btn2.setMaximumHeight(37)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.linedit1)
        hbox1.addWidget(self.btn1)

        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.linedit2)
        hbox2.addWidget(self.btn2)

        vbox = QVBoxLayout()

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.btn1.clicked.connect(self.onbtn1click)
        self.btn2.clicked.connect(self.onbtn2click)

        # 保存打开的文件名
        self.finemame = []

    def onbtn1click(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        dlg.exec_()
        self.finemame = dlg.selectedFiles()
        self.linedit1.setText(self.finemame[0])
        print(self.finemame)

    def onbtn2click(self):
        src_name = self.finemame[0]  # type: str
        pos = src_name.rfind(".")
        des_name = src_name[0:pos] + "_extract.txt"
        target = self.linedit2.text()

        with open(src_name, 'r') as f:
            with open(des_name, 'w') as f1:
                line = ' '
                while line:
                    line = f.readline()
                    if target in line:
                        f1.write(line)
        QMessageBox.information(self, '提示', '完成', QMessageBox.Ok, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ext = Extract()
    ext.show()
    sys.exit(app.exec_())
