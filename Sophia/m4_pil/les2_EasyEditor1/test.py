import os

from PIL import Image
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap

workdir = ''


class ImageProcessor():

    def __init__(self):
        self.Image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modifated/'

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        lb_image.hide()
        pixmap_image = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmap_image = pixmap_image.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmap_image)
        lb_image.show()


def showChosenImage():
    """показать выбранную картинку"""
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)


def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def showFilenamesList():
    extensions = '.jpg .jpeg .png .gif .bmp'.split()
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for file in filenames:
        lw_files.addItem(file)


def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.lower().endswith(ext):
                result.append(filename)
    return result


app = QApplication([])
win = QWidget()

win.resize(700, 500)
win.setWindowTitle('Easy Editor')

lb_image = QLabel('картинка')
btn_dir = QPushButton('папка')
lw_files = QListWidget()

btn_left = QPushButton('лево')
btn_right = QPushButton('право')
btn_flip = QPushButton('зеркало')
btn_sharp = QPushButton('жоско')
btn_bw = QPushButton('Ч.Б')
row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)

row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)

col2.addLayout(row_tools)

row.addLayout(col1)
row.addLayout(col2)
win.setLayout(row)

btn_dir.clicked.connect(showFilenamesList)
lw_files.currentRowChanged.connect(showChosenImage)

workimage = ImageProcessor()

win.show()
app.exec()
