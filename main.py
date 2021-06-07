import requests
from bs4 import BeautifulSoup

limited = 50
url = "https://stackoverflow.com/questions/tagged/beautifulsoup"

def extract_job(html):
  title = html.find("div", {"class":"summary"}).find("a")["question-hyperlink"]
  job_id = html.find("a")


result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
last_pages = pages[-2].get_text(strip=True)
final = int(last_pages)

print(type(final))

jobs = []
for page in range(final):
    print(f"Scrapping SO Page: {page}")
    result = requests.get(f"{url}&pg={page + 1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
       job = extract_job(result)
       jobs.append(job)

print(type(final))