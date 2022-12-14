import os
from colorama import Fore, Back
def addnew(data):
    id = len(data) + 1
    fname = input('Введите имя... ->  ')
    lname = input('Введите фамилию... ->  ')
    phone = input('Введите номер телефона... ->  ')
    conf = str(input(f'Подтвердите информацию:'
                         f'id: {id}'
                         f'Имя: {fname}'
                         f'Фамилия: {lname}'
                         f'Номер телефона: {phone}'
                         f'[y]-ДА  [n]-НЕТ'))
    conf.replace('Y', 'y')
    conf.replace('N', 'n')
    if conf == 'y':
        data.append({'id': id, 'f_name': fname, 'l_name': lname, 'phone': phone})
    elif conf == 'n':
        print('Отменено.')
    else:
        print(Fore.RED + 'Ошибка ввода' + Fore.RESET)
        addnew(data)

def editcontact(data):
    cont = int(input('Введите порядковый номер контакта... ->  '))
    if cont <= len(data):
        for i in data:
            if i['id'] == cont:
                print('Что Вы хотите изменить?' + '\n'
                      '1. Изменить Имя: \t' + str({i['f_name']}) + '\n'
                      '2. Изменить Фамилия:\t' + str({i['l_name']}) + '\n'
                      '3. Изменить Телефон:\t' + str({i['phone']}) + '\n'
                      '4. Изменить все.')
                ch = int(input('Выберите действие ->  '))
                if ch == 1:
                    i['f_name'] = input('Введите новое имя. ->  ')
                elif ch == 2:
                    i['l_name'] = input('Введите новую фамилию. ->  ')
                elif ch == 3:
                    i['phone'] = input('Введите новый номер телефона. ->  ')
                elif ch == 4:
                    i['f_name'] = input('Введите новое имя. ->  ')
                    i['l_name'] = input('Введите новую фамилию. ->  ')
                    i['phone'] = input('Введите новый номер телефона. ->  ')
                elif ch == '':
                    print(Fore.RED + 'Ошибка ввода! повторите попытку' + Fore.RESET)
                    editcontact(data)
    else:
        print(Fore.RED + 'Ошибка ввода' + Fore.RESET)
        editcontact(data)

def deletecontact(data):
    cont = int(input('Введите порядковый номер контакта... ->  '))
    res = ''
    if cont <= len(data):
        for i in data:
            if i['id'] == cont:
                res = str(i['id'])+'. '+str(i['f_name'])+' '+str(i['l_name'])+' '+str(i['phone'])
                print(str(i['id'])+'. '+str(i['f_name'])+' '+str(i['l_name'])+' '+str(i['phone'])+'\n'+
                      'Вы уверены что хотите удалить этот контакт?')
                conf = str(input(Fore.RED + '[y]-ДА  [n]-НЕТ' + Fore.RESET))
                conf.replace('Y', 'y')
                conf.replace('N', 'n')
                if conf == 'y':
                    data.remove(i)
                    res = res + ' - УДАЛЕН!'
                    it = 1
                    for j in data:
                        j['id'] = it
                        it += 1
                    return res
    else:
        print(Fore.RED + 'Ошибка ввода' + Fore.RESET)
        editcontact(data)