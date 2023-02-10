# импортируем необходимые пакеты для перевода
# используем несколько переводчиков одновременно, чтобы увеличить шансы на получение ответа
from translatepy import Translator
# импортируем каждый переводчик отдельно, чтобы испольовать его при выборе конкретного сервиса
from translatepy.translators.google import GoogleTranslate
from translatepy.translators.yandex import YandexTranslate
from translatepy.translators.microsoft import MicrosoftTranslate
# from translatepy.translators.deepl import DeeplTranslate
from translatepy.translators.reverso import ReversoTranslate
from translatepy.translators.translatecom import TranslateComTranslate
#Импортируем DeepL для первода в этом сервисе
import deepL
from pathlib import Path  # импортируем pathlib дял удобства обработки всех файлов в папке
import language_tool_python  # импортируем пакет для проверки грамматики/орфографии и внесения корректировок

#Создадим функцию перевода
def text_translate(text, sour, dest, service):    #sour - язык исходного текста, dest - язык перевода
    if service == 'Multi':
        Translate_service = Translator()   #Translate_service переменная, отвечающая за сервис перевода
    elif service == 'Google':
        Translate_service = GoogleTranslate()
    elif service == 'Yandex':
        Translate_service = YandexTranslate()
    elif service == 'Microsoft':
        Translate_service = MicrosoftTranslate()
    # elif service == 'DeepL':
    #     Translate_service = DeeplTranslate()
    elif service == 'Reverso':
        Translate_service = ReversoTranslate()
    elif service == 'TranslateCom':
        Translate_service = TranslateComTranslate()
    result = str(Translate_service.translate(text, destination_language=dest, source_language=sour))
    Translate_service.clean_cache()
    return result

#Создадим функцию проверки орфографии и грамматики переведенного текста
def text_correct(text, corrector):
    tool = language_tool_python.LanguageTool(corrector)
    corrected_text = tool.correct(text)
    return corrected_text


# Создадим функцию открытия и чтения адресов папок из файла
def Openfilelinks():
    with open('FileLinks.txt', 'r') as file:
        lines = file.readlines()
    return lines[1].replace('\n', ''), lines[3].replace('\n', ''), lines[5].replace('\n', ''), lines[7].replace('\n', ''), lines[8].replace('\n', '')


#Создадим функцию для сохранения переведенного текста в новый файл
def ed_text_save(filename, text, translate, service, output_files):
    filename = filename[0:len(filename)-4:1]
    # output_files = output_files + '/'
    return open(output_files + filename + '_' + translate + '_' + service +'.txt', 'w', encoding="utf-8").write(text)


#Создадим функцию для сохранения отредактированного (DeepL.Write) текста в новый файл
def DeeplWrite_save(filename, text):
    filename = filename[0:len(filename) - 4:1]
    # output_files = Openfilelinks()[3]
    return open(Openfilelinks()[2] + filename + '_Ed' + '.txt', 'w', encoding="utf-8").write(text)


#Функция обработки текста
def operate(language, translate, service, corrector, input_files, output_files, web):
    for text_file in (Path(input_files).glob('*.txt')):  #редактируем каждый находящийся текстовый файл в папке по отдельности
        file = open(text_file, 'r', encoding="utf-8")
        translated_text = ''    #создаем переменную, которая будет хранить переведенный текст, обнуляем с каждым новым текстом
        if service == 'DeepL':    #провереям условие для выбора сервиса перевода
            translated_text = deepL.browser_translate(file, language, translate, web)    #запускаем функцию перевода и возвращаем переведенный текст и название файла для будущего сохранения
        else:    #пропишем перевод для всех остальных сервисов
            for line in file:    #переводим текст для каждой строки из файла
                if line == '\n':    #проверяем условие, если пустая строка, то записываем её в translated_text и идем дальше
                    translated_text = translated_text + '\n'
                else:
                    translated_text = translated_text + text_translate(line, language, translate, service) + '\n'  #возвращаем перевод строки и записываем в переменную
        #Убираем пустые строки в переведенном тексте с помощью регулярного выражения
        clear_translated_text = '\n'.join(el.strip() for el in translated_text.split('\n') if el.strip())
        #Проверяем нужен ли нам корректор. Если да, то запускаем функцию с соотвествующим значением
        if corrector == '':
            corrected_text = clear_translated_text
        else:
            corrected_text = text_correct(translated_text, corrector)    #возвращаем откорректированный (орфография+грамматика) текст и записываем в переменную
        #Сохраним переведенный и откорректированный текст в новом файле
        ed_text_save(text_file.name, corrected_text, translate, service, output_files)








