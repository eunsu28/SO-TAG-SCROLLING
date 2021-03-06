import requests
from bs4 import BeautifulSoup
import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode = "w")
    writer = csv.writer(file)
    writer.writerow(["title"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return 

limited = 50
url = "https://stackoverflow.com/questions/tagged/beautifulsoup?tab=newest&pagesize=50"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
last_pages = pages[-2].get_text(strip=True)
final = int(last_pages)

print(type(final))

def extract_job(result):
    title = result.find("a", {"class":"question-hyperlink"}).text
    return {"title" : title}

jobs = []
for page in range(final):
    print(f"Scrapping SO Page: {page}")
    result = requests.get(f"{url}?tab=newest&page={page + 1}&pagesize=50")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"summary"})
    for result in results:
       job = extract_job(result)
       jobs.append(job)
       

save_to_file(jobs)

print(jobs)