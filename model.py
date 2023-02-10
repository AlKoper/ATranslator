# импортируем каждый переводчик отдельно, чтобы испольовать его при выборе конкретного сервиса
from translatepy.translators.google import GoogleTranslate
from translatepy.translators.yandex import YandexTranslate
from translatepy.translators.microsoft import MicrosoftTranslate
from translatepy.translators.reverso import ReversoTranslate
from translatepy.translators.translatecom import TranslateComTranslate
import deepL    #Импортируем DeepL для перевода
from pathlib import Path  # импортируем pathlib дял удобства обработки всех файлов в папке


#Создадим функцию перевода
def text_translate(text, sour, dest, service):    #sour - язык исходного текста, dest - язык перевода
    if service == 'Google':
        Translate_service = GoogleTranslate()
    elif service == 'Yandex':
        Translate_service = YandexTranslate()
    elif service == 'Microsoft':
        Translate_service = MicrosoftTranslate()
    elif service == 'Reverso':
        Translate_service = ReversoTranslate()
    elif service == 'TranslateCom':
        Translate_service = TranslateComTranslate()
    result = str(Translate_service.translate(text, destination_language=dest, source_language=sour))
    Translate_service.clean_cache()
    return result

# Создадим функцию открытия/чтения адресов из файла FileLinks.txt (хранится/записывается информация для работы скрипта)
def Openfilelinks():
    with open('FileLinks.txt', 'r') as file:
        lines = file.readlines()
    return lines[1].replace('\n', ''), lines[3].replace('\n', ''), lines[5].replace('\n', ''), lines[7].replace('\n', ''), lines[8].replace('\n', '')


#Создадим функцию для сохранения переведенного текста в новый файл
def trans_text_save(filename, text, translate, service):
    filename = filename[0:len(filename)-4:1]
    return open(Openfilelinks()[1] + filename + '_' + translate + '_' + service +'.txt', 'w', encoding="utf-8").write(text)


#Создадим функцию для сохранения отредактированного (DeepL.Write) текста в новый файл
def DeeplWrite_save(filename, text):
    filename = filename[0:len(filename) - 4:1]
    return open(Openfilelinks()[2] + filename + '_Ed' + '.txt', 'w', encoding="utf-8").write(text)


#Функция обработки текста
def operate(language, translate, service, input_files, web):
    for text_file in (Path(input_files).glob('*.txt')):  #редактируем каждый находящийся текстовый файл в папке по отдельности
        file = open(text_file, 'r', encoding="utf-8")
        translated_text = ''    #создаем переменную, которая будет хранить переведенный текст, обнуляем с каждым новым текстом
        if service == 'DeepL':    #провереям условие для выбора сервиса DeepL перевода
            translated_text = deepL.browser_translate(file, language, translate, web)    #запускаем функцию перевода и возвращаем переведенный текст и название файла для будущего сохранения
        else:    #пропишем перевод для всех остальных сервисов
            for line in file:    #переводим текст для каждой строки из файла по отдельности
                if line != '\n':    #проверяем условие, если непустая строка, то рабоатем с ней. Остальное пропускаем
                    translated_text = translated_text + text_translate(line, language, translate, service) + '\n'  # возвращаем перевод строки и записываем в переменную
        # Убираем пустые строки в переведенном тексте с помощью регулярного выражения
        clear_translated_text = '\n'.join(el.strip() for el in translated_text.split('\n') if el.strip())
        #Сохраним переведенный текст в новом файле
        trans_text_save(text_file.name, clear_translated_text, translate, service)








