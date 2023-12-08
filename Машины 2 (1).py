#nazv_kharakteristic = ['Гос номер', 'Тип кузова', 'Цвет', 'Коробка передач', 'Год выпуска', 'Привод', 'Пробег', 'Тип двигателя', 'Объём двигателя', 'Мощность', 'Руль']
def menu():
    with open('spisok.txt', 'r', encoding="utf-8") as r:  # , encoding="utf-8"
        stroki = r.readlines()  # Строки
        new = [line for line in stroki if len(line) != 1]
    with open('spisok.txt', 'w', encoding="utf-8") as w:  # , encoding="utf-8"
        w.writelines(new)
    with open('spisok.txt', 'r', encoding="utf-8") as s:  # , encoding="utf-8"
        stroki = s.readlines()
        Q = len(stroki)  # Количество машин
        for x in stroki:
            if x[0] == '' or x[0] == ' ':
                Q -= 1
    number = [int(x) for x in range(1, Q + 1)]  # Порядковый номер машины
    print('\nСписок автомобилей:\n')
    print('     | Название авто              | Гос.номер')
    print('_____|____________________________|___________')
    vse_kharakteristic = []
    for w in range(0, Q):
        stroka_kharakteristic = []
        kharakteristic = []
        nazv_kharakteristic = []
        znach_kharakteristic = []
        # stroki[i].split(',')
        split = ''
        for x in stroki[w]:
            if x == ',':
                stroka_kharakteristic += [split]
                split = ''
            else:
                split += x
        stroka_kharakteristic += [split]
        for i in range(len(stroka_kharakteristic)):
            # stroka_kharakteristic[i].split('-')
            split = ''
            for x in stroka_kharakteristic[i]:
                if x == '-':
                    kharakteristic += [split]
                    split = ''
                else:
                    split += x
            kharakteristic += [split]
        for i in range(len(kharakteristic)):
            if (i % 2 == 0):
                nazv_kharakteristic += [kharakteristic[i]]
            else:
                znach_kharakteristic += [kharakteristic[i]]
        vse_kharakteristic += [[nazv_kharakteristic] + [znach_kharakteristic]]
        print(number[w], (3 - len(str(number[w]))) * ' ', '|', znach_kharakteristic[0],
              (25 - len(znach_kharakteristic[0])) * ' ', '|', znach_kharakteristic[1])
        print('_____|____________________________|___________')
    print('\nМеню навигации\n'
          '1)Для просмотра характеристик и модификации введите порядковый номер автомобиля\n'
          '2)Чтобы добавить автомобиль в список нажмите + \n'
          '3)Чтобы удалить автомобиль из списка нажмите -\n'
          '4)Чтобы сделать поиск по параметрам введите "поиск"\n')
    returnn = [vse_kharakteristic, stroki, Q, number]
    return returnn
def vvod():
    returnn = menu()
    Q = returnn[2]
    vvod1 = input()
    for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if (vvod1[0] == i):
            x = int(vvod1)
            if x not in range(1, Q+1):
                print('Вы ввели неверный номер автомобиля. Повторите ввод')
            else: kharakteristic(x)
        elif (vvod1 == '+'):
            dobavl()
        elif (vvod1 == '-'):
            delete()
        elif (vvod1 == 'поиск'):
            print("Введите параметр для поиска")
            pois = input()
            poisk(pois)
            
