import psycopg2 as psycopg2

from Resources.ConfigLoader import ConfigLoader


class UserDB:

    def __init__(self):
        self.host = ConfigLoader.get_config().get('database')['host']
        self.database = ConfigLoader.get_config().get('database')['name']
        self.user = ConfigLoader.get_config().get('database')['user']['name']
        self.password = ConfigLoader.get_config().get('database')['user']['password']

    def query_users(self):
        rows = self.execute_query('SELECT id, username, password, role, active FROM users;')
        users = []
        for row in rows:
            print(row)
            user_dict = dict()
            user_dict['id'] = row[0]
            user_dict['username'] = row[1]
            user_dict['password'] = row[2]
            user_dict['role'] = row[3]
            user_dict['active'] = row[4]
            users.append(user_dict)
        return users

    def execute_query(self, query):
        conn = None
        rows = []
        try:
            conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return rows


