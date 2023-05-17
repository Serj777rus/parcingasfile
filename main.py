import requests
from bs4 import BeautifulSoup
import re

news_sites = ['https://www.bbc.com/news', 'https://www.reuters.com/', 'https://www.aljazeera.com/'] # список новостных сайтов
output_file = 'news_links.txt' # имя файла, в который будут сохраняться ссылки на новости
links = [] # список для хранения ссылок на новости

# проходим по каждому сайту из списка news_sites
for site in news_sites:
    # загружаем страницу сайта
    response = requests.get(site)
    if response.status_code == 200:
        # преобразуем HTML-код страницы в объект BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # ищем все ссылки на странице
        for link in soup.find_all('a'):
            href = link.get('href')
            # проверяем, является ли ссылка на новость
            if href and ('/news/' in href or '/article/' in href):
                # добавляем ссылку в список
                full_link = re.sub(r'^//', 'https://', href)
                links.append(full_link)

# сохраняем список ссылок в файл
with open(output_file, 'w') as file:
    file.write('\n'.join(links))
