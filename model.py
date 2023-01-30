from json import dump as json_dump, load as json_load
from os.path import isfile
from random import choice, randrange


# # TODO:
# 1. Работу с файлами отдельно
# 2. Работу с каждой структурой отдельно по классам
# 3. Вложенные структура (класс < предмет < ученик < оценка)
# 4. Вынести функционал сохранения из общей логики и вызывать его отдельно
# #


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

# Все журналы - Открыть и Отдать список
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

# Сохренение в файл журнала # json
def journal_save( class_name: str = journal_name, data: dict = journal ):
    global journals
    file_name = f"classes\\{ class_name.upper() }.json"
    with open( file_name, "w", encoding="UTF-8" ) as f:
        json_dump( data, f, ensure_ascii=False )
# journal_save( "7B", journal )

# Отдает журнал
def journal_get( journal = journal ) -> dict:
    return journal

# Открыть предмет в выбранном журнале
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

# Добавить Ученика
def learner_add( learner_name, marks= [] ):
  global journal, subject_name
  journal[subject_name][learner_name] = marks
  journal_save( journal_name, journal )
  return journal[subject_name]
# print ( list( learner_add( "Суслов" ) ) )
# print ( list( learner_add( "Дуслов", [2, 3, 5] ) ) )

# Удалить ученика
def learner_del ( learner_name ):
  global journal, subject_name
  if learner_name in list ( journal[subject_name] ):
    marks = journal[subject_name].pop( learner_name )
  journal_save( journal_name, journal )
  return journal[subject_name], marks
# print ( list( learner_del( "Суслов" )[0] ) )
# print ( list( learner_add( "Суслов" ) ) )

# Изменит Ученика
def learner_edit( learner_name, new ):
  _, marks = learner_del( learner_name )
  journal = learner_add( new, marks )
  journal_save( journal_name, journal )
  return journal[subject_name]
# print ( list( learner_edit( "Дуслов", "Гуслов" ) ) )

# Получить студента и оценики
def marks_get( learner_name ) -> ( str, list ): # str, [ int, int, int, ... ]
  global journal, subject_name
  return learner_name, journal[subject_name][learner_name]
#print( marks_get( "Иванов" ) )

# Добавить оценку
def mark_add( learner_name: str, mark: int = 5, ) -> dict: # -> subject
    global journal, subject_name
    journal[subject_name][learner_name].append( mark )
    journal_save( journal_name, journal )
    return journal[subject_name]
# print ( mark_add( "Иванов", 4 )["2"] )
# print ( mark_add( "Иванов", 1 )["2"] )
# print ( mark_add( "Иванов", 1 )["2"] )

# Удалить оценку
def mark_del( learner_name, mark ):
  global journal, subject_name
  if mark in journal[subject_name][learner_name]:
    journal[subject_name][learner_name].pop( journal[subject_name][learner_name].index( mark ))
    journal_save( journal_name, journal )
  return journal
# print ( mark_del( "Иванов", 1 )["2"] )

# Земенить оценку или поставить новую
def mark_upd( learner_name, mark, old = 1 ):
  global journal, subject_name
  for om in range( old, mark ):
    if om in journal[subject_name][learner_name]:
      mark_del( learner_name, om )
      break
  mark_add( learner_name, mark )
  journal_save( journal_name, journal )
  return journal
# print ( mark_add( "Иванов", 1 )["2"] )
# print ( mark_upd( "Иванов", 4 )["2"] )
# print ( mark_upd( "Иванов", 3 )["2"] )
# print ( mark_add( "Иванов", 4 )["2"] )



# Для тестирования
# if __name__ == "__main__":
#     from os import system
#     system("cls")
#     import controller
#     controller.main()