def kharakteristic(x):
    returnn = menu()
    vse_kharakteristic = returnn[0]
    stroki = returnn[1]
    Q = returnn[2]
    print(vse_kharakteristic)
    print(stroki)
    print(Q)
    flag1 =0
    while flag1 == 0:
        if x not in range(1, Q+1):
            print('Вы ввели неверный номер автомобиля. Повторите ввод')
        else:
            #'Гос номер', 'Тип кузова', 'Цвет', 'Коробка передач', 'Год выпуска', 'Привод', 'Пробег', 'Тип двигателя', 'Объём двигателя', 'Мощность', 'Руль'
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nХарактеристики автомобиля:\n')
            print('__________________________________________')
            nazv_kharakteristic = vse_kharakteristic[x-1][0]
            znach_kharakteristic = vse_kharakteristic[x-1][1]
            for i in range(len(nazv_kharakteristic)): #Вывод списка характеристик
                print(i+1, (2-len(str(i+1))) * ' ', '|',  nazv_kharakteristic[i], ((15 - len(str(nazv_kharakteristic[i]))) * ' '), '|', znach_kharakteristic[i], '\n____|' + (18  * '_') + '|__________________')
            print('\nЧтобы изменить характеристики автомобиля введите "изменить"')
            print('Чтобы вернуться назад к списку автомобилей введите "назад"')
            flag5 = 0
            while flag5 == 0:
                vvod2 = str(input())
                if vvod2 == 'назад' or vvod2 == 'Назад' or vvod2 == 'yfpfl' or vvod2 == 'Yfpfl':
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                    flag1 = 1
                    flag5 = 1
                elif vvod2 == 'изменить' or vvod2 == 'Изменить' or vvod2 == 'bpvtybnm' or vvod2 == 'Bpvtybnm':
                    izmen_nomer = int(input('Введите номер характеристики которую вы хотите изменить'))
                    if izmen_nomer in range(1, 12):
                        izmen = input('Введите изменённую характеристику')
                        znach_kharakteristic[izmen_nomer-1] = izmen
                        with open('spisok.txt', 'r', encoding="utf-8") as r:  # , encoding="utf-8"
                            stroki = r.readlines()
                            count = 1
                            with open('spisok.txt', 'w', encoding="utf-8") as w:  # , encoding="utf-8"
                                for line in stroki:
                                    if count != x:
                                        w.write(line)
                                    elif count == x:
                                        spis_khar = ''
                                        for y in range(0, len(nazv_kharakteristic)):
                                            spis_khar += nazv_kharakteristic[y] + '-' + znach_kharakteristic[y] + ','
                                        w.write(spis_khar[:-1] + '\n')
                                    count += 1
                        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nХарактеристики автомобиля успешно изменены\n')
                    flag5 = 1
                    vvod()
                else:
                    print('Вы ввели неверуню команду. Повторите ввод')
                    flag5 = 0
            vvod()
