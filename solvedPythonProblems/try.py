# def a()
#     b() + c()
#
# def b():
#     return 3
#
# def c():
#     return 7 * b()
#
# print (a())
# import csv

# import requests
# from bs4 import BeautifulSoup

# url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
# response = requests.get(url)
# html = response.content

# soup = BeautifulSoup(html)
# table = soup.find('tbody', attrs={'class': 'stripe'})

# list_of_rows = []
# for row in table.findAll('tr')[1:]:
#     list_of_cells = []
#     for cell in row.findAll('td'):
#         text = cell.text.replace('&nbsp;', '')
#         list_of_cells.append(text)
#     list_of_rows.append(list_of_cells)

# outfile = open("./inmates.csv", "wb")
# writer = csv.writer(outfile)
# writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
# writer.writerows(list_of_rows)
# for i in range(3):
# 	print("Rawat")
# 	for i in range(2):
# 		print("Akhil")
# a = open('abcd.txt', 'w+')
# a.write("Akhil")
# a.write("Rawat")
a = ["a","b","a","c"]
a.pop(a.index("a"))
print(a)