import requests
from bs4 import BeautifulSoup

limited = 50
url = "https://stackoverflow.com/questions/tagged/beautifulsoup"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
last_pages = pages[-1].get_text(strip=True)
int(last_pages)

def extract_job(html):
  title = html.find("div", {"class":"summary"}).find("a")["question-hyperlink"]
  job_id = html.find("a")


jobs = []
for page in range(last_pages):
    print(f"Scrapping SO Page: {page}")
    result = requests.get(f"{url}&pg={page + 1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
       job = extract_job(result)
       jobs.append(job)

print(jobs)