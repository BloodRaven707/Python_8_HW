from json import dump as json_dump, load as json_load
from os.path import isfile
from random import choice, randrange

# Globals_test
subjects_test = { "Mathematics": "Математика", "Physics": "Физика", "Russian": "Русский", "Химия": "Chemistry" }  #, "": ""

# Globals
journals = []      # Список журналов
journal = {}       # Объект журнал - выбраный/используемый
class_name = ""    # Наименование выбранного класса 7А      // Потом
journal_name = ""  # Наименование выбранного класса 7А      // Потом

subjects = []      # Список предметов в журнале
# subject = {}     !!!!!!!! НЕТ УКАЗАТЕЛЕЙ КАК в GO..... УБРАТЬ..... ломат программу # Объект предмет - выбраный
subject_name = {}  # Наименование предмета

learners = []      # Список учеников по именам
learner_name = ""  # Выбранный ученик

# Все журналы - Отдать список
def journals_list() -> list:
    global journals
    with open( "classes\\journals.txt", encoding="UTF-8" ) as f:
        for s in f:
            journals.append(s.strip())
    return journals

# Все журналы - Сохранить новый список
def journals_save( journals = journals ):
    with open( "classes\\journals.txt", "w", encoding="UTF-8" ) as f:
        for class_name in journals:
            f.write( class_name )

# Открытие файла журнала # json
def journal_open( class_name: str = journal_name ) -> dict: # -> journal
    global journal, journal_name, subjects
    file_name = f"classes\\{ class_name.upper() }.json"
    # expansion = file_name.split(".")[-1]
    try:
        with open( file_name, encoding="UTF-8" ) as file:
            journal = json_load( file )
    except:
        return journal
    journal_name = class_name
    subjects = list(journal)
    return journal
def journal_opend_txt( class_name: str = journal_name ) -> dict:
    global journal
    with open( f"classes\\{ class_name.upper() }.txt", encoding='UTF-8' ) as file:
        for line in file:
            subject_name, data = line.strip().split(';')
            journals[subject_name] = {}
            for subject in data.split(','):
                learner = subject.split(':')
                journals[subject_name][learner[0]] = learner[1].split(',')
    return journal
# print( "" ); print( "7A" ); print( *list(open_file( "7A" ).items()), sep="\n" ); print( "" )

# Сохренение в файл журнала
def journal_save( class_name: str = journal_name, data: dict = journal ):
    global journals
    file_name = f"classes\\{ class_name.upper() }.json"
    with open( file_name, "w", encoding="UTF-8" ) as f:
        json_dump( data, f, ensure_ascii=False )
# journal_save( "7B", journal )

# Отдает журнал
def journal_get( journal = journal ) -> dict:
    return journal

# Открыть предмет в журнале
def subject_open( get_subject_name ) -> dict:
    global journal, subject_name
    subject_name = get_subject_name
    learners = list( journal[ subject_name ] )
    return journal[subject_name]
# print( subject_open( 'Математика' ) )

# Получить предмет
def subject_get() -> dict: # -> { learner_name: [ int, int ], learner_name: [ int, int ] }
    global journal, subject_name
    return journal[subject_name]
# print( subject_get( 'Математика' ) )

# Получить студента и оценики
def marks_get( learner_name ) -> ( str, list ): # str, [ int, int, int, ... ]
    global subject
    return learner_name, subject[ learner_name ]

# Добавить оценку
def mark_add( learner_name: str, mark: int = 5, ) -> dict: # -> subject
    global journal, subject_name
    marks = journal[subject_name][learner_name]
    marks.append(mark)
    journal[subject_name][learner_name] = marks
    journal_save( journal_name, journal )
    return journal[subject_name]





# Для тестирования
# if __name__ == "__main__":
#     from os import system
#     system("cls")
#     import controller
#     controller.main()
