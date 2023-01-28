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


#Создадим функцию запуска браузера
def browser_launch(language, translate):
    global browser
    options = Options()    #здесь будут содержаться настройки браузера
    options.headless = False    #отключу показ браузера (при False будет показывать)
    # browser = webdriver.Firefox(options=options, service=Service(log_path=os.devnull, executable_path='geckodriver.exe'))    #инициируем драйвер браузера Firefox (ПК)
    browser = webdriver.Chrome(executable_path='/media/andrew/75A74AA74301978F/PycharmProjects/ATranslator/geckodriver/chromedriver')  # инициируем драйвер браузера Chrome (Ноут)
    translate_url = 'https://www.deepl.com/translator#' + language + '/' + translate + '/'    #Создаем адрем перевода, который зависит от исходного языка и языка перевода

    browser.get(translate_url)    #открываем сайт
    sleep(8)   #спим 8 секунд, чтобы прогрузилась страница


#Создадим функцию, которая парсит перевод - наша основная функция
def browser_translate(file):
    translated_text = ''  # создаем переменную, которая будет хранить переведенный текст
    for line in file:    #переводим текст для каждой строки из файла
        if line == '\n':    #проверяем условие, если пустая строка, то записываем её в translated_text и идем дальше
            translated_text = translated_text + '\n'
        else:
            browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[1]/div[3]/div[2]/textarea').send_keys(line)
            sleep(5)  # спим 5 секунд, чтобы сервис перевёл текст, с параметром можно поэксперементировать
            #Выгружаем перевод
            html = browser.page_source
            soup = BeautifulSoup(html, 'lxml')
            translation = soup.find('div', id='target-dummydiv')
            translated_text = translated_text + translation.text    #Записываем перевод в переменную
            browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[1]/div[3]/div[2]/textarea').clear()    #очистим поле для следующей строки
    return translated_text


def browser_close():
    global browser
    #Закрываем браузер
    browser.close()
    browser.quit()
