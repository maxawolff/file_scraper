from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

def get_a_job():
    job_dict = {}
    count = 1
    url = "https://stackoverflow.com/jobs?pg=1"
    for i in range(1, 11):
        url = url[:34]
        url += str(i)
        content = urlopen(url)
        soup = BeautifulSoup(content)
        titles = []
        mydivs = soup.findAll("div", { "class" : "-job-summary" })
        for div in mydivs:
            a_tag = div.findAll('a')
            company_div = div.findAll("div", { "class" : "-company" })
            title = a_tag[0]['title']
            titles.append(title)
        job_dict[count:titles]
        job_dict
    return job_dict


if __name__ == '__main__':
    get_a_job()
