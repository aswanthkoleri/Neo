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

client = zulip.Client(config_file="~/.zuliprc")
BOT_MAIL = "neo-bot@bint.zulipchat.com"
class Neo(object):
    '''
    A docstring documenting this bot.
    '''
    def __init__(self):
        self.client = zulip.Client(site="https://bint.zulipchat.com/api/")
        self.subscribe_all()
        self.subKeys=["hello","sample"]

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
            message = ""
            

# First get 

