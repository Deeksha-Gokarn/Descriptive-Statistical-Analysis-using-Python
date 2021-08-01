from bs4 import BeautifulSoup
from lxml import html
import glob

from testschritte import Testschritte


class Inhalt(Testschritte):

    def __init__(self):

        super().__init__()
        self.page = []
        self.tree = []
        self.soup_files = []
        self.table = None
        self.title = None
        self.span = None
        self.passed = list()
        self.failed = list()
        self.blocked = list()
      
	    # Parsing out the required data using BeautifulSoup Parser
        self.path = r'filepath'
        for filename in glob.glob(self.path):
            with open(filename, 'r') as f:
                page = f.read()
                self.page.append(page)
                tree = html.fromstring(page)
                self.tree.append(tree)
                self.soup_file = BeautifulSoup(page, features="lxml")
                self.soup_files.append(self.soup_file)


    def tables(self):

        self.Makro = list()
        self.Kommentar = list()
        self.ergebnis = list()
        self.Testzeit = list()

        self.Laufzeit = list()
        self.Zeitstempel = list()
        self.Parameters = list()

        self.inhalt_num = [(link.get('href')) for link in self.soup_file.find_all('a')]
        self.title = self.soup_file.find('div').get_text()

        if self.title == "// Testprotokoll":
            print(self.title)
            for t in self.soup_file:
                print(self.soup_file.find('table', class_='mk_zahl').get_text())
        else:
            print("Not the main page")

            # DB
            for soup_file in self.soup_files:
                self.a_tags = soup_file.find_all('span',class_='mk_zahl')
                self.cycle = [str(each.get_text()) for each in self.a_tags]
                self.table = soup_file.findAll(class_="mk_tabelle")
                self.parameters = soup_file.find_all('tt')
                self.table = soup_file.findAll(class_="mk_tabelle")

                items = [column.findAll('td') for column in self.table]
                for i in items:
                    self.makro = i[1].get_text()
                    self.Makro.append(self.makro)
                    self.kommentar = i[3].get_text()
                    self.Kommentar.append(self.kommentar)
                    self.Ergebnis = i[5].get_text()
                    self.ergebnis.append(self.Ergebnis)
                    if self.Ergebnis == "PASS" or self.Ergebnis == "BLOCKED":
                        self.testzeit = i[7].get_text().strip('\n')
                        self.Testzeit.append(self.testzeit)
                        self.laufzeit = i[17].get_text().strip('\n')
                        self.Laufzeit.append(self.laufzeit)
                        self.zeitstempel = i[27].get_text().strip('\n')
                        self.Zeitstempel.append(self.zeitstempel)
                    elif self.Ergebnis == "FAIL":
                        self.testzeit_failed = i[9].get_text().strip('\n')
                        self.Testzeit.append(self.testzeit_failed)
                        self.laufzeit_failed = i[19].get_text().strip('\n')
                        self.Laufzeit.append(self.laufzeit_failed)
                        self.zeitstempel_failed = i[29].get_text().strip('\n')
                        self.Zeitstempel.append(self.zeitstempel_failed)

                #Parameters
                for each in self.parameters:
                    Parameter = [str(each.get_text().strip('\n'))]
                    self.Parameters.append(Parameter)

    def auto_tables(self):

        for soup_file in self.soup_file:

            self.auto = soup_file.find('div').get_text()

            if self.auto == "Automation":
                for table in soup_file.select('table.mk_tab_Auto'):
                    self.rows = table.select('tr')
                    self.headers = [td.text for td in self.rows[0].select('td.mk_tab_Auto_head')]
                    for row in self.rows[1:]:
                        self.values = [td.text for td in row.select('td.mk_tab_Auto_body')]
                        print(dict(zip(self.headers, self.values)))
            else:
                print("None")


    def display(self):

        print("Makro:",self.Makro)
        print("Kommentar:",self.Kommentar)
        print("Ergebnis:", self.ergebnis)
        print("Testzeit_Pass:", self.Testzeit)
        print("Laufzeit:", self.Laufzeit)
        print("Zeitstempel:", self.Zeitstempel)
        print("Parameter:", self.Parameters)

	# Extracting required elements by Pattern Matching 
	  
	 def pattern_extract(self)
	  
	  pattern_one = re.compile(r'Inhalt\d.[a-z]\w+#Step\d{1,4}:\d{1,4}\s#?(Absatzmarke|[A-Z]\w+#?)')
	  path = r'filepath'
		for filename in glob.glob(path):
			with open(filename,'r') as f:
				contents = f.read()

				matches_one = pattern_one.finditer(contents)
				for match in matches_one:
					print(match)
					

contents = Inhalt()
contents.tables()
contents.auto_tables()
contents.display()