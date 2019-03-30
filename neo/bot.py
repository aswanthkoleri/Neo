import pprint
import zulip
import sys
import re
import json
import httplib2
import os
from topnews import News
from todo import Todo,displayTodo
from translate import Translate
from location import Location
from weather import fetch_api_key, get_weather
from currencyExchange import fetch_currency_exchange_rate
from summarizer import summarizeDoc
from digest import digest
client = zulip.Client(config_file="~/.zuliprc")

BOT_MAIL = "neo-bot@bint.zulipchat.com"

class Neo(object):
    '''
    A docstring documenting this bot.
    '''

    def __init__(self):
        self.client = zulip.Client(site="https://bint.zulipchat.com/api/")
        self.subscribe_all()
        self.translate = Translate()
        self.location = Location()
        self.news = News()
        self.subKeys=["hello","sample"]
        self.todoList=[]
    
    #  This will subscribe and listen to messages on all streams.
    def subscribe_all(self):
        json = self.client.get_streams()["streams"]
        streams = [{"name": stream["name"]} for stream in json]
        self.client.add_subscriptions(streams)

    def process(self, msg):
		# array  consisting of all the words
        message_id=msg["id"]
        content = msg["content"].split()
        sender_email = msg["sender_email"]
        ttype = msg["type"]
        stream_name = msg['display_recipient']
        stream_topic = msg['subject']
        if sender_email== BOT_MAIL:
            return 

        if content[0].lower() == "neo" or content[0] == "@**neo**":
            message = ""
            if content[1].lower() == "hello":
                message="Hi"
            elif content[1].lower() == "news":
                try:
                    news = self.news.getTopNews()
                    for item in news:
                        message += "**"+item.title+"**"
                        message += '\n'
                        message += item.des
                        message += '\n\n'
                except:
                    message = "Unable to get news"
           
            elif content[1].lower() == "translate":
                try:
                    message = content[2:]
                    message = " ".join(message)
                    print(message)
                    message = self.translate.translateMsg(message)
                except:
                    message = "Type in following format : neo translate **word**"
            
            elif content[1].lower() == "weather":
                api_key = fetch_api_key()
                if len(content) > 2 and content[2].lower() != "":
                    # Query format: Neo weather London
                    weather = get_weather(api_key, content[2].lower())
                    if str(weather['cod']) != "404":
                        message += "[](http://openweathermap.org/img/w/{}.png)".format(weather['weather'][0]['icon'])
                        message += "**Weather report for {}**\n".format(content[2].lower())
                        message += "Temperature: **{}**\n".format(str(weather['main']['temp']) + "° C")
                        message += "Pressure: **{}**\n".format(str(weather['main']['pressure']) + " hPa")
                        message += "Humidity: **{}**\n".format(str(weather['main']['humidity']) + "%")
                        message += "Wind Speed: **{}**".format(str(weather['wind']['speed']) + " $$m/s^2$$")
                    else:
                        message = "City not found!\nabc"
                else:
                    message = "Please add a location name."
            
            elif content[1].lower() == "geolocation":
                try:
                    place = content[2]
                    result = self.location.getLocation(place)
                    message = ""
                    message += "**Latitude** : "+str(result.lat)+"\n"+"**Longitude** : "+str(result.lng)
                except:
                    message = "Type a correct place in following format : neo geolocation **place**"
            
            elif content[1].lower() == "currency":
                if len(content) == 3 and content[2].lower() != "":
                    # Query format: Neo currency USD
                    currency = fetch_currency_exchange_rate("", content[2].upper())
                    message += "**Showing all currency conversions for 1 {}:**\n".format(content[2].upper())
                    for curr in currency['rates']:
                        message += "1 {} = ".format(content[2].upper()) + "{}".format(format(currency['rates'][curr], '.2f')) + " {}\n".format(curr)
                    message += "Last Updated: *{}*".format(currency['date'])
                elif len(content) == 5 and content[2].lower() != "" and content[4].lower() != "":
                    # Query format: Neo currency INR to USD
                    currency = fetch_currency_exchange_rate(content[2].upper(), content[4].upper())
                    message += "1 {} = ".format(content[4].upper()) + "{}".format(format(currency['rates'][content[2].upper()], '.2f')) + " {}\n".format(content[4].upper())
                    message += "Last Updated: *{}*".format(currency['date'])
                else:
                    message = "Please ask the query in correct format."
            
            elif content[1].lower() == "todo":
                # Has to do some more modifications 
                if content[2].lower() == "add":
                    todoItem=" ".join(content[3:]).lower()
                    Todo("add",self.todoList,todoItem)
                    message="** The todo is added **\n The current Todo List is :\n\n"
                    message=displayTodo(message,self.todoList)
                elif content[2].lower() =="done":
                    if content[3].lower().isdigit(): 
                        itemNo=int(content[3].lower())
                        # print(itemNo)
                        message+="** The item is marked as done **\n"
                        Todo("done",self.todoList,"",itemNo)
                        message=displayTodo(message,self.todoList)
                    else:
                        message="Enter the Todo item number"
                elif content[2].lower() =="undone":
                    if content[3].lower().isdigit(): 
                        itemNo=int(content[3].lower())
                        # print(itemNo)
                        message+="** The item is marked as undone **\n"
                        Todo("undone",self.todoList,"",itemNo)
                        message=displayTodo(message,self.todoList)
                    else:
                        message="Enter the Todo item number"
                elif content[2].lower() == "remove":
                    if content[3].lower()!="all":
                        if content[3].lower().isdigit():
                            itemNo=int(content[3].lower())
                            Todo("remove",self.todoList,"",itemNo)
                            message="** The todo item is removed **\nThe current Todo List is :\n\n"
                            message=displayTodo(message,self.todoList)
                        else:
                            message="Enter the Todo item number"
                    elif content[3].lower() == "all":
                        Todo("remove_all",self.todoList,"",itemNo)
                        message="The Todo list is cleared"
                    else:
                        message="Invalid todo command"
                else:
                    message="Invalid todo command."
            elif content[1].lower()=="summarize":
                try:
                    sentenceCount=int(content[2].lower())
                    summarizerType=content[3].upper()
                    document=" ".join(content[4:]).lower()
                    summary=summarizeDoc(summarizerType,document,sentenceCount)
                    message="The summary is:\n"+summary
                except:
                    message="Something went wrong with the command you typed. Please check"
            elif content[1].lower()=="digest":
                # Get all users
                (message,summary)=digest(stream_name,message_id,sender_email)
                message+="\n** The summary of the messages is : **\n"+summary
            else:
                message="HELP option"
            self.client.send_message({
                "type": "stream",
                "subject": msg["subject"],
                "to": msg["display_recipient"],
                "content": message
            })

def main():
    neo= Neo()
    neo.client.call_on_each_message(neo.process)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Thanks for using Neo Bot. Bye!")
		sys.exit(0)