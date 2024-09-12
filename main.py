import requests
from bs4 import BeautifulSoup
import json

class AsprinScraper:
    def __init__(self):
        self.base_url = "https://medlineplus.gov/druginfo/meds/a682878.html"

    def get_source(self, url):
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                return BeautifulSoup(r.content, 'lxml')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def get_name(self, source):
        try:
            return source.find("h1", attrs={"class":"with-also"}).text
        except Exception:
            return None

    def get_section_info(self, source, id_element):
        try:
            section = source.find("div", attrs={"id": id_element})
            if section:
                title = section.find("h2").text
                content = section.find("p").text
                return dict(
                    title=title,
                    content=content
                )
        except Exception:
            return None

    def scrape_data(self):
        result = []
        source = self.get_source(self.base_url)
        if not source:
            return result
        
        name = self.get_name(source)
        section_ids = ['why', 'how', 'other-uses', 'precautions', 'special-dietary', 'if-i-forget', 'side-effects', 'storage-conditions', 'overdose', 'other-information']
        
        sections = []
        for section_id in section_ids:
            section_info = self.get_section_info(source, section_id)
            if section_info:
                sections.append(section_info)
        
        result.append(dict(
            name=name,
            sections=sections
        ))

        return result

    def write_as_json(self, data, filename="result.json"):
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=2)

if __name__ == '__main__':
    scraper = AsprinScraper()
    data = scraper.scrape_data()
    scraper.write_as_json(data, filename="result.json")
