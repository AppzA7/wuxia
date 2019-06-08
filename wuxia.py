import sqlite3
import sqls

class WuxiaWorld:
    def __init__(self, db_file_path='./wuxiaworld.db'):
        self.db_file = db_file_path; 
        self.baseUrl = "https://www.wuxiaworld.com/"
        self.conn=None
        self.createConnection()
        self.__create_databases__()

    def createConnection(self):
        """ create a database connection to a SQLite database """
        try:
            self.conn = sqlite3.connect(self.db_file)
            print("successfully connected to wuxia db")
        except Exception as e:
            print(e)
        return self.conn

    def getSizeDatabase(self):
        if(self.conn):
            cursor = self.conn.execute('select name from sqlite_master where type="table"')
            return (len(cursor.fetchall()))
            
    def __create_databases__(self):
        if(self.conn):
            self.conn.execute(sqls.create_novel_table)

    def getChapterUrl(self, novel, chapter, abbr):
        return self.baseUrl + "novel/{}/{}-chapter-{}".format(novel, abbr, chapter)
    
    def getChapterContent(self, url):
        

if __name__ == "__main__":
    ww = WuxiaWorld()
    ww.getSizeDatabase()