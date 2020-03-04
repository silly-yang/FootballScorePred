import configparser
import pymysql

class DBHelper:

    def __init__(self):
        # 讀取conf
        conf = configparser.ConfigParser()
        conf.read("config.ini")

        self.host = conf['DB']['host']
        self.user = conf['DB']['user']
        self.password = conf['DB']['password']
        self.db = conf['DB']['dbName']

    def __connect__(self):
        
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql, params):
        self.__connect__()
        self.cur.execute(sql, params)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    # def execute(self, sql):
    #     self.__connect__()
    #     self.cur.execute(sql)
    #     self.__disconnect__()
