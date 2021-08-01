from bs4 import BeautifulSoup
from lxml import html
import glob

class Gesamtprotokoll:

    def __init__(self):
        self.title = None
        self.links = None
        self.test_case()

    def test_case(self):

        path = r'filepath'
        for filename in glob.glob(path):
            with open(filename, "r") as f:
                page = f.read()
                tree = html.fromstring(page)
                soup_file = BeautifulSoup(page, features="lxml")

                self.title = soup_file.find('title').get_text()
                self.a_tags = soup_file.find_all('a')
                self.cases = [str(each.get_text()) for each in self.a_tags]
                self.teil_num = [(link.get('href')) for link in soup_file.find_all('a')]

                # PASS: Blue Color
                self.color_pass = soup_file.find_all(attrs={"color":"#0000FF"})
                self.status_pass = [str(column.get_text()) for column in self.color_pass]

                # FAIL: Red Color
                self.color_fail = soup_file.find_all(attrs={"color": "#FF0000"})
                self.status_fail = [str(column.get_text()) for column in self.color_fail]


    def display(self):
        print("Dateien:",self.title)
        print("Testfälle:",self.cases)
        print("Teil Nummer:",self.teil_num)
        print("PASS Testfälle:",self.status_pass)
        print("FAIL Testfälle:", self.status_fail)

if __name__ == '__main__':

    Gesamt = Gesamtprotokoll()
    Gesamt.test_case()
    Gesamt.display()