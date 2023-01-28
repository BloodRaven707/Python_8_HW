from os import system


import model
import view


menu_journal_choise = ["### Выберите класс: ###"]
menu_subject_choise = ["### Выберите предмет: ###"]
menu_learner_choise = ["### Выберите действие: ###"]

def main():
    # system("cls")  # Уже очищена
    menu_journal_choise.extend( model.journals_list() )
    command = view.input_command( menu_journal_choise )
    if command == 0:
         view.close(); return
    model.journal_open( menu_journal_choise[ command ] )

    system("cls")
    # Журнал выбран, список предметов загружен
    menu_subject_choise.extend( model.subjects )
    command = view.input_command( menu_subject_choise )
    if command == 0:
         view.close(); return

    model.subject_open( menu_subject_choise[ command ] )

    # Выбран предмет, список учеников загружен
    menu_learner_choise.extend([ "Поставить оценку, за работу на уроке", "", "", "", "", "", "", "" ])
    while True:
        system("cls")
        # Доступные действия
        command, learner_name = view.input_lerner_command( menu_learner_choise, model.journal[ model.subject_name ] )

        # Выход
        if command == 0:
            view.close(); return

        # Добавить оценку
        if command == 1:
            view.show_learner_and_mark( learner_name, model.journal[ model.subject_name ][ learner_name ] )
            # Запрос оценки
            mark = view.mark_input()
            model.mark_add( learner_name, mark )

        ##########################################################
        #
        # Не успеваю, ни фига...
        #
        ##########################################################

        elif command == 2:
            pass

        elif command == 3:
            # найти (вызвать) ученика
            search = view.search_request()          #               ex. /str/
            result = model.search_pupil(search)     # inp. /str/    ex. /dict - ?/
            view.show_pupil(result)                 # inp. /str/    ex. /list - ?/

        elif command == 4:
            # поставить ученику оценку
            search = view.search_request()          #               ex. /str/
            result = model.search_pupil(search)     # inp. /str/    ex. /dict - ?/
            model.mark_put(result, mark)            # inp. /dict, str/  ex.
            view.mark_success()                     # inp.          ex. /str/ 'Оценка внесена в журнал'

        elif command == 5:
            # добавить ученика
            new_pupil = view.create_pupil()         # inp.          ex. /dict -?/
            model.school_db.append(new_pupil)       # inp. /dict/   ex. /list/

        elif command == 6:
            # изменить ученика
            search = view.search_request()          # inp.          ex. /str/
            result = model.search_pupil(search)     # inp. /str/    ex. /list/
            confirm = view.confirm_changes(result)  # inp. /list/   ex. /str/   y/n
            if 'n' not in confirm:
                new_pupil = view.create_pupil()     # inp.          ex. /dict/
            response = model.change_pupil(result,confirm,new_pupil) # inp. /list, str, list/    ex. /str/
            view.change_success(response)           # inp. /str/

        elif command == 7:
            # удалить ученика
            search = view.search_request()          # inp.          ex. /str/
            result = model.search_pupil(search)     # inp. /str/    ex. /list/
            confirm = view.confirm_changes(result)  # inp. /list/   ex. /str/  y/n
            response = model.delete_contact(result,confirm) # inp. /list, str/ ex. /str/
            view.delete_success(response)           # inp. /str/    ex. /str/ 'Ученик удален'

        elif command == 8:
            # сохранить класс в файл с БД
            model.save_db(path)                     # inp. /str/    ex. updated file
            view.save_success()                     # inp.          ex. /str/ 'Файл сохранен'






# Для тестирования
if __name__ == "__main__":
    system("cls")
    main()
