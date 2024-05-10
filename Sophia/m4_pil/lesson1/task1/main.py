from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

# открой файл с оригиналом картинки
with Image.open('original.jpg') as pic:
    print('Изображение открыто!\nРазмер:', pic.size)

    # сделай оригинал изображения чёрно-белым
    pic_gray = pic.convert('L')
    pic_gray.save('gray.jpg')
    pic_gray.show()
    print('Размер:', pic_gray.size)
    print('Формат:', pic_gray.format)
    print('Тип:', pic_gray.mode)
    # сделай оригинал изображения размытым
    pic_blured = pic.filter(ImageFilter.BLUR)
    pic_blured.save('blured.jpg')
    pic_blured.show()
    # поверни оригинал изображения на 180 градусов
    pic_mirrow = pic.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirrow.save('mirrow.jpg')
    pic_mirrow.show()
    # добавление контраста
    pic_contrast = ImageEnhance.Contrast(pic).enhance(1.5)
    pic_contrast.save('cont.jpg')
    pic_contrast.show()