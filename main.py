from src.utilits import get_employers, create_db, create_tables, fillter_db
from src.DB import DBManager
import os

DB_PASS = os.getenv('DB_PASS')

if __name__ == '__main__':
    """ записываем 10 компании, для поиска ваканси только по ним """
    companies = [1740,      # яндекс
                 4006,      # qsoft
                 1122462,   # Skyeng
                 3529,      # сбербанк
                 880048,    # ooo мелдана
                 84585,     # авито
                 78638,     # Тинькофф
                 64174,     # 2gis
                 1272486,   # Сбермаркет
                 15478,     # VK
                 ]

    database_name = 'job'

    dbmanager = DBManager(database_name, DB_PASS)
    create_db(database_name, DB_PASS)
    create_tables(database_name, DB_PASS)
    fillter_db(get_employers(companies), database_name, DB_PASS)
print('Выберите дальшнейшее действие для работы приложения:\n'
      '1 - для получения списка всех компаний и количества вакансий у каждой компании\n'
      '2 - список всех  вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n'
      '3 - получить среднюю зарплату по вакансиям\n'
      '4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n'
      '5 - для получения списка всех вакансий, в названии которых содержатся переданные в метод слова\n'
      'стоп - закончить работу\n')
while True:
    user_input = str(input())
    if user_input == "стоп":
        print('До новых встреч')
        break
    elif user_input == '1':
        print(dbmanager.get_companies_and_vacancies_count())
    elif user_input == '2':
        print(dbmanager.get_all_vacancies())
    elif user_input == '3':
        print(dbmanager.get_avg_salary())
    elif user_input == '4':
        print(dbmanager.get_vacancies_wth_highest_salary())
    elif user_input == '5':
        keyword = input('Введите ключевое слово: ')
        print(dbmanager.get_vacancies_with_keyword(keyword))
    else:
        print('Ошибка, попробуйте еще раз')