import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

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

class DataAnalyzer:

    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def analyze_data(self):
        print(self.data.describe(include='all'))

    def visualize_data(self):
        self.data['LowTemp'] = pd.to_numeric(self.data['LowTemp'])
        self.data['HighTemp'] = pd.to_numeric(self.data['HighTemp'])
        
        self.data['AvgTemp'] = (self.data['LowTemp'] + self.data['HighTemp']) / 2
        sorted_data = self.data.sort_values(by='AvgTemp')

        plt.figure(figsize=(12, 7))
        plt.barh(sorted_data['LocationLink'].str.split('/').str[-3], sorted_data['AvgTemp'], color='skyblue')
        plt.xlabel('Durchschnittstemperatur (°C)')
        plt.title('Durchschnittstemperatur in verschiedenen Städten')
        plt.tight_layout()
        plt.show()
