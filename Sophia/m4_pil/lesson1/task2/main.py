# создай методы для редактирования оригинала

# создай объект класса ImageEditor с данными картинки-оригинала

# отредактируй изображение и сохрани результат
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


class ImageEditor:
    def __init__(self, filename):
        # конструктор класса
        self.filename = filename
        self.original = None
        self.changed = []

    def open(self):
        # открыть и показать оригинал
        self.original = Image.open(self.filename)
        self.original.show()

    def do_left(self):
        # перевернуть фото слева направо
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)
        rotated.save('flipped.jpg')

    def do_cropped(self):
        # обрезаем фото
        box = (100, 100, 400, 450)
        cropped = self.original.crop(box)
        self.changed.append(cropped)
        cropped.save('cropped.jpg')


MyImage = ImageEditor('original.jpg')
MyImage.open()
MyImage.do_left()
MyImage.do_cropped()
for i in MyImage.changed:
    i.show()
