from BeautifulSoup import BeautifulSoup

html = open('utubedsilva.html','r')
soup = BeautifulSoup(html)
vidTitle = soup.findAll(id="eow-title")
print vidTitle[0].get('title')
