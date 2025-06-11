import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Lỗi khi tải trang: {url}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes_data = []

    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        quotes_data.append({'quote': text, 'author': author})

    return quotes_data

if __name__ == "__main__":
    base_url = "https://quotes.toscrape.com/page/"
    all_quotes = []

    for page in range(1, 4):  # scrape 3 pages
        url = f"{base_url}{page}/"
        print(f"Đang thu thập dữ liệu từ: {url}")
        quotes = scrape_quotes(url)
        all_quotes.extend(quotes)

    for q in all_quotes:
        print(f"{q['quote']} — {q['author']}")
