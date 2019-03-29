import requests

class Item:
    def __init__(self,title,des):
        self.title = title
        self.des = des

class News():
    def getTopNews(self):
        news = []
        results = requests.get('https://newsapi.org/v2/everything?q=bitcoin&from=2019-02-28&sortBy=publishedAt&apiKey=dd5021d0806649dcbbfbdb18d9fd4055')
        data = results.json()
        for i in range(10):
            #print(data["articles"][i]["title"])
            news.append(Item(data["articles"][i]["title"],data["articles"][i]["description"]))
        return news
            
if __name__ == "__main__":
    n = News()
    r = n.getTopNews()
    print(r)