import psycopg2

class DbContext(object):
    def __init__(self, connectionSettings):
        self.connectionSettings = connectionSettings;

    def __enter__(self):
        #acquire resources
        return self;

    def __exit__(self, exc_type, exc_value, traceback):
        #release resources
        pass;

    def executeQuery(self, queryString, *params):
        res = self.__safeExecute__(queryString, lambda cur: cur.fetchall(), params);
        return res;

    def executeScalar(self, queryString, *params):
        res = self.__safeExecute__(queryString, lambda cur: cur.fetchone()[0], *params);
        return res;

    def __safeExecute__(self, queryString, getResultFunc, *params):
        try:
            connection = psycopg2.connect(**self.connectionSettings);
            cur = connection.cursor()
            cur.execute(queryString, params);
            res = getResultFunc(cur);
            connection.commit();
            return res;
        except (Exception, psycopg2.DatabaseError) as error:
            print(error);
        finally:
            if cur is not None:
                cur.close();
            if connection is not None:
                connection.close();
