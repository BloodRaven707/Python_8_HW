# Универсальное меню
def show_menu( menu: list ) -> int:
    print( f"\n{ menu[ 0 ] }" )
    for i in range( 1, len( menu ) ):
        print( f'\t{ i } - { menu[ i ] }' )
    print( f'\t{ 0 } - {"Завершить работу"}' )

# Запрос ввода
def input_command( menu: list ) -> str:
    while True:
        # Вывод меню
        show_menu( menu )
        command = input( '\nВведите числовую команду: ' )
        if command.isdigit():
            command = int( command )
            if 0 <= command <= len( menu ):
                return command
            else:
                print( "Не верная команда" )

# Вывод всех учеников с оценками
def show_learners_and_marks( subject: dict ):
    learners = list(subject)
    print( "\n### Список учеников: ###" )
    for i, learner_name in enumerate( learners, 1 ):
        marks = subject[ learner_name ]
        print( f"\t{ i } - { learner_name }: { marks }")

# Вывод 1-го ученика с оценками
def show_learner_and_mark( learner_name, marks ):
    print( f"\n\t{ learner_name }: { marks }" )

# Ввод команды для действий с учениками (Меню с проверкой 2-х элементов)
def input_lerner_command( menu: list, subject: dict ) -> ( int, str ):
    while True:
        show_learners_and_marks( subject )
        # Вывод меню
        show_menu( menu )
        print( "\nПодсказка: дейсвие ученик. Пример ввода: \"1 1\". Не забудьте пробел..." )
        commands = input( 'Введите числовую команду: ' )
        if commands == "0":
            return 0, ""

        if all([command.isdigit() for command in commands.split()]) and len( commands.split() ) == 2:
            command, learner_id = [ int(command) for command in commands.split() ]
            if 0 <= command <= len( menu ) and 1 <= learner_id <= len( subject ):
                return command, list( subject )[ learner_id ]
            else:
                print( "Не верная команда..." )

# Ввдод оценки...
def mark_input() -> int:
    while True:
        mark = input( "\nВведите оценку от 1 до 5: " )
        if mark.isdigit() and mark in [ "1", "2", "3", "4", "5" ]:
            return int(mark)
        else:
            print( f"Недьзя поставить оценку {mark}..." )


def close():
    print( "\nВ пень я запарился...\n" )




# Для тестирования
# if __name__ == "__main__":
#     from os import system
#     system("cls")
#     import controller
#     controller.main()
