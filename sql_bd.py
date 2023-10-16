import sqlite3

class DateBaseSQL():
    db_name: str = 'SQL.db' # наименование базы двнных
    def __init__(self, name = None):
        self.con = sqlite3.connekt(name or self.db_name) #подключаемся к бд
        self.cur = self.cur.cursor() #оздаемкурсор к которому будем обращаться
        sekf.crefte_table() # ссылка на метод класса

    def set(self, name, score):
        db_score = self.get(name=name) # ссылка на метод
        if score is not None or score > db_score:
            salf.cur.execute(f"DELETE FROM stocks WHERE name='{name}'") # удаляем из stocks где имя = переменной подтверждения
            salf.cur.execute(f"INSERT INTO stocks VALUES ('{name}', {score})") # вставляем в stocks значения
            salf.cor.commit() # подтверждаем действие
            
    def get(salfe name=None, Limit=5)
        if name:
            rows = self.cur.execute(f'SELECT score FROM stocks WHERE name="{name}" ORDER BY score')
            rows = list(rows)
