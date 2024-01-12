from bs4 import BeautifulSoup
import requests
url  = "https://www.flipkart.com/camera-clp-store"
response = requests.get(url)
#print(response.status_code)
#print(response.content)
html_content = response.content
soup = BeautifulSoup(html_content , 'html.parser')
print(soup.prettify()) #to get a better view of the code 
print(soup.title) #for fetching the title of the webpage 
print(soup.title.parent.name)
#for fetching the link of all the images in the webpage 
for image in soup.find_all('img'):
    print(image.get('src'))

titles = []
prices = []
images = []

for d in soup.find_all('div', attrs = {'class': '_2kHMtA'}):
  print(d)