from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QListWidget,
    QLineEdit, QPushButton,
    QHBoxLayout
)
from PyQt5.QtGui import QIcon

try:
    from src.constants import *
    import rc.resources
except:
    import sys, os
    sys.path.insert(0, os.path.dirname(sys.path[0]))
    from configparser import ConfigParser
    from constants import *
    import rc.resources

class LinksSettings(QWidget):

    def __init__(self, parser, parent=None):
        super(LinksSettings, self).__init__(parent)
        self.parser = parser
        self.setup_UI()

    def setup_UI(self):
        self.setWindowIcon(QIcon(":/hyperlink.png"))
        self.setWindowTitle("URL Links")
        self.mainlayout = QVBoxLayout()
        self.listlayout = QVBoxLayout()
        self.btnslayout = QHBoxLayout()
        self.setup_url_list()
        self.setup_btns()
        self.setLayout(self.mainlayout)
        self.resize(self.mainlayout.sizeHint())
        self.setMinimumWidth(640)

    def setup_url_list(self):
        self.urllist = QListWidget()
        self.urllink = QLineEdit()
        self.mainlayout.addWidget(self.urllist)
        self.mainlayout.addWidget(self.urllink)
        self.mainlayout.addLayout(self.listlayout)

    def setup_btns(self):
        self.btns_conf = {
            "cancel": ("Cancel", self.close),
            "submit": ("Apply", self.apply)
        }
        self.btns = {}
        self.btns["new"] = QPushButton("New")
        self.btnslayout.addWidget(self.btns["new"])
        self.btns["delete"] = QPushButton("Delete")
        self.btnslayout.addWidget(self.btns["delete"])
        self.btnslayout.addStretch()
        for name, val in self.btns_conf.items():
            btn = QPushButton(val[0])
            btn.clicked.connect(val[1])
            self.btnslayout.addWidget(btn)
            self.btns[name] = btn
        self.mainlayout.addLayout(self.btnslayout)

    def apply(self):
        pass

    def update_url_list(self):
        pass

if __name__=="__main__":
    parser = ConfigParser()
    parser.read(LINKS_CONFIG)
    app = QApplication(sys.argv)
    widget = LinksSettings(parser)
    widget.show()
    sys.exit(app.exec())