def dobavl():
    returnn = menu()
    Q = returnn[2]
      # ДОБАВЛЕНИЕ
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nДобавление автомобиля.')
    flag2 = 0
    while flag2 == 0:
        model = input('Ведите марку и модель автомобиля. Чтобы вернуться назад напишите "назад" \n')
        if model == 'назад' or model == 'Назад' or model == 'yfpfl' or model == 'Yfpfl':
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            vvod()
        elif model != 'назад' or model != 'Назад' or model != 'yfpfl' or model != 'Yfpfl':
            flag4 = 0
            nazv_kharakteristic = ['Название авто', 'Гос номер', 'Тип кузова', 'Цвет', 'Коробка передач', 'Год выпуска', 'Привод', 'Пробег', 'Тип двигателя', 'Объём двигателя', 'Мощность', 'Руль']
            dobavl_kharakteristic = []
            dobavl_kharakteristic += ['Название авто-' + model + ',']
            dobavl_kharakteristic += ['Гос номер-' + input('Введите гос номер') + ',']
            while flag4 == 0:
                yesno = str(input('Ввести дополнительные характеристики автомобиля?  (да / нет)'))
                if yesno == 'да' or yesno == 'Да' or yesno == 'lf' or yesno == 'Lf':
                    print('Если не хотите вводить какую-либо характеристику введите -')
                    for i in range(2, len(nazv_kharakteristic)):
                        if i != len(nazv_kharakteristic)-1:
                            dobavl_kharakteristic += [nazv_kharakteristic[i] + '-' + input(nazv_kharakteristic[i] + ' ') + ',']
                        elif i == len(nazv_kharakteristic)-1:
                            dobavl_kharakteristic += [nazv_kharakteristic[i] + '-' + input(nazv_kharakteristic[i]+ ' ')]
                    with open('spisok.txt', 'r', encoding="utf-8") as r:  # , encoding="utf-8"
                        stroki = r.readlines()
                        count = 1
                        with open('spisok.txt', 'w', encoding="utf-8") as w:  # , encoding="utf-8"
                            for line in stroki:
                                if count != Q + 1:
                                    w.write(line)
                                count += 1
                            w.write('\n')
                            for i in range(len(dobavl_kharakteristic)):
                                w.write(dobavl_kharakteristic[i])
                    print('Автомобиль успешно добавлен')
                    vvod()
                elif yesno == 'нет' or yesno == 'Нет' or yesno == 'ytn' or yesno == 'Ytn':
                    with open('spisok.txt', 'r', encoding="utf-8") as r:  # , encoding="utf-8"
                        stroki = r.readlines()
                        count = 1
                        with open('spisok.txt', 'w', encoding="utf-8") as w:  # , encoding="utf-8"
                            for line in stroki:
                                if count != Q + 1:
                                    w.write(line)
                                    count += 1
                            w.write('\n' + dobavl_kharakteristic[0] + dobavl_kharakteristic[1] + ' - , - , - , - , - , - , - , - , - , - ')
                    with open('spisok.txt', 'r', encoding="utf-8") as r:  # , encoding="utf-8"
                        lines = r.readlines()
                        new = [line for line in lines if len(line) != 1]
                        with open('spisok.txt', 'w', encoding="utf-8") as w:  # , encoding="utf-8"
                            w.writelines(new)
                    print('Автомобиль успешно добавлен\n')
                    vvod()
                else:
                    print('Вы ввели неверуню команду. Повторите ввод')
                    flag4 = 0
def delete():
    # УДАЛЕНИЕ
    returnn = menu()
    vse_kharakteristic =returnn[0]
    stroki = returnn[1]
    Q = returnn[2]
    number = returnn[3]
    print('\nУдаление автомобиля')
    flag3 = 0
    while flag3 == 0:
        delete = input('Ведите номер автомобиля который хотите удалить. Чтобы вернуться назад напишите "назад" ')
        for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if delete == 'назад' or delete == 'Назад' or delete == 'yfpfl' or delete == 'Yfpfl':
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                flag3 = 1
            elif (delete[0] == i):
                if int(delete) in range(1, Q + 1):
                    delete = int(delete)
                    delete_str = []
                    #stroka[delete-1].split(',')
                    split = ''
                    for x in stroki[delete - 1]:
                        if x == ',':
                            delete_str += [split]  # += [split] --- .append
                            split = ''
                        else:
                            split += x
                    delete_str += [split]
                    marka = delete_str[0]
                    print('Вы действительно хотите удалить автомобиль', vse_kharakteristic[delete-1][1][0], vse_kharakteristic[delete-1][1][1], 'из списка?  (да / нет)')
                    yesno2 = str(input())
                    if yesno2 == 'да' or yesno2 == 'Да' or yesno2 == 'lf' or yesno2 == 'Lf':
                        with open('spisok.txt', 'r', encoding="utf-8") as r:  # , encoding="utf-8"
                            stroki = r.readlines()
                            count = 1
                            with open('spisok.txt', 'w', encoding="utf-8") as w:  # , encoding="utf-8"
                                for line in stroki:
                                    if count != delete:
                                        w.write(line)
                                    count += 1
                        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nАвтомобиль', marka,
                              'успешно удалён')
                        del number[-1]  # number.pop
                        vvod()
                    elif yesno2 == 'нет' or yesno2 == 'Нет' or yesno2 == 'ytn' or yesno2 == 'Ytn':
                        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nПроизошла отмена удаления\n')
                        vvod()
                else: print('Вы ввели неверное значение. Повторите ввод')
                flag3 = 0
            else:
                print('Вы ввели неверное значение\n')
                flag3 = 0
            vvod()
        for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if (delete[0] == i):
                if int(delete) in range(1, Q + 1):
                    delete = int(delete)
                    delete_str = []
                    #stroka[delete-1].split(',')
                    split = ''
                    for x in stroki[delete - 1]:
                        if x == ',':
                            delete_str += [split]  # += [split] --- .append
                            split = ''
                        else:
                            split += x
                    delete_str += [split]
                    marka = delete_str[0]
                    print('Вы действительно хотите удалить автомобиль', vse_kharakteristic[delete-1][1][0], vse_kharakteristic[delete-1][1][1], 'из списка?  (да / нет)')
                    yesno2 = str(input())
                    if yesno2 == 'да' or yesno2 == 'Да' or yesno2 == 'lf' or yesno2 == 'Lf':
                        with open('spisok.txt', 'r', encoding="utf-8") as r:  # , encoding="utf-8"
                            stroki = r.readlines()
                            count = 1
                            with open('spisok.txt', 'w', encoding="utf-8") as w:  # , encoding="utf-8"
                                for line in stroki:
                                    if count != delete:
                                        w.write(line)
                                    count += 1
                        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nАвтомобиль', marka,
                              'успешно удалён')
                        del number[-1]  # number.pop
                        vvod()
                    elif yesno2 == 'нет' or yesno2 == 'Нет' or yesno2 == 'ytn' or yesno2 == 'Ytn':
                        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nПроизошла отмена удаления\n')
                        vvod()
