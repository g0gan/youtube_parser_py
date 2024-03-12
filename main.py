import requests
from bs4 import BeautifulSoup
import csv

def parse_video_titles_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    
    with open('youtube_results.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['URL', 'Название видео'])
        
        for url in urls:
            url = url.strip()
            if url.startswith('https://www.youtube.com/watch?v='):
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    title_tag = soup.find('meta', property='og:title')
                    video_title = title_tag['content'] if title_tag else 'Название не найдено'
                    csv_writer.writerow([url, video_title])
                else:
                    csv_writer.writerow(['Ошибка при загрузке страницы', url])

if __name__ == "__main__":
    file_path = 'youtube_links.txt'  # Укажите путь к вашему файлу с ссылками
    parse_video_titles_from_file(file_path)
