import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap

from PIL import Image

workdir = ''


class ImageProcessor:
    """класс-обработчик фотографии"""

    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'

    def loadImage(self, dir, filename):
        """при загрузке запоминаем путь и имя файла. открываем файл"""
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        """показать картинку"""
        lb_image.hide()
        pixmap_image = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmap_image = pixmap_image.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmap_image)
        lb_image.show()

    def saveImage(self):
        """сохраняет копию файла в подпапке"""
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def do_bw(self):
        """сделать чёрно-белым"""
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)


def showChosenImage():
    """показать выбранную картинку"""
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)


def chooseWorkdir():
    """получает доступ к папке компьютера"""
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def showFilenamesList():
    extensions = '.jpg .jpeg .png .gif .bmp'.split()
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    # отображаем список файлов в окошке слева
    for file in filenames:
        lw_files.addItem(file)


def filter(files, extensions):
    """проверяет, является ли файл картинкой. если да - добавляет в список, возвращает его"""
    result = []
    for filename in files:
        for ext in extensions:
            if filename.lower().endswith(ext):
                result.append(filename)
    return result


# создаём приложение и окно
app = QApplication([])
win = QWidget()
# установим размеры окна и заголовок
win.resize(700, 500)
win.setWindowTitle('Easy Editor')

# создаём виджеты
lb_image = QLabel('Картинка')
btn_dir = QPushButton('Папка')
lw_files = QListWidget()

btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_flip = QPushButton('Зеркало')
btn_sharp = QPushButton('Резкость')
btn_bw = QPushButton('Ч/Б')

# размещаем виджеты
row = QHBoxLayout()  # основная строка
col1 = QVBoxLayout()  # делится на 2 столбца
col2 = QVBoxLayout()
# в левый ряд добавляем кнопку и список виджетов
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
# в правый ряд - картинку и строку кнопок
col2.addWidget(lb_image)
# строка кнопок:
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)

col2.addLayout(row_tools)
# добавляем две колонки на главную линию
row.addLayout(col1)
row.addLayout(col2)
win.setLayout(row)

workimage = ImageProcessor()
# подключаем методы к кнопкам
btn_dir.clicked.connect(showFilenamesList)
lw_files.currentRowChanged.connect(showChosenImage)

btn_bw.clicked.connect(workimage.do_bw)

win.show()
app.exec()
