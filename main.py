import pandas as pd
from datetime import *

def get_data(ritasi, fn):
	ritasi = ritasi + ((ritasi-1)*14)
	df = pd.read_csv(fn)
	df = df.drop([0,1])
	df = slice_by_ritasi(ritasi,df)
	return df

def slice_by_ritasi(ritasi, df):
	column_name = []
	for i in range(ritasi-1,ritasi+13):
		column_name.append("Unnamed: "+str(i))
	return df[column_name]


def create_population(ritasi):
	for fn in range(1,14):
		df = get_data(ritasi,'./'+fn+'.csv')
		df = df.iloc[:,[1,2]].dropna()

		label = df.iloc[:,0].to_list()
		value = df.iloc[:,1].to_list()
		value  = [datetime.strptime(str(item), "%H:%M:%S %p") for item in value]


		starter_value = value[0]

		for i,item in enumerate(value):
			value[i] = int(((item - starter_value).total_seconds()) / 60)


create_population(1)