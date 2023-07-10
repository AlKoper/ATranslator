from pathlib import Path    #импортируем pathlib дял удобства обработки всех файлов в папке
from time import sleep    #для прерывания, чтобу успеть всё перевести/отредактировать
import selenium.webdriver
#Импортируем пакеты для парсинга
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import model


# Создадим функцию, которая парсит перевод
def browser_translate(file, language, translate, web):
    Options().headless = False    # настройки браузера - показ браузера (при False будет показывать)
    if web == 'Chrome':    # проверяем, каквое вебдрайвер будет использовать
        browser = webdriver.Chrome(executable_path=model.Openfilelinks()[3])  # инициируем драйвер браузера Chrome
    elif web == 'Firefox':
        browser = webdriver.Firefox(executable_path=model.Openfilelinks()[3])  # инициируем драйвер браузера Firefox
    translate_url = 'https://www.deepl.com/translator#' + language + '/' + translate + '/'  # Создаем адрем перевода, который зависит от исходного языка и языка перевода
    browser.get(translate_url)  # открываем сайт с переводчиком
    sleep(5)  # спим 5 секунд, чтобы прогрузилась страница

    translated_text = ''  # создаем переменную, которая будет хранить переведенный текст
    for line in file:    #переводим текст для каждой строки из файла
        if line != '\n':    #проверяем условие, если непустая строка, то работаем с ней. Остальное пропускаем
            browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[1]/div[3]/div[2]/d-textarea/div').click()
            browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[1]/div[3]/div[2]/d-textarea/div').send_keys(line)
            sleep(5)  # спим 5 секунд, чтобы сервис перевёл текст, с параметром можно поэксперементировать
            #Выгружаем перевод
            # html = browser.page_source
            # soup = BeautifulSoup(html, 'lxml')
            # translation = soup.find('div', id='target-dummydiv')
            # translated_text = translated_text + translation.text    #Записываем перевод в переменную
            translated_text = translated_text + browser.find_element(By.XPATH, '/html/body/div[3]/main/div[5]/div[1]/div[2]/section[2]/div[3]/div[1]/d-textarea').text +'\n'   #Записываем перевод в переменную
            browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[1]/div[3]/div[2]/d-textarea/div').clear()    #очистим поле для следующей строки
    browser.close()
    browser.quit()
    return translated_text


# Создадим функцию, которая редактирует исходный текст на DeepL.Write
def deepl_write(web):
    # запустим браузер и откроуем нужную страницу
    Options().headless = False  # настройки браузера - показ браузера (при False будет показывать)
    if web == 'Chrome':
        browser = webdriver.Chrome(executable_path=model.Openfilelinks()[3])  # инициируем драйвер браузера Chrome
    elif web == 'Firefox':
        browser = webdriver.Firefox(executable_path=model.Openfilelinks()[3])  # инициируем драйвер браузера Firefox
    browser = webdriver.Chrome(executable_path=model.Openfilelinks()[3])  # инициируем драйвер браузера Chrome (Ноут)
    write_url = 'https://www.deepl.com/write'  # новый проект от разработчиков DeepL, которая позволяет редактировать и исправлять текст
    browser.get(write_url)  # открываем сайт с переводчиком
    sleep(5)  # спим 5 секунд, чтобы прогрузилась страница
    browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[1]/div[3]/div[2]/d-textarea/div').clear()  # чистим окно для вставки переведенного текста

    # будем редактровать каждый файл в папке, находящийся по адресу Output files
    for text_file in (Path(model.Openfilelinks()[1]).glob('*.txt')):  #редактируем каждый находящийся текстовый файл в папке по отдельности
        file = open(text_file, 'r', encoding="utf-8")
        # работаем с открывшимся файлом
        writed_text = ''  # создаем переменную, которая будет хранить отредактированный текст
        for line in file:    #переводим текст для каждой строки из файла
            if line != '\n':    #проверяем условие, если непустая строка, то работаем с ней. Остальное пропускаем
                browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[1]/div[3]/div[2]/d-textarea/div').clear()
                browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[1]/div[3]/div[2]/d-textarea/div').send_keys(line)  # вставляем переведенный текст
                sleep(5)    # спим 5 секунд, чтобы сервис отредактировал текст, с параметром можно поэксперементировать
                # html = browser.page_source
                # soup = BeautifulSoup(html, 'lxml')
                # edited_text = soup.find('div', id='target-dummydiv')
                writed_text = writed_text + browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[2]/div[3]/div[1]/d-textarea/div').text + '\n'  # Записываем новую струку в отредактированный текст
                browser.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div/div[2]/section[1]/div[3]/div[2]/d-textarea/div').clear()    #очистим поле для следующей строки
        writed_text_clear = '\n'.join(el.strip() for el in writed_text.split('\n') if el.strip())    #Убираем пустые строки в отредактируемом тексте с помощью регулярного выражения
        model.DeeplWrite_save(text_file.name, writed_text_clear)
    browser.close()
    browser.quit()
