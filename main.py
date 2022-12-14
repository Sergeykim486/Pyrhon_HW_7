import os
import importfile, exportfile, editbook, printbook
from colorama import Fore, Back
spacer = '══════════════════════════════════════════════════════════════'
Task = 0
Phonebook = []
os.system('cls')

def show_menu():
    os.system('cls')
    print(Back.YELLOW + ''
          '███████████████████████████████████████████████████\n'
          '██                                               ██\n'
          '██   Г Л А В Н О Е  М Е Н Ю                      ██\n'
          '██                                               ██\n'
          '██   ФАЙЛ                  ПРАВКА                ██\n'
          '██   1. Открыть JSON       5. Добавить           ██\n'
          '██   2. Открыть CSV        6. Изменить           ██\n'
          '██   3. Сохранить JSON     7. Удалить            ██\n'
          '██   4. Сохранить CSV      8. Показать спписок   ██\n'
          '██   '+Fore.RED+'9. Выход'+Fore.RESET+'                                    ██\n'
          '██                                               ██\n'
          '███████████████████████████████████████████████████\n'
          ''+ Back.RESET)
def enter_key_to_continue():
    input("\033[0m{}".format(f'{spacer}\nДля продолжения нажмите клавишу [ENTER]'))
    main()
def error(x):
    os.system('cls')
    print(Back.RED + '\n                                       '
          '\n              ОШИБКА!!!                '
          '\n  Вы ввели не существующую команду...  '
          '\n      Выберите команду из списка.      '
          '\n                                       ')
    enter_key_to_continue()
def inputdata(inputcomment):
    d = input(Fore.BLUE + f'{inputcomment} ->  ' + Fore.RESET)
    return d
def printres(res):
    print(Fore.GREEN + f'{spacer}\n'
          + Fore.CYAN + f'{res}\n'
          + Fore.GREEN + f'{spacer}' + Fore.RESET)
def choice(x):
    global Phonebook, spacer
    if x == 1:
        os.system('cls')
        Phonebook = importfile.openjsonfile('Phones.json')
        printres(printbook.printtable(Phonebook) + Fore.GREEN + f'\n{spacer}\nДанные json успешно загружены.' + Fore.RESET)
        enter_key_to_continue()
    elif x == 2:
        os.system('cls')
        Phonebook = importfile.opencsvfile('Phones.csv')
        printres(printbook.printtable(Phonebook) + Fore.GREEN + f'\n{spacer}\nДанные csv успешно загружены.' + Fore.RESET)
        enter_key_to_continue()
    elif x == 3:
        if Phonebook == []:
            os.system('cls')
            print(Fore.RED + 'Вы не открыли файл! \nСначала откройте файл JSON или CSV...' + Fore.RED)
            enter_key_to_continue()
        else:
            os.system('cls')
            exportfile.savetojson('Phones.json', Phonebook)
            printres('JSON файл сохранен')
            enter_key_to_continue()
    elif x == 4:
        if Phonebook == []:
            os.system('cls')
            print(Fore.RED + 'Вы не открыли файл! \nСначала откройте файл JSON или CSV...' + Fore.RED)
            enter_key_to_continue()
        else:
            exportfile.savetocsv('Phones.csv', Phonebook)
            printres('CSV файл сохранен')
            enter_key_to_continue()
    elif x == 5:
        if Phonebook == []:
            os.system('cls')
            print(Fore.RED + 'Вы не открыли файл! \nСначала откройте файл JSON или CSV...' + Fore.RED)
            enter_key_to_continue()
        else:
            os.system('cls')
            printres(printbook.printtable(Phonebook))
            editbook.addnew(Phonebook)
            enter_key_to_continue()
    elif x == 6:
        if Phonebook == []:
            os.system('cls')
            print(Fore.RED + 'Вы не открыли файл! \nСначала откройте файл JSON или CSV...' + Fore.RED)
            enter_key_to_continue()
        else:
            os.system('cls')
            printres(printbook.printtable(Phonebook))
            editbook.editcontact(Phonebook)
            enter_key_to_continue()
    elif x == 7:
        if Phonebook == []:
            os.system('cls')
            print(Fore.RED + 'Вы не открыли файл! \nСначала откройте файл JSON или CSV...' + Fore.RED)
            enter_key_to_continue()
        else:
            os.system('cls')
            printres(printbook.printtable(Phonebook))
            editbook.deletecontact(Phonebook)
            enter_key_to_continue()
    elif x == 8:
        if Phonebook == []:
            os.system('cls')
            print(Fore.RED + 'Вы не открыли файл! \nСначала откройте файл JSON или CSV...' + Fore.RED)
            enter_key_to_continue()
        else:
            os.system('cls')
            printres(printbook.printtable(Phonebook))
            enter_key_to_continue()
    elif x == 9:
        os.system('cls')
        print(Fore.RED + 'Выход из программы...' + Fore.RESET)
        import sys
        sys.exit()
    else:
        error(Task)
def main():
    show_menu()
    try:
        Task = int(input(Fore.BLUE + 'Введите номер операции ->  ' + Fore.RESET))
    except:
        Task = 0
    choice(Task)

main()