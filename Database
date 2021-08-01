from testfall_cont import *
from testschritte import *
from inhalt import *
from itertools import zip_longest
import sqlite3


class Database:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('gopel.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute('''DROP TABLE inhalt''')

        self.curr.execute('''CREATE TABLE testfall(teil_num INT PRIMARY KEY,cases TEXT)''')
        self.curr.execute('''CREATE TABLE testschritte(test_step TEXT PRIMARY KEY,indeces TEXT,teil_num INT, FOREIGN KEY(teil_num) REFERENCES testfall(teil_num) ON DELETE SET NULL)''')
        self.curr.execute('''CREATE TABLE inhalt(cycle TEXT PRIMARY KEY, Makro TEXT, Ergebnis TEXT,Testzeit TEXT,Laufzeit TEXT, Zeitstempel TEXT,test_step TEXT,FOREIGN KEY(test_step) REFERENCES testschritte(test_step) ON DELETE SET NULL)''')
        self.curr.execute('''CREATE TABLE relations(teil_num INT,test_step TEXT, cycle TEXT,FOREIGN KEY(teil_num) REFERENCES testfall(teil_num) ON DELETE CASCADE, FOREIGN KEY(test_step) REFERENCES testschritte(test_step) ON DELETE CASCADE, FOREIGN KEY(cycle) REFERENCES inhalt(cycle) ON DELETE CASCADE)''')
        self.conn.commit()

    def gopel_db(self):
        
        gesamt = Gesamtprotokoll()
        gesamt.test_case()
        DML = '''INSERT INTO testfall VALUES(?,?)'''
        data = list(zip_longest(gesamt.teil_num,gesamt.cases, fillvalue=None))
        self.curr.executemany(DML, data)
        self.conn.commit()
    
        test = Testschritte()
        test.test_steps()
    
        DML = '''INSERT INTO testschritte (test_step,indeces) VALUES(?,?)'''
        data = list(zip_longest(test.prop,test.indeces,fillvalue= None))
        self.curr.executemany(DML,data)
        self.curr.execute('''UPDATE testschritte SET teil_num = 'Teil9.xml' WHERE teil_num IS NULL''')
    
        self.conn.commit()
    
        contents = Inhalt()
        contents.tables()
        contents.db_tables()
        DML = '''INSERT INTO inhalt VALUES(?,?,?,?,?,?,?)'''
        data = list(zip_longest(contents.cycle, contents.makro, contents.Ergebnis, contents.Testzeit, contents.Laufzeit,
                                contents.Zeitstempel, test.prop, fillvalue=None))
        self.curr.executemany(DML, data)
        self.conn.commit()
    
        DML = '''INSERT INTO relations (test_step,cycle) VALUES(?,?)'''
        data = list(zip_longest(test.prop,contents.cycle, fillvalue=None))
        self.curr.executemany(DML, data)
        self.curr.execute('''UPDATE relations SET teil_num = 'Teil9.xml' WHERE teil_num IS NULL''')
        self.conn.commit()

    # Connecting all three tables
	
    '''SELECT cases,indeces,makro,ergebnis,laufzeit,Zeitstempel FROM testfall,testschritte,inhalt
    WHERE testfall.teil_num = testschritte.teil_num and testschritte.test_step = inhalt.test_step'''


data = Database()
data.create_connection()
data.create_table()
data.gopel_db()