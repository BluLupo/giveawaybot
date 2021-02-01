from core.database.db_connect import Connection
from pypika import Query, Table

conf = Table("config_table")

class ConfRepository(Connection):
    def getAll(self):
        query = Query.from_(conf).select("*")
        q = query.get_sql(quote_char=None)
        return self._selectAll(q)

    def getOne(self):
        query = Query.from_(conf).select("*")
        q = query.get_sql(quote_char=None)
        return self._select(q)

    def setGiveaway(self, args=None):
        q = "UPDATE config_table SET switch = %s WHERE ID = 1"
        return self._update(q, args)

    def setMain(self, args=None):
        q = "UPDATE config_table SET main_text = %s WHERE ID = 1"
        return self._update(q, args)

    def setButton(self, args=None):
        q = "UPDATE config_table SET button_text = %s WHERE ID = 1"
        return self._update(q, args)