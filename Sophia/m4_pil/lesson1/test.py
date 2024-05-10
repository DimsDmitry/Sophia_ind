question = input('Введите команду (off - завершить):')
while question != 'off':
    if question == 'Рассказать анегдот':
        print('Почему улыбалась Джоконда? Ее смешил Леонардо да Винчи!')
        question = input('Введите команду (off - завершить):')
    elif question == 'Купить мерч':
        print('Список товаров: футболка, джинсы, кроссовки')
        question1 = input('Введите товар:')
        if question1 == 'футболка':
            print('К оплате: 1000р')
        elif question1 == 'джинсы':
            print('К оплате: 1500р')
        elif question1 == 'кроссовки':
            print('К оплате: 1200р')
    elif question == 'Рекомендовать музыку':
        question2 = input('Введите ваше настроение:')
        if question2 == 'веселое':
            print('Рекомедую Шансон')
        elif question2 == 'грустное':
            print('Рекомедую Джаз')
        else:
            print('Рекомедую Хип-хоп')
        question = input('Введите команду (off - завершить):')
    else:
        print('Я тебя не понимаю')
    question = input('Введите команду (off - завершить):')