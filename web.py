import requests, bs4

# res = requests.get('https://en.wikipedia.org/wiki/List_of_Top_Gear_episodes')
# res.raise_for_status()
# playFile = open('TopGearHTML.txt', 'wb')
# for chunk in res.iter_content(100000):
#         playFile.write(chunk)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

exampleFile = open('TopGearHTML.txt')
soup = bs4.BeautifulSoup(exampleFile.read(),"lxml")
#hacky way to get all the viewers' numbers
elems = soup.findAll('td')[151:][1::7]

filteredList = []

for element in elems:
	elementToAppend = element.getText()[:4]
	#if(isinstance(elementToAppend, double)):
	if(is_number(elementToAppend)):
		filteredList.append(float(elementToAppend))

filteredList.sort()
#print(len(filteredList))
for number in filteredList:
	print(number)