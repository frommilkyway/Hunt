import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

base_url = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&search_period=7&text=python&page=0'


def hunt_parse(base_url, headers):
    jobs = []
    session = requests.session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find(
                'a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find(
                'a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find(
                'a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            text1 = div.find(
                'div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            text2 = div.find(
                'div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            content = text1 + ' ' + text2
            jobs.append({
                'title': title,
                'href': href,
                'company': company,
                'content': content
            })
            print(jobs)
    else:
        print('ERROR')


hunt_parse(base_url, headers)
