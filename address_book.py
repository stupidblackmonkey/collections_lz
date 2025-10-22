# Создаем словарь с людьми и их адресами
lyudi = { "вадимка": "ул. Ленина, д. 10" , "Вовчик": "пр. Победы, д. 25" , "димка": "ул. Центральная, д. 5"}
while True:
    print("1 - Просмотреть все записи")
    print("2 - Изменить адрес")
    print("3 - Удалить запись")
    
    vibor = input("Выберите действие (1-3): ")
    
    if vibor == "1":
        # Просмотр всех записей
        if not lyudi:
            print("Словарь пуст")
        else:
            # Перебираем все имена и сразу выводим имя и адрес
            for name in lyudi:
                print(name, ":", lyudi[name])
    
    elif vibor == "2":
        # Изменение адреса
        name = input("Введите имя человека: ")
        if name in lyudi:
            novi_adres = input("Введите новый адрес: ")
            lyudi[name] = novi_adres
            print("Адрес для", name, "изменен")
        else:
            print("Человек не найден")
    
    elif vibor == "3":
        # Удаление записи
        name = input("Введите имя для удаления: ")
        if name in lyudi:
            del lyudi[name]
            print("Запись", name, "удалена")
        else:
            print("Человек не найден")
    
    elif vibor > "3":
       print("Неверный выбор. Попробуйте снова.")
    
