import pprint
import zulip
import sys
import re
import json
import httplib2
import os
from topnews import News

BOT_MAIL = "neo-bot@bint.zulipchat.com"

class Neo(object):
    '''
    A docstring documenting this bot.
    '''

    def __init__(self):
        self.client = zulip.Client(site="https://bint.zulipchat.com/api/")
        self.subscribe_all()
        self.trans = Translate()
        self.news = News()
        self.subKeys=["hello","sample"]
    
    #  This will subscribe and listen to messages on all streams.
    def subscribe_all(self):
        json = self.client.get_streams()["streams"]
        streams = [{"name": stream["name"]} for stream in json]
        self.client.add_subscriptions(streams)

    def process(self, msg):
		# array  consisting of all the words
        content = msg["content"].split()
        sender_email = msg["sender_email"]
        ttype = msg["type"]
        stream_name = msg['display_recipient']
        stream_topic = msg['subject']
        if sender_email== BOT_MAIL:
            return 

        if content[0].lower() == "neo" or content[0] == "@**neo**":
            if content[1].lower() == "hello":
                message="Hi"
                self.client.send_message({
                    "type": "stream",
                    "subject": msg["subject"],
                    "to": msg["display_recipient"],
                    "content": message
                    })
            if content[1].lower() == "news":
                news = self.news.getTopNews()
                message = ""
                for item in news:
                    message += "**"+item.title+"**"
                    message += '\n'
                    message += item.des
                    message += '\n\n'
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