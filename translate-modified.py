import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(from_file, to_file='translated.txt', from_lang='', to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    text = ''
    with open(from_file, encoding='utf-8') as read_file:
        for line in read_file:
            text = text + line
    if from_lang != '':
        language = f'{from_lang}-{to_lang}'
    else:
        language = to_lang


    params = {
        'key': API_KEY,
        'text': text,
        'lang': language,
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    with open(to_file, 'w', encoding='utf-8') as final_translation:
        final_translation.write(''.join(json_['text']))
    return ''.join(json_['text'])


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    print(translate_it('DE.txt', 'translated.txt'))