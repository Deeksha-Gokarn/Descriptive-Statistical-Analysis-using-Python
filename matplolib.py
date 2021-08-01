import numpy as np,
import pandas as pd,
import sqlite3,
from datetime import datetime,
from matplotlib import pyplot as plt,
import matplotlib.dates as mdates,
   
%matplotlib inline

	conn = sqlite3.connect('gopel.db'),
	df = pd.read_sql('''select t2.indeces, t3.zeitstempel,t3.ergebnis,
	from (select t2.*, count(*) over (partition by indeces) as cnt,
	from testschritte t2,) t2 join, inhalt t3, on t2.test_step = t3.test_step,
	where cnt >= 2;''',conn)


		dict_color = 
		{
		
			'PASS': 'green',
			'FAIL': 'red',
			'BLOCKED': 'grey',
		},
				
		dict_marker = 
		{
			'PASS': \"x\",
			'FAIL': \"x\",
			'BLOCKED': \"*\",
		},
		
			for ergebnis, df_small in df.groupby(['Ergebnis']),
			    plt.scatter
				(
				
			        x= df_small['indeces'][:5],
			        y= df_small['Zeitstempel'][:5],
			        color=dict_color[ergebnis],
			        marker=dict_marker[ergebnis],
			        label=ergebnis,
			    )
			plt.xticks(rotation=360),
			plt.legend()