import webbrowser

#a list of the websites
websites_list = ["http://team-bhp.com", "http://autocar.co.uk", "https://www.reddit.com/r/Jokes/"
, "http://www.theverge.com", "http://www.topgear.com/car-news"]

for address in websites_list:
	webbrowser.open(address)