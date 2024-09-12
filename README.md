# AsprinScraper (Web Scraper Example)
## English
This project has been prepared as a Python example that saves the information about the drug called "Asprin" on the Medline Plus web page as a JSON file by taking data from the URL with the data scraping technique.
### Requirements
- Python 3.x
- requests 
- beautifulsoup4
- lxml
To Install the required packages:
```bash
pip install requests beautifulsoup4 lxml
```
### Setup
1. Clone the project repository:
```bash
git clone <repository-url>
cd web-scraper
```
2. Install the required libraries:
```bash
pip install -r requirements.txt
```
### Usage
Run the main script data and save it to a JSON file:
```bash
python main.py
```
### Code Explanation
#### Import
```Python 
import requests
from bs4 import BeautifulSoup
import json
```
#### Class Definition, Constructor and Base URL Definition
```Python 
class AsprinScraper:
    def __init__(self):
        self.base_url = "https://medlineplus.gov/druginfo/meds/a682878.html"
```
Create a class named "AspirinScraper", and then defined the constructor and base url.
#### Loading Data
```Python 
def get_source(self, url):
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                return BeautifulSoup(r.content, 'lxml')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
```
This function fetches the HTML content of the URL and parses it using BeautifulSoup.
#### Extracting Information
##### Title Info
```Python 
def get_name(self, source):
        try:
            return source.find("h1", attrs={"class":"with-also"}).text
        except Exception:
            return None
```  
This function extracts the medication name ("asprin") from HTML content.
##### Section Info
```Python 
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
```  
This function extracts information from different section of the web page.

#### Data Scraping and Saving
##### Data Scraping
```Python 
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
``` 
This function performs data scraping.
##### Saving 
```Python 
 def write_as_json(self, data, filename="result.json"):
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=2)
``` 
This function creates a JSON file and saves the data by writing it into it.
#### Operating the Module
```Python
if __name__ == '__main__':
    scraper = AsprinScraper()
    data = scraper.scrape_data()
    scraper.write_as_json(data, filename="result.json")
```
This codeline checks if the Python file is being run directly.

### Contributors
Contributors to this Projects
Elif Nehir OĞUZ

### License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
---------------------------------------------------------------------------------------------------------------------------------------------------
## Türkçe
Bu proje, Medline Plus web sayfasında yer alan "Asprin" isimli ilaç hakkındaki bilgileri, veri kazıma tekniği ile URL'den veri alarak JSON dosyası olarak kaydeden bir Python örneği olarak hazırlanmıştır.
### Gereksinimler
- Python 3.x
- requests 
- beautifulsoup4
- lxml
Gerekli paketleri kurmak için:
```bash
pip install requests beautifulsoup4 lxml
```
### Kurulum
1. Proje deposunu klonlayın:
```bash
git clone <repository-url>
cd web-scraper
```
2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```
### Kullanım
Ana komut dosyası verilerini çalıştırın ve bir JSON dosyasına kaydedin:
```bash
python main.py
```
### Kod Açıklaması
#### Import (İçe Aktarmak)
```Python 
import requests
from bs4 import BeautifulSoup
import json
```
#### Sınıf Tanımı, Yapıcı ve Temel URL Tanımı
```Python 
class AsprinScraper:
    def __init__(self):
        self.base_url = "https://medlineplus.gov/druginfo/meds/a682878.html"
```
"AspirinScraper" adında bir sınıf oluşturun ve ardından yapıcıyı ve temel URL'yi tanımlayın.
#### Veri Yükleme
```Python 
def get_source(self, url):
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                return BeautifulSoup(r.content, 'lxml')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
```
Bu işlev, URL'nin HTML içeriğini getirir ve BeautifulSoup'u kullanarak ayrıştırır.
#### Bilgi Çıkarma
##### Başlık Bilgisi
```Python 
def get_name(self, source):
        try:
            return source.find("h1", attrs={"class":"with-also"}).text
        except Exception:
            return None
```  
Bu işlev, ilaç adını ("asprin") HTML içeriğinden çıkarır.
##### Bölüm Bilgisi
```Python 
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
```  
Bu işlev, web sayfasının farklı bölümlerinden bilgi çıkarır.
#### Veri Kazıma ve Kaydetme
##### Veri Kazıma
```Python 
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
``` 
Bu fonksiyon veri kazıma işlemini gerçekleştirir.
##### Kaydetme 
```Python 
 def write_as_json(self, data, filename="result.json"):
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=2)
``` 
Bu işlev bir JSON dosyası oluşturur ve verileri bu dosyaya yazarak kaydeder.
#### Operating the Module
```Python
if __name__ == '__main__':
    scraper = AsprinScraper()
    data = scraper.scrape_data()
    scraper.write_as_json(data, filename="result.json")
```
Bu kod satırı Python dosyasının doğrudan çalıştırılıp çalıştırılmadığını kontrol eder.

### Katkıda Bulunanlar
Bu projede katkıda bulunanlar:
- Elif Nehir OĞUZ

### Lisans
Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisanslanmıştır.

### NOT
Bu örnekte, README dosyasını hem İngilizce hem de Türkçe olarak iki dilde hazırladım. Bölümler arasında ayırıcı çizgiler ('-------') kullanarak iki dili ayırt edebilirsiniz.
