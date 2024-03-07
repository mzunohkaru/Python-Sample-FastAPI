import requests
from config import APP_ID

URL = 'https://app.rakuten.co.jp/services/api/Travel/KeywordHotelSearch/20170426'

params = {
    'applicationId': APP_ID,
    'keyword': '沖縄'
}

res = requests.get(URL, params)

print(res.status_code)

allData = res.json()


hotels = allData['hotels']
firstHotelsData = hotels[0]
hotelListData = firstHotelsData['hotel']
firstHotelListData = hotelListData[0]
hotelBasicInfoData = firstHotelListData['hotelBasicInfo']

print(hotelBasicInfoData)


hotel = allData['hotels'][0]['hotel'][0]['hotelBasicInfo']
hotelName = hotel['hotelName']
hotelAccess = hotel['access']
hotelAddress = hotel['address1']+hotel['address2']

print(hotelAddress)