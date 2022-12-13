import os
import importfile, exportfile, editbook, printbook
from colorama import init, Fore, Back

Task = 0
Phonebook = []
os.system('cls')

def show_menu():
    os.system('cls')
    print(Back.YELLOW + ''
          '████████████████████████████████████████████\n'
          '██                                        ██\n'
          '██   Г Л А В Н О Е  М Е Н Ю               ██\n'
          '██                                        ██\n'
          '██   ФАЙЛ                  ПРАВКА         ██\n'
          '██   1. Открыть JSON       6. Добавить    ██\n'
          '██   2. Открыть CSV        7. Изменить    ██\n'
          '██   3. Сохранить JSON     8. Удалить     ██\n'
          '██   4. Сохранить CSV                     ██\n'
          '██   5. Выход                             ██\n'
          '██                                        ██\n'
          '████████████████████████████████████████████\n'
          ''+ Back.RESET)
def enter_key_to_continue():
    input("\033[0m{}".format('=================================================\nДля продолжения нажмите клавишу [ENTER]'))
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
    print(Fore.GREEN + f'==============================================================\n'
          + Fore.CYAN + f'    {res}\n'
          + Fore.GREEN + f'==============================================================' + Fore.RESET)

def choice(x):
    if x == 1:
        enter_key_to_continue()
    elif x == 2:
        enter_key_to_continue()
    elif x == 3:
        enter_key_to_continue()
    elif x == 4:
        enter_key_to_continue()
    elif x == 5:
        os.system('cls')
        print("\033[0m{}".format('Выход из программы...'))
        import sys
        sys.exit()
    elif x == 6:
        enter_key_to_continue()
    elif x == 7:
        enter_key_to_continue()
    elif x == 8:
        enter_key_to_continue()
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