def poisk(pois):
    with open('spisok.txt', 'r', encoding="utf-8") as r:  # , encoding="utf-8"
        stroki = r.readlines()  # Строки
        new = [line for line in stroki if len(line) != 1]
    with open('spisok.txt', 'w', encoding="utf-8") as w:  # , encoding="utf-8"
        w.writelines(new)
    with open('spisok.txt', 'r', encoding="utf-8") as s:  # , encoding="utf-8"
        stroki = s.readlines()
        Q = len(stroki)  # Количество машин
        for x in stroki:
            if x[0] == '' or x[0] == ' ':
                Q -= 1
    
    with open('spisok.txt', 'r', encoding="utf-8") as s:  # , encoding="utf-8"
        for w in range(0, Q):
            stroka_kharakteristic = []
            kharakteristic = []
            nazv_kharakteristic = []
            znach_kharakteristic = []
            split = ''
            for x in stroki[w]:
                if x == ',':
                    stroka_kharakteristic += [split]
                    split = ''
                else:
                    split += x
            stroka_kharakteristic += [split]
            dlyaPoiska(stroka_kharakteristic, pois)
        print("------------------------------------------")
        vvod()

def dlyaPoiska(stroka_kharakteristic, pois):
    a = stroka_kharakteristic
    m = a[11]
    m = m[0:-1]
    a[11] = m #Обрезание двух последних символов (\n), они мешают поиску по параметру - руль
    with open('spisok.txt', 'r', encoding="utf-8") as r:  # , encoding="utf-8"
        stroki = r.readlines()  # Строки
        new = [line for line in stroki if len(line) != 1]
    with open('spisok.txt', 'w', encoding="utf-8") as w:  # , encoding="utf-8"
        w.writelines(new)
    with open('spisok.txt', 'r', encoding="utf-8") as s:  # , encoding="utf-8"
        stroki = s.readlines()
        Q = len(stroki)  # Количество машин
        for x in stroki:
            if x[0] == '' or x[0] == ' ':
                Q -= 1
    for NAZV in ['Название авто-', 'Гос номер-', 'Тип кузова-', 'Цвет-', 'Коробка передач-', 'Год выпуска-', 'Привод-', 'Пробег-', 'Тип двигателя-', 'Объем двигателя-', 'Мощность-', 'Руль-']:
        for i in range(0, len(a)):
            if a[i] == NAZV + pois:
                print("------------------------------------------")
                for i in range(0, len(a) + 1):
                    if i == 0:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:13] + ' '*(16-len(stroka_kharakteristic[i][:13])), '|', stroka_kharakteristic[i][14:])
                    elif i == 1:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:9] + ' '*(16-len(stroka_kharakteristic[i][:9])), '|', stroka_kharakteristic[i][10:])
                    elif i == 2:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:10] + ' '*(16-len(stroka_kharakteristic[i][:10])), '|', stroka_kharakteristic[i][11:])
                    elif i == 3:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:4] + ' '*(16-len(stroka_kharakteristic[i][:4])), '|', stroka_kharakteristic[i][5:])
                    elif i == 4:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:15] + ' '*(16-len(stroka_kharakteristic[i][:15])), '|', stroka_kharakteristic[i][16:])
                    elif i == 5:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:11] + ' '*(16-len(stroka_kharakteristic[i][:11])), '|', stroka_kharakteristic[i][12:])
                    elif i == 6:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:6] + ' '*(16-len(stroka_kharakteristic[i][:6])), '|', stroka_kharakteristic[i][7:])
                    elif i == 7:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:6] + ' '*(16-len(stroka_kharakteristic[i][:6])), '|', stroka_kharakteristic[i][7:])
                    elif i == 8:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:13] + ' '*(16-len(stroka_kharakteristic[i][:13])), '|', stroka_kharakteristic[i][14:])
                    elif i == 9:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:15] + ' '*(16-len(stroka_kharakteristic[i][:15])), '|', stroka_kharakteristic[i][16:])
                    elif i == 10:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:8] + ' '*(16-len(stroka_kharakteristic[i][:8])), '|', stroka_kharakteristic[i][9:])
                    elif i == 11:
                        print(i+1, (2-len(str(i+1)))*' ', '|', stroka_kharakteristic[i][:4] + ' '*(16-len(stroka_kharakteristic[i][:4])), '|', stroka_kharakteristic[i][5:])
vvod()




#Название авто-Toyota Land Cruiser,Гос номер-в372мн124,Тип кузова-внедорожник,Цвет-черный,Коробка передач-автомат,ГОд выпуска-2015,Привод-полный,Пробег-180000,Тип двигателя-дизель,Объем двигателя-4.5,Мощность-235,Руль-левый
'''def poisk():
    poisk = []
    returnn = menu()
    vse_kharakteristic = returnn[0]

    stroki = returnn[1]
    Q = returnn[2]
    number = returnn[3]
    vvod_khar = input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nВведите характеристику по которой хотите произвести поиск\n')
    vvod_znach = input('Введите значение для поиска')
    for lines in vse_kharakteristic:
        for y in lines[1]:
            if y == vvod_znach:
                poisk += [lines]
    Q = len(poisk)
    if poisk != []  :
        print('\nСписок автомобилей:\n')
        print('     | Название авто              | Гос.номер')
        print('_____|____________________________|___________')
        for w in range(0, Q):
            print(number[w], (3 - len(str(number[w]))) * ' ', '|', poisk[w][0], (25 - len(poisk[w][0])) * ' ', '|', poisk[w][1])
            print('_____|____________________________|___________')
        print('\nМеню навигации\n'
          '1)Для просмотра характеристик и модификации введите порядковый номер автомобиля\n'
          '2)Для поиска введите "поиск"\n'
          '3)Чтобы добавить автомобиль в список нажмите + \n'
          '4)Чтобы удалить автомобиль из списка нажмите -\n')
        vvod1 = input()

        for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if (vvod1[0] == i):
                x = int(vvod1)
                if x not in range(1, Q + 1):
                    print('Вы ввели неверный номер автомобиля. Повторите ввод')
                else:
                    kharakteristic(x)
            elif (vvod1 == '+'):
                dobavl()
            elif (vvod1 == '-'):
                delete()

    else:  
        print('Авто не найдены')
        vvod()'''
