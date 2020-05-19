from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

url = input("What indeed url would you like to search: ").strip()
initurl = url; 

start = 0;
job_no = 0;
page_num = 0;
npo_jobs = {}

while True:
	response = requests.get(url)
	data = response.text
	soup = BeautifulSoup(data, 'html.parser')
	jobs = soup.find_all("div", {'class' : 'jobsearch-SerpJobCard'})

	for j in jobs:
		title = j.find('h2', {'class' : 'title'}).text.strip()
		company = j.find('span', {'class' : 'company'}).text.strip()
		desc = j.find('div', {'class' : 'summary'}).text.strip()

		job_no +=1
		npo_jobs[job_no] = [title, company, desc]

		print('Title: ',title+str(job_no),'\n','Company: ',company,'\n','Description: ',desc,'\n----------')

	if soup.find("a", {'aria-label' : 'Next'}):
		page_num += 10
		url = initurl+"&start={}".format(page_num)
	else:
		break

npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient = 'index', columns = ['Job Title', 'Company', 'Description'])
npo_jobs_df.to_csv('indeedJobs.csv')