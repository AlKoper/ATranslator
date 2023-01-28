from tkinter import *    #Импортируем библиотеку для создания графического интерфейса
from tkinter.ttk import Combobox
import model


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

#Объявим функцию с настройкой графического интерфейса
def setup():
    # global choice_language, choice_translate, choice_service, choice_corrector, start_button, choice_input, choice_output
    global combo_language, combo_translate, combo_service, combo_corrector, start_button, text_input, text_output
    #глобальные переменнеые, которые будем использовать в фукнции нажатия кнопки
    # Создадим окно верхнего уровня
    root = Tk()
    root.title('A_Translator')    #введем тайтл
    root.geometry('350x310')    #установим размер окна
    root.config(bg='light blue')    #установим фон окна
    center(root)

    #Создадим объекты в окне (подписи + кнопка):
    text_language = Label(root, width=6, font='Calibri 17', text='Язык:', bg='light blue')
    text_translate = Label(root, width=8, font='Calibri 17', text='Перевод:', bg='light blue')
    text_service = Label(root, width=7, font='Calibri 17', text='Сервис:', bg='light blue')
    text_corrector = Label(root, width=10, font='Calibri 17', text='Корректор:', bg='light blue')
    text_input_label = Label(root, width=9, font='Calibri 12', text='Input files:', bg='light blue')
    text_output_label = Label(root, width=9, font='Calibri 12', text='Output files:', bg='light blue')
    start_button = Button(root, font=('Calibri', 14), text='Поехали!', width=20, bg='light grey')

    #Создадим менюшки для ввода текста ввода/вывода текстовых файлов
    #Создадим переменнеы. котореы будут хранить адерса папок ввода/вывода по умолчанию. Используем эти адреса в программе по умолчанию
    # choice_input = StringVar(root)
    # choice_output = StringVar(root)
    # text_input = Entry(root, background='white', justify=LEFT, width=51, textvariable=choice_input)
    # text_output = Entry(root, background='white', justify=LEFT, width=51, textvariable=choice_output)
    text_input = Entry(root, background='white', justify=LEFT, width=51)
    text_output = Entry(root, background='white', justify=LEFT, width=51)

    # text_input.insert(0, 'D:\Translated texts\Input files')    #Используем этот адрес по умолчанию (место расположения исходных текстов) (ПК)
    # text_output.insert(0, 'D:\Translated texts\Output files')    #Используем этот адрес по умолчанию (место, куда выкладываем переработанные тексты) (ПК)
    text_input.insert(0, '/media/andrew/75A74AA74301978F/PycharmProjects/ATranslator/Input files/')  # Используем этот адрес по умолчанию (место расположения исходных текстов) (Ноут)
    text_output.insert(0, '/media/andrew/75A74AA74301978F/PycharmProjects/ATranslator/Output files/')  # Используем этот адрес по умолчанию (место, куда выкладываем переработанные тексты) (Ноут)

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
    #Меню языка корректора
    # combo_corrector = Combobox(root, textvariable=choice_corrector)
    combo_corrector = Combobox(root)
    combo_corrector['values'] = corrector_values    #Зададим значения языка для грамматической/орфографической проверки
    combo_corrector.current(0)  #Устанавливаем по умолчанию первое значение из списка

    #Разместим виджеты в рут окне согласно разработанного плана, используя для этого менеджер компановки:
      # 1-й вариант размещения виджетов
    # text_input_label.grid(row=0, column=0,pady=0, padx=20, sticky=W)
    # text_input.grid(row=1, columnspan=2)
    # text_output_label.grid(row=2, column=0, pady=0, padx=24, sticky=W)
    # text_output.grid(row=3, columnspan=2)

    # text_language.grid(row=5, column=0, pady=10, padx=10, sticky=W)
    # combo_language.grid(row=6, column=0, pady=10, padx=20, sticky=W)
    # text_translate.grid(row=5, column=1, pady=10, padx=20, sticky=E)
    # combo_translate.grid(row=6, column=1, pady=10, padx=20, sticky=E)
    # text_service.grid(row=7, column=0, pady=10, padx=20, sticky=W)
    # combo_service.grid(row=8, column=0, pady=10, padx=20, sticky=W)
    # text_corrector.grid(row=7, column=1, pady=10, padx=20, sticky=E)
    # combo_corrector.grid(row=8, column=1, pady=10, padx=20, sticky=E)
    # start_button.grid(row=9, columnspan=2, pady=10)

      #2-й вариант размещения виджетов
    text_input_label.grid(row=0, column=0, pady=0, padx=16, sticky=W)
    text_input.grid(row=1, padx=20, columnspan=2)
    text_output_label.grid(row=2, column=0, pady=0, padx=20, sticky=W)
    text_output.grid(row=3, padx=20, columnspan=2)
    text_language.grid(row=4, column=0, pady=0, padx=16, sticky=E)
    combo_language.grid(row=4, column=1, pady=0, padx=10, sticky=W)
    text_translate.grid(row=5, column=0, pady=0, padx=22, sticky=E)
    combo_translate.grid(row=5, column=1, pady=0, padx=10, sticky=W)
    text_service.grid(row=6, column=0, pady=0, padx=20, sticky=E)
    combo_service.grid(row=6, column=1, pady=0, padx=10, sticky=W)
    text_corrector.grid(row=7, column=0, pady=0, padx=20, sticky=E)
    combo_corrector.grid(row=7, column=1, pady=0, padx=10, sticky=W)
    start_button.grid(row=8, columnspan=2, pady=20)

    # Содадим взаимодействие с виджетами
    combo_language.bind("<<ComboboxSelected>>", menu_handler)
    combo_translate.bind("<<ComboboxSelected>>", menu_handler)
    combo_service.bind("<<ComboboxSelected>>", menu_handler)
    combo_corrector.bind("<<ComboboxSelected>>", menu_handler)
    start_button.bind('<Button-1>', start_handler)  # связываем событие (нажатие Button-1 [левая кнопка мышки]) и функцию start_handler


#Обработчки для менюшек (влияет на подпись кнопки и показывает выбор параметров перевода)
def menu_handler(event):
    global start_button
    start_button.config(text='Поехали!')

#Обработчик для кнопки
def start_handler(event):
    global combo_language, combo_translate, combo_service, combo_corrector, start_button, text_input, text_output
    # global choice_language, choice_translate, choice_service, choice_corrector, start_button, choice_input, choice_output
    #Возвратим значения из выпадающих меню и присвоим их соответствующим переменным
    start_button.config(text='В процессе...')
    input_files_selection = text_input.get()
    output_files_selection = text_output.get()

    language_selection = combo_language.get()
    translate_selection = combo_translate.get()
    service_selection = combo_service.get()
    corrector_selection = combo_corrector.get()


    # input_files_selection = choice_input.get()
    # output_files_selection = choice_output.get()
    # language_selection = choice_language.get()
    # translate_selection = choice_translate.get()
    # service_selection = choice_service.get()
    # corrector_selection = choice_corrector.get()
    #вызываем функцию для обработки текста с вводными из выпадающих мню
    model.operate(language_selection, translate_selection, service_selection, corrector_selection, input_files_selection, output_files_selection)
    start_button.config(text='Готово!')


if __name__ == '__main__':
    setup()    #запускаем графический интерфейс + Конструктор
    mainloop()  #передаем управление модулю Tkinter, позволяя ему обрабатывать нажатия и другие действия пользователя