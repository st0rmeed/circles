import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtCore import Qt, QRect
from PyQt6 import uic
import random


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.write_circle)
        self.show()

    def write_circle(self):
        x, y = random.randint(0, 800), random.randint(0, 600)
        d = random.randint(10, 100)
        self.circles.append((x, y, d))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for x, y, diameter in self.circles:
            qp.setBrush(QBrush(QColor(255, 255, 0)))
            qp.drawEllipse(QRect(x, y, diameter, diameter))
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Circles()
    sys.exit(app.exec())
