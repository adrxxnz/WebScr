# I'll use BS and Request to get Jobs which are looking for people with Python on a website
import requests
from bs4 import BeautifulSoup


html_text = requests.post('https://www.infojobs.net/jobsearch/search-results/list.xhtml').text

soup = BeautifulSoup(html_text, 'lxml')

#Only 1 job post
job = soup.find('li', class_='ij-List-item')

classJob = job.find('h2', class_='ij-OfferCardContent-description-title')
titleJob = classJob.find('a', class_ = 'ij-OfferCardContent-description-title-link').text

skills = job.find()



print(titleJob)
