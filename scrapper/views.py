from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
# Create your views here.
page =  requests.get("https://timesofindia.indiatimes.com/travel/kochi/weather")
soup = BeautifulSoup(page.content, 'html.parser')
temp1 = soup.find_all(class_='_temp')[0].get_text()
data = soup.find_all(class_="weather_list")[0].find_all("strong")
hum1 = data[0].get_text()
uv1 = data[1].get_text()
rain1 = data[2].get_text()
w1 = data[3].get_text()

page =  requests.get("https://timesofindia.indiatimes.com/travel/delhi/weather")
soup = BeautifulSoup(page.content, 'html.parser')
temp2 = soup.find_all(class_='_temp')[0].get_text()
data = soup.find_all(class_="weather_list")[0].find_all("strong")
hum2 = data[0].get_text()
uv2 = data[1].get_text()
rain2 = data[2].get_text()
w2 = data[3].get_text()

page =  requests.get("https://timesofindia.indiatimes.com/travel/mumbai/weather")
soup = BeautifulSoup(page.content, 'html.parser')
temp3 = soup.find_all(class_='_temp')[0].get_text()
data = soup.find_all(class_="weather_list")[0].find_all("strong")
hum3 = data[0].get_text()
uv3 = data[1].get_text()
rain3 = data[2].get_text()
w3 = data[3].get_text()
def main(request):
    context={
        "temp1": temp1,
        "hum1": hum1,
        "uv1" : uv1,
        "rain1": rain1,
        "w1": w1,
        "temp2": temp2,
        "hum2": hum2,
        "uv2" : uv2,
        "rain2": rain2,
        "w2": w2,
        "temp3": temp3,
        "hum3": hum3,
        "uv3" : uv3,
        "rain3": rain3,
        "w3": w3,
    }
    return render(request, 'home/index.html', context)