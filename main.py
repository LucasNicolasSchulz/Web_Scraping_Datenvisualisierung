from bs4 import BeautifulSoup
import requests

#URL
url = 'https://www.wetter.ch/'

#Get request
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

cloud_elements = soup.find_all('div', class_='bigmap_citybox')

cloud_data = []

for cloud in cloud_elements:
    style_content = cloud['style']
    image_url = style_content.split('background-image:url(')[1].split(')')[0]
    location_link = cloud.find('div', class_='bigmap_city_tempsbox').find_next_sibling()['onclick'].split("'")[1]
    temp_low = cloud.find('div', class_='bigmap_city_templowbox').text
    temp_high = cloud.find('div', class_='bigmap_city_temphighbox').text

    cloud_data.append({
        'ImageURL': 'https://www.wetter.ch' + image_url,
        'LocationLink': 'https://www.wetter.ch' + location_link,
        'LowTemp': temp_low,
        'HighTemp': temp_high
    })

for data in cloud_data[:5]:
    print(data)
