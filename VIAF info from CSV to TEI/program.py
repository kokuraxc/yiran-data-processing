import csv
import xml.etree.ElementTree as et

import pandas as pd
df = pd.read_csv('Copy of 人物数据1.0_VIAF.csv')
df = df.dropna(subset=['NodeID 人物编号'])
df['VIAF'] = df['VIAF'].replace(pd.np.nan, '', regex=True)
print(df['VIAF'])
df['NodeID 人物编号'] = df['NodeID 人物编号'].fillna(-10.0).astype(int)
df['NodeID 人物编号'] = '00000' + df['NodeID 人物编号'].astype(str)
df['NodeID 人物编号'] = 's' + df['NodeID 人物编号'].str.slice(-6)
saved_column = df['NodeID 人物编号'] #df.column_name #you can also use df['column_name']

di = df.set_index('NodeID 人物编号')['VIAF'].to_dict()


# print(saved_column)
# print(df)


et.register_namespace('',"http://www.tei-c.org/ns/1.0")
tree = et.parse('sbdbTEI.xml')
root = tree.getroot()

for person in root.iter('{http://www.tei-c.org/ns/1.0}person'):
	name = person.get('xml:id')
	nodeid = person.get('{http://www.w3.org/XML/1998/namespace}id')
	#if nodeid in di:
		#print(nodeid + ', ' + str(di[nodeid]))
	for idno in person.findall('{http://www.tei-c.org/ns/1.0}idno'):
		if (idno.attrib['type'] == 'VIAF') and (nodeid in di):
			# print(idno.attrib)
			idno.text = str(di[nodeid])

tree.write('output.xml', encoding="UTF-8", xml_declaration=True, method="xml")

with open('output.xml', 'r') as fread:
	data = fread.read().replace(' />', '/>')
	with open('output_r.xml', 'w+') as fwrite:
		fwrite.write(data)