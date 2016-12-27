import requests, bs4
import json

grid_file = open('grid.txt')
soup = bs4.BeautifulSoup(grid_file.read(),"lxml")

#get all the table data entries (each cell)
td_elements = soup.findAll('td')
#get all the input entries that are nested inside the td
input_elements = soup.findAll('input')

counter = 0;
entries = []

for td_element in td_elements:
	#get the row and column for the current data entry
	row = td_element.get('id')[2:]
	column = td_element.get('id')[1:2]
	#this will be the pre-filled value (if any)
	value = input_elements[counter].get('value')
	counter += 1
	data = json.dumps({"row": row, "column": column, "value": value}, sort_keys=True)
	entries.append(data)

with open('medium/5.json', 'w') as f:
		json.dump(entries, f)
		f.close()