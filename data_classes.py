import pandas as pd
import requests
from bs4 import BeautifulSoup

class DataExtractor:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        cloud_elements = soup.find_all('div', class_='bigmap_citybox')
        
        cloud_data = []
        for cloud in cloud_elements:
            style_content = cloud['style']
            image_url = style_content.split('background-image:url(')[1].split(')')[0]
            location_link = cloud['onclick'].split("'")[1]
            
            temp_low = cloud.find('div', class_='bigmap_city_templowbox').text
            temp_high = cloud.find('div', class_='bigmap_city_temphighbox').text

            cloud_data.append({
                'ImageURL': 'https://www.wetter.ch' + image_url,
                'LocationLink': 'https://www.wetter.ch' + location_link,
                'LowTemp': temp_low,
                'HighTemp': temp_high
            })

        return cloud_data

class DataAnalisierer:
    def __init__(self, data):
        self.data = data
        self.df = pd.DataFrame(self.data)

    def get_statistics(self):
        return self.df.describe()
