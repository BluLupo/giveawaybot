from core.database.db_connect import Connection
from pypika import Query, Table

users = Table("users")

class UserRepository(Connection):
    def getAll(self):
        query = Query.from_(users).select("*")
        q = query.get_sql(quote_char=None)
        return self._selectAll(q)

    def getById(self, args=None):
        query = Query.from_(users).select("*").where(users.user_id == "%s")
        q = query.get_sql(quote_char=None)
        return self._select(q, args)

    def getRandom(self, args=None):
        q = "SELECT * FROM users ORDER BY RAND() LIMIT 1"
        return self._select(q, args)

    def add(self, args=None):
        q = "INSERT IGNORE INTO users (user_id, user_nickname) VALUES (%s,%s)"
        return self._insert(q, args)

    def deleteAllOne(self):
        q = "DELETE FROM users"
        return self._deleteone(q)

    def deleteAll(self, args=None):
        q = "DELETE FROM users"
        return self._delete(q,args)