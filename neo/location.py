import requests

class LngNLat:
    def __init__(self,lat,lng):
        self.lat = lat
        self.lng = lng

class Location():
    def getLocation(self,place):
        results = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+place+',+CA&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU')
        data = results.json()
        print(data["results"][0]["geometry"]["location"]["lat"])
        print(data["results"][0]["geometry"]["location"]["lng"])
        return LngNLat(data["results"][0]["geometry"]["location"]["lat"],data["results"][0]["geometry"]["location"]["lng"])

# if __name__ == "__main__":
#     n = Location()
#     r = n.getLocation('allahabad')
#     print(r)
