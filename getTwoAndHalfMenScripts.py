from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=two-and-a-half-men&episode="

regex = re.compile('^scrolling-script-container')

def getScriptsInList():
	content = []
	for i in range(3):# number of seasons
		for j in range(9): # episodes from 1 to 9
			try:
			    page = urllib.request.urlopen(url+"s0"+str(i+1)+"e"+"0"+str(j+1))
			except:
			    print("An error occured.")

			soup = BeautifulSoup(page, 'html.parser')
			# for br in soup.find_all("\n"):
			# 	br.replace_with(" ")
			for br in soup.find_all("br"):
			    br.replace_with("\n")
			content_lis = soup.find_all('div', attrs={'class': regex})
			for li in content_lis:
			    content.append(li.getText())
			print("episode number "+str(j+1)+" of season "+str(i+1)+" done.")

		for k in range(9,24): # episodes from 9 to 24
			try:
			    page = urllib.request.urlopen(url+"s0"+str(i+1)+"e"+str(k+1))
			except:
			    print("An error occured. and page is ",url+"s0"+str(i+1)+"e"+str(k+1))

			soup = BeautifulSoup(page, 'html.parser')
			content_lis = soup.find_all('div', attrs={'class': regex})
			for li in content_lis:
			    content.append(li.getText())
			print("episode number "+str(k+1)+" of season "+str(i+1)+" done.")

	return content

def writeInFile(fileName,contents):
	file=open(fileName,"w",encoding='utf-8')
	# print(type(content[0]))
	for i in contents:
		file.write(i)
		file.write("\n\n")
	file.close()

scrappedScripts=getScriptsInList()
writeInFile("scriptsFor3Seasons.txt",scrappedScripts)