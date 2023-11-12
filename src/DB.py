import psycopg2


class DBManager:
    def __init__(self, database_name, DB_PASS):
        self.database_name = database_name
        self.DB_PASS = DB_PASS

    def get_companies_and_vacancies_count(self):
        '''  Метод получает список всех компаний и
        количество вакансий у каждой компании '''
        with psycopg2.connect(host="localhost", database=self.database_name,
                              user="postgres", password=self.DB_PASS) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT company_name, COUNT(vacancy_id) '
                            'FROM companies '
                            'JOIN vacancies USING (company_id) '
                            'GROUP BY company_name;')
                data = cur.fetchall()
            conn.commit()
        return data

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия
        вакансии и зарплаты и ссылки на вакансию."""
        with psycopg2.connect(host="localhost", database=self.database_name,
                              user="postgres", password=self.DB_PASS) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT title_vacancy, company_name, salary, vacancies.link '
                            'FROM vacancies '
                            'JOIN companies USING (company_id);')

                data = cur.fetchall()
            conn.commit()
        return data

    def get_avg_salary(self):
        '''Метод получает среднюю зарплату по вакансиям'''
        with psycopg2.connect(host="localhost", database=self.database_name,
                                user="postgres", password=self.DB_PASS) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT company_name, round(AVG(salary)) AS average_salary '
                            'FROM companies '
                            'JOIN vacancies USING (company_id) '
                            'GROUP BY company_name;')
                data = cur.fetchall()
            conn.commit()
        return data

    def get_vacancies_wth_highest_salary(self):
        '''Метод получает список всех вакансий,
                у которых зарплата выше средней по всем вакансиям'''
        with psycopg2.connect(host="localhost", database=self.database_name,
                                      user="postgres", password=self.DB_PASS) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * '
                            'FROM vacancies '
                            'WHERE salary > (SELECT AVG(salary) FROM vacancies);')
                data = cur.fetchall()
            conn.commit()
        return data

    def get_vacancies_with_keyword(self, keyword):
        '''Метод получает список всех вакансий,
        в названии которых содержатся переданные в метод слова'''
        with psycopg2.connect(host="localhost", database=self.database_name,
                                      user="postgres", password=self.DB_PASS) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""
                SELECT * 
                FROM vacancies
                WHERE lower(title_vacancy) LIKE '%{keyword}%'
                OR lower(title_vacancy) LIKE '%{keyword}'
                OR lower(title_vacancy) LIKE '{keyword}%'""")

                data = cur.fetchall()
            conn.commit()
        return data