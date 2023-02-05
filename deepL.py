#Добавляем библиотеки, которые будем использовать
from pathlib import Path    #импортируем pathlib дял удобства обработки всех файлов в папке
from time import sleep    #для перерывами между переводов, чтобу успеть всё перевести
import os.path
#Импортируем пакеты для парсинга
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import model

#Создадим функцию запуска браузера
def browser_launch(language, translate):
    global browser
    options = Options()    #здесь будут содержаться настройки браузера
    options.headless = False    #отключу показ браузера (при False будет показывать)
    # browser = webdriver.Firefox(options=options, service=Service(log_path=os.devnull, executable_path='geckodriver.exe'))    #инициируем драйвер браузера Firefox (ПК)
    # browser = webdriver.Chrome(executable_path='/media/andrew/75A74AA74301978F/PycharmProjects/ATranslator/geckodriver/chromedriver')  # инициируем драйвер браузера Chrome (Ноут)
    browser = webdriver.Chrome(executable_path=model.Openfilelinks()[3])  # инициируем драйвер браузера Chrome (Ноут)
    translate_url = 'https://www.deepl.com/translator#' + language + '/' + translate + '/'    #Создаем адрем перевода, который зависит от исходного языка и языка перевода
    browser.get(translate_url)    #открываем сайт с переводчиком
    sleep(8)  # спим 8 секунд, чтобы прогрузилась страница

    # browser.execute_script("window.open('');")    #создаем еще одну вкладку и переключаемся на неё
    # browser.switch_to.window(browser.window_handles[1])    #продолжаем верхний пункт
    # browser.get(write_url)    #открываем сайт с редактированием текста в новой вкладке
    # browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[1]/div[3]/div[2]/d-textarea/div').clear()  # чистим окно для вставки переведенного текста
    # sleep(3)  # спим 5 секунд, чтобы прогрузилась страница



# Создадим функцию, которая парсит перевод - наша основная функция
def browser_translate(file):
    global browser
    translated_text = ''  # создаем переменную, которая будет хранить переведенный текст
    for line in file:    #переводим текст для каждой строки из файла
        if line == '\n':    #проверяем условие, если пустая строка, то записываем её в translated_text и идем дальше
            translated_text = translated_text + '\n'
        else:
            browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[1]/div[3]/div[2]/d-textarea/div').click()
            browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[1]/div[3]/div[2]/d-textarea/div').send_keys(line)
            sleep(5)  # спим 5 секунд, чтобы сервис перевёл текст, с параметром можно поэксперементировать
            #Выгружаем перевод
            html = browser.page_source
            soup = BeautifulSoup(html, 'lxml')
            translation = soup.find('div', id='target-dummydiv')
            translated_text = translated_text + translation.text    #Записываем перевод в переменную
            print(translation.text)
            browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[1]/div[3]/div[2]/d-textarea/div').clear()    #очистим поле для следующей строки
    return translated_text

# def browser_translate(file):
#     translated_text = ''  # создаем переменную, которая будет хранить переведенный текст
#     for line in file:    #переводим текст для каждой строки из файла
#         if line == '\n':    #проверяем условие, если пустая строка, то записываем её в translated_text и идем дальше
#             translated_text = translated_text + '\n'
#         else:
#             browser.switch_to.window(browser.window_handles[0])  # переключаемся на вкалдку с переводчиком
#             browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[1]/div[3]/div[2]/textarea').send_keys(line)
#             sleep(5)  # спим 5 секунд, чтобы сервис перевёл текст, с параметром можно поэксперементировать
#             #Выгружаем перевод
#             html = browser.page_source
#             soup = BeautifulSoup(html, 'lxml')
#             translation = soup.find('div', id='target-dummydiv')
#             browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[1]/div[3]/div[2]/textarea').clear()    #очистим поле для следующей строки
#
#             browser.switch_to.window(browser.window_handles[1])  # переключаемся на вкладку с редактированием текста
#             browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[1]/div[3]/div[2]/d-textarea/div').send_keys(translation.text)    #вставляем переведенный текст
#             sleep(5)    # спим 5 секунд, чтобы сервис отредактировал текст, с параметром можно поэксперементировать
#             html = browser.page_source
#             soup = BeautifulSoup(html, 'lxml')
#             edited_text = soup.find('div', id='target-dummydiv')
#             browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[1]/div[3]/div[2]/d-textarea/div').clear()  # чистим окно для вставки переведенного текста
#
#             translated_text = translated_text + edited_text.text     #Записываем новую струку в переведенный текст
#     return translated_text



# Создадим функцию, которая редактирует исходный текст на DeepL.Write
def deepl_write():
    # запустим браузер и откроуем нужную страницу
    options = Options()  # здесь будут содержаться настройки браузера
    options.headless = False  # включу показ браузера (при False будет показывать)
    browser = webdriver.Chrome(executable_path=model.Openfilelinks()[3])  # инициируем драйвер браузера Chrome (Ноут)
    write_url = 'https://www.deepl.com/write'  # новый проект от разработчиков DeepL, которая позволяет редактировать и исправлять текст
    browser.get(write_url)  # открываем сайт с переводчиком
    sleep(5)  # спим 5 секунд, чтобы прогрузилась страница
    browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[1]/div[3]/div[2]/d-textarea/div').clear()  # чистим окно для вставки переведенного текста

    # будем редактровать каждый файл в папке, находящийся по адресу input_files
    for text_file in (Path(model.Openfilelinks()[1]).glob('*.txt')):  #редактируем каждый находящийся текстовый файл в папке по отдельности
        file = open(text_file, 'r', encoding="utf-8")
        # работаем с открывшимся файлом
        writed_text = ''  # создаем переменную, которая будет хранить отредактированный текст
        for line in file:    #переводим текст для каждой строки из файла
            if line == '\n':    #проверяем условие, если пустая строка, то записываем её в translated_text и идем дальше
                writed_text = writed_text + '\n'
            else:
                browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[1]/div[3]/div[2]/d-textarea/div').clear()
                browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[1]/div[3]/div[2]/d-textarea/div').send_keys(line)  # вставляем переведенный текст
                sleep(5)    # спим 5 секунд, чтобы сервис отредактировал текст, с параметром можно поэксперементировать
                html = browser.page_source
                soup = BeautifulSoup(html, 'lxml')
                edited_text = soup.find('div', id='target-dummydiv')
                writed_text = writed_text + edited_text.text  # Записываем новую струку в отредактированный текст
                browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[1]/div[3]/div[2]/d-textarea/div').clear()    #очистим поле для следующей строки
        writed_text_clear = '\n'.join(el.strip() for el in writed_text.split('\n') if el.strip())    #Убираем пустые строки в отредактируемом тексте с помощью регулярного выражения
        model.DeeplWrite_save(text_file.name, writed_text_clear)
    return


def browser_close():
    global browser
    #Закрываем браузер
    browser.close()
    browser.quit()


# if __name__ == '__main__':
#     browser_launch('ru', 'en')
#     browser_translate('Привет! Меня зовут Андрей! Как тебя зовут? Откуда ты?')
#     browser_close()
