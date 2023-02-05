# import tkinter
import tkinter
from tkinter import *    #Импортируем библиотеку для создания графического интерфейса
from tkinter.ttk import Combobox
import model
import deepL


#Функция для центрирования trkinter окна (не моя, но работает)
def center(win):
    """
    centers of tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

#Объявим функцию с настройкой графического интерфейса главного окна
def setup():
    # global choice_language, choice_translate, choice_service, choice_corrector, start_button, choice_input, choice_output
    global root, combo_language, combo_translate, combo_service, combo_corrector, combo_deeplwrite, start_button   # text_input, text_output, webdriver_address
    #глобальные переменнеые, которые будем использовать в фукнции нажатия кнопки
    # Создадим окно верхнего уровня
    root = Tk()
    root.title('A_Translator')    #введем тайтл
    root.geometry('400x300')    #установим размер окна
    root.config(bg='light blue')    #установим фон окна
    center(root)

    #Создадим объекты в окне (подписи + кнопка):
    text_language = Label(root, width=6, font='Calibri 17', text='Язык:', bg='light blue')
    text_translate = Label(root, width=8, font='Calibri 17', text='Перевод:', bg='light blue')
    text_service = Label(root, width=7, font='Calibri 17', text='Сервис:', bg='light blue')
    text_corrector = Label(root, width=10, font='Calibri 17', text='Корректор:', bg='light blue')
    text_input_label = Label(root, width=9, font='Calibri 12', text='Input files:', bg='light blue')
    text_output_label = Label(root, width=9, font='Calibri 12', text='Output files:', bg='light blue')
    webdriverfiles_label = Label(root, width=12, font='Calibri 12', text='WebDriver files:', bg='light blue')
    deeplwrite_label = Label(root, width=10, font='Calibri 17', text='DeepL.Write:', bg='light blue')
    start_button = Button(root, font=('Calibri', 14), text='Поехали!', width=20, bg='light grey')
    options_button = Button(root, font=('Calibri', 10), text='Настройки', width=20, bg='light grey')

    #Создадим менюшки для ввода текста ввода/вывода текстовых файлов
    #Создадим переменнеы. котореы будут хранить адерса папок ввода/вывода по умолчанию. Используем эти адреса в программе по умолчанию
    # choice_input = StringVar(root)
    # choice_output = StringVar(root)
    # text_input = Entry(root, background='white', justify=LEFT, width=51, textvariable=choice_input)
    # text_output = Entry(root, background='white', justify=LEFT, width=51, textvariable=choice_output)
    text_input = Entry(root, background='white', justify=LEFT, width=51)
    text_output = Entry(root, background='white', justify=LEFT, width=51)
    webdriver_address = Entry(root, background='white', justify=LEFT, width=51)

    # прочитаем файл, чтобы узнать расположение папок для текстовых файлов
    # text_input.insert(0, 'D:\Translated texts\Input files')    #Используем этот адрес по умолчанию (место расположения исходных текстов) (ПК)
    # text_output.insert(0, 'D:\Translated texts\Output files')    #Используем этот адрес по умолчанию (место, куда выкладываем переработанные тексты) (ПК)
    # webdriver_address.insert(0, '')    #Используем этот адрес по умолчанию (место, куда выкладываем переработанные тексты) (ПК)
    # text_input.insert(0, '/media/andrew/75A74AA74301978F/PycharmProjects/ATranslator/Input files/')  # Используем этот адрес по умолчанию (место расположения исходных текстов) (Ноут)
    # text_output.insert(0, '/media/andrew/75A74AA74301978F/PycharmProjects/ATranslator/Output files/')  # Используем этот адрес по умолчанию (место, куда выкладываем переработанные тексты) (Ноут)
    text_input.insert(0, model.Openfilelinks()[0]) # Используем этот адрес по умолчанию (место расположения исходных текстов) (Ноут)
    text_output.insert(0, model.Openfilelinks()[1]) # Используем этот адрес по умолчанию (место, куда выкладываем переработанные тексты) (Ноут)
    webdriver_address.insert(0, model.Openfilelinks()[2])   # Используем этот адрес по умолчанию (место, куда выкладываем переработанные тексты) (Ноут)

    # Создадим списки (выпадающие меню):
    #Сперва создадим переменные, которые будут хранить зачения выбора пользователя перед запуском обработки текста
    # choice_language = StringVar(root)    #переменная, которая будет хранить значение исходного языка после выбора пользователя из выпадающего меню
    # choice_translate = StringVar(root)    #переменная, которая будет хранить значение язфка перевода после выбора пользователя из выпадающего меню
    # choice_service = StringVar(root)    #переменная, которая будет хранить значение сервиса перевода после выбора пользователя из выпадающего меню
    # choice_corrector = StringVar(root)    #переменная, которая будет хранить значение корректора после выбора пользователя из выпадающего меню
    #Создадим списки выбора из выпадающих меню
    language_values = ('ru', 'en', 'de', 'fr', 'it', 'es', 'pt', 'ja')
    translate_values = ('en', 'ru', 'de', 'fr', 'it', 'es', 'pt', 'ja')
    service_values = ('DeepL', 'Microsoft','Google', 'Reverso', 'TranslateCom', 'Yandex', 'Multi')
    corrector_values = ('', 'en-US', 'en-GB', 'ru', 'de-DE', 'it', 'es', 'pt', 'ja')
    deeplwrite_values = ('Нет', 'Да')
    #Создадим выпадающие меню
    #Меню исходного языка
    # combo_language = Combobox(root, textvariable=choice_language)
    combo_language = Combobox(root)
    combo_language['values'] = language_values   #Зададим значения языков исходного текста
    combo_language.current(0)    #Устанавливаем по умолчанию первое значение из списка
    #Меню языка перевода
    # combo_translate = Combobox(root, textvariable=choice_translate)
    combo_translate = Combobox(root)
    combo_translate['values'] = translate_values    #Зададим значения языкоа для перевода
    combo_translate.current(0)  # Устанавливаем по умолчанию первое значение из списка
    #Меню сервиса перевода
    # combo_service = Combobox(root, textvariable=choice_service)
    combo_service = Combobox(root)
    combo_service['values'] = service_values    #Зададим значения сервисов для перевода
    combo_service.current(0)  # Устанавливаем по умолчанию первое значение из списка
    # Меню сервиса  DeepL.Write
    combo_deeplwrite = Combobox(root)
    combo_deeplwrite['values'] = deeplwrite_values    #Зададим значения сервисов для перевода
    combo_deeplwrite.current(0)  # Устанавливаем по умолчанию первое значение из списка
    # Меню языка корректора
    # combo_corrector = Combobox(root, textvariable=choice_corrector)
    combo_corrector = Combobox(root)
    combo_corrector['values'] = corrector_values    #Зададим значения языка для грамматической/орфографической проверки
    combo_corrector.current(0)  #Устанавливаем по умолчанию первое значение из списка

    #2-й вариант размещения виджетов
    # размещаем вводнеы данные
    # text_input_label.grid(row=0, column=0, pady=0, padx=16, sticky=W)
    # text_input.grid(row=1, padx=20, columnspan=2)
    # text_output_label.grid(row=2, column=0, pady=0, padx=21, sticky=W)
    # text_output.grid(row=3, padx=20, columnspan=2)
    # webdriverfiles_label.grid(row=4, column=0, pady=0, padx=21, sticky=W)
    # webdriver_address.grid(row=5, padx=20, columnspan=2)
    # размещаем разделяющую линию
    line = Canvas(root, width=300, height=30, bg='light blue', highlightthickness=0)
    line.create_line(5, 15, 295, 15, fill='black', width=2)
    line.grid(row=0, padx=0, columnspan=2)
    # размещаем выбор сервисов и кнопку
    text_language.grid(row=1, column=0, pady=0, padx=16, sticky=E)
    combo_language.grid(row=1, column=1, pady=0, padx=10, sticky=W)
    text_translate.grid(row=2, column=0, pady=0, padx=22, sticky=E)
    combo_translate.grid(row=2, column=1, pady=0, padx=10, sticky=W)
    text_service.grid(row=3, column=0, pady=0, padx=20, sticky=E)
    combo_service.grid(row=3, column=1, pady=0, padx=10, sticky=W)
    deeplwrite_label.grid(row=4, column=0, pady=0, padx=27, sticky=E)
    combo_deeplwrite.grid(row=4, column=1, pady=0, padx=10, sticky=W)
    text_corrector.grid(row=5, column=0, pady=0, padx=20, sticky=E)
    combo_corrector.grid(row=5, column=1, pady=0, padx=10, sticky=W)
    # размещаем разделяющую линию
    line = Canvas(root, width=300, height=30, bg='light blue', highlightthickness=0)
    line.create_line(5, 15, 295, 15, fill='black', width=2)
    line.grid(row=6, padx=0, columnspan=2)
    # размещаем кнопки
    start_button.grid(row=7, columnspan=2, pady=0)
    options_button.grid(row=8, columnspan=2, pady=0, padx=0)


    # Содадим взаимодействие с виджетами
    combo_language.bind("<<ComboboxSelected>>", menu_handler)
    combo_translate.bind("<<ComboboxSelected>>", menu_handler)
    combo_service.bind("<<ComboboxSelected>>", menu_handler)
    combo_corrector.bind("<<ComboboxSelected>>", menu_handler)
    start_button.bind('<Button-1>', start_handler)  # связываем событие (нажатие Button-1 [левая кнопка мышки]) и функцию start_handler
    options_button.bind('<Button-1>', options_handler)  # связываем событие (нажатие Button-1 [левая кнопка мышки]) и функцию options_handler


#Обработчки для менюшек (влияет на подпись кнопки и показывает выбор параметров перевода)
def menu_handler(event):
    global start_button
    start_button.config(text='Поехали!')

#Обработчик для кнопки start_button
def start_handler(event):
    # global combo_language, combo_translate, combo_service, combo_corrector, start_button # text_input, text_output, webdriver_address
    # global choice_language, choice_translate, choice_service, choice_corrector, start_button, choice_input, choice_output
    #Возвратим значения из выпадающих меню и присвоим их соответствующим переменным
    start_button.config(text='В процессе...')
    # input_files_selection = model.Openfilelinks()[0]
    # output_files_selection = model.Openfilelinks()[1]
    # language_selection = combo_language.get()
    # translate_selection = combo_translate.get()
    # service_selection = combo_service.get()
    # corrector_selection = combo_corrector.get()
    # # сохраним в файл пути для вводных значений для будущего использования (input, output and webdriver links)
    # new_FileLinks = ['Input files:', input_files_selection, 'Output files:', output_files_selection, 'WebDriver:', webdriver_selection, 'Output DeepL edited files:', '/media/andrew/75A74AA74301978F/PycharmProjects/ATranslator/Output files/Edited/']
    # with open('FileLinks.txt', 'w') as file:
    #     file.writelines("%s\n" % line for line in new_FileLinks)
    # input_files_selection = choice_input.get()
    # output_files_selection = choice_output.get()
    # language_selection = choice_language.get()
    # translate_selection = choice_translate.get()
    # service_selection = choice_service.get()
    # corrector_selection = choice_corrector.get()
    if combo_deeplwrite.get() == 'Нет':
        model.operate(combo_language.get(), combo_translate.get(), combo_service.get(), combo_corrector.get(), model.Openfilelinks()[0], model.Openfilelinks()[1])    # Запускаем функцию перевода текстов
    else:
        deepL.deepl_write()    # Запускаем функцию редактирования текста с помощью DeepL.Write
    start_button.config(text='Готово!')

#Обработчик для кнопки options_button
def options_handler(event):
    global options_window, text_input, text_output, text_deeplwrite, webdriverfiles
    # Создадим окно настроек и расположим его по центру
    options_window = tkinter.Toplevel(root)
    options_window.title('Настройки')
    options_window.geometry('400x300')
    options_window.config(bg='light blue')
    center(options_window)
    options_window.grab_set()
    # Создадим и добавим виджеты в окно для настроек
    text_input_label = Label(options_window, width=12, font='Calibri 12', text='Input files:', bg='light blue')
    text_output_label = Label(options_window, width=12, font='Calibri 12', text='Output files:', bg='light blue')
    text_deeplwrite_label = Label(options_window, width=14, font='Calibri 12', text='DeepL.Write files:', bg='light blue')
    webdriverfiles_label = Label(options_window, width=14, font='Calibri 12', text='WebDriver files:', bg='light blue')
    webdriver_label = Label(options_window, width=10, font='Calibri 12', text='WebDriver:', bg='light blue')
    text_input = Entry(options_window, background='white', justify=LEFT, width=44)
    text_output = Entry(options_window, background='white', justify=LEFT, width=44)
    text_deeplwrite = Entry(options_window, background='white', justify=LEFT, width=44)
    webdriverfiles = Entry(options_window, background='white', justify=LEFT, width=44)
    save_button = Button(options_window, font=('Calibri', 14), text='Сохранить', width=14, bg='light grey')
    # Создадим выпадающие меню
    webdriver_values = ('Chrome', 'Firefox')
    combo_webdriver = Combobox(options_window)
    combo_webdriver['values'] = webdriver_values  # Зададим значения для выбора
    combo_webdriver.current(0)  # Устанавливаем по умолчанию первое значение из списка
    # Разместим виджеты в окне
    text_input_label.grid(row=0, column=0, pady=0, padx=0, sticky=W)
    text_input.grid(row=1, padx=0, columnspan=2)
    text_output_label.grid(row=2, column=0, pady=0, padx=7, sticky=W)
    text_output.grid(row=3, padx=20, columnspan=2)
    text_deeplwrite_label.grid(row=4, column=0, pady=0, padx=20, sticky=W)
    text_deeplwrite.grid(row=5, padx=20, columnspan=2)
        # размещаем разделяющую линию
    line = Canvas(options_window, width=300, height=25, bg='light blue', highlightthickness=0)
    line.create_line(5, 15, 295, 15, fill='black', width=2)
    line.grid(row=6, padx=0, columnspan=2)
        # размещаем виджеты для вебдрайвера и кнопки сохранения
    webdriverfiles_label.grid(row=7, column=0, pady=0, padx=15, sticky=W)
    webdriverfiles.grid(row=8, padx=20, columnspan=2)
    webdriver_label.grid(row=9, column=0, pady=5, padx=0, sticky=E)
    combo_webdriver.grid(row=9, column=1, pady=0, padx=20, sticky=W)
    save_button.grid(row=10, columnspan=2, pady=10)
    save_button.bind('<Button-1>', save_handler)   # связываем обработчик с кнопкой
    # Загрузим располодение файлов из файла FileLinks.txt
    text_input.insert(0, model.Openfilelinks()[0]) # Используем этот адрес по умолчанию (место расположения исходных текстов)
    text_output.insert(0, model.Openfilelinks()[1]) # Используем этот адрес по умолчанию (место, куда выкладываем переведенные тексты)
    text_deeplwrite.insert(0, model.Openfilelinks()[2])  # Используем этот адрес по умолчанию (место, куда выкладываем отредактированные DeepL.Write тексты)
    webdriverfiles.insert(0, model.Openfilelinks()[3])   # Используем этот адрес по умолчанию (место, где нахолится вебдрайвер)

# обработчик для кнопки save_button
def save_handler(event):
    # сохраним в FileLinks.txt вводнные данные (input, output, deepl.write and webdriver addresses)
    new_FileLinks = ['Input files:', text_input.get(), 'Output files:', text_output.get(), 'Output DeepL edited files:', text_deeplwrite.get(), 'WebDriver:', webdriverfiles.get()]
    with open('FileLinks.txt', 'w') as file:
        file.writelines("%s\n" % line for line in new_FileLinks)
    options_window.destroy()
    pass


if __name__ == '__main__':
    setup()    #запускаем графический интерфейс + Конструктор
    mainloop()  #передаем управление модулю Tkinter, позволяя ему обрабатывать нажатия и другие действия пользователя