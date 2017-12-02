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
        res = self.__safeExecute__(
            queryString, 
            lambda cur: cur.execute(queryString, params),
            lambda cur: cur.fetchall());
        return res;

    def executeNonQuery(self, queryString, *params):
        res = self.__safeExecute__(
            queryString, 
            lambda cur: cur.execute(queryString, params),
            lambda cur: None);
        return res;

    def executeProcedure(self, procNane, *params):
        res = self.__safeExecute__(
            procNane, 
            lambda cur: cur.callproc(procNane, params),
            lambda cur: cur.fetchall());
        return res;

    def executeScalar(self, queryString, *params):
        res = self.__safeExecute__(
            queryString, 
            lambda cur: cur.execute(queryString, params),
            lambda cur: cur.fetchone()[0]);
        return res;

    def __safeExecute__(self, queryString, executeAction, getResultFunc):
        try:
            connection = psycopg2.connect(**self.connectionSettings);
            cur = connection.cursor()
            executeAction(cur);
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
