# NEO BOT

<img src="https://user-images.githubusercontent.com/20956124/55281725-cba30300-535e-11e9-9fb6-d55e0a03aeb8.png">

A Zulip bot created in HackInTheNorth 4.0 by Team SedLyf

---

## Developers and Maintainers
The project is developed at **HackInTheNorth 4.0** hackathon and maintained by
- Aswanth Koleri ([aswanthkoleri](https://github.com/aswanthkoleri))
- Druval CR ([druvalcr28](https://github.com/druvalcr28))
- Divyanshu N Singh([DNS-404](https://github.com/DNS-404))
- Jogendra Kumar ([jogendra](https://github.com/jogendra))

# Instructions to run locally:
1. [Create a Zulip Realm](https://zulip.com/create_realm/)
2. Goto to settings and create a new generic bot named 'neo'. (Settings can be found in dropdown of gear icon present in top right corner of zulip realm)
3. Download the zuliprc file for your bot and place it in your home directory as `.zuliprc`. 
4. Install all the requirements using ``` pip install -r requirements.txt ```
5. In ``` bot.py ``` , change site in ``` self.client = zulip.Client(site="https://bint.zulipchat.com/api/") ``` to url of your created zulip realm.Do the same for ``` BOT_MAIL ``` variable.  
6. Run ``` bot.py ``` using python 3. ``` python3 bot.py ```
7. Head over to your created zulip realm and start using the bot.

# Features

Neo-Bot can:
- Meeting Scheduling
- Check Spam
- Smart Messages Summarization
- Smart Text Summarization
- To-Do
- Currency Exchange
- Geolocation
- Top News
- Translate Languages
- Weather Queries

## How to use?
### Meeting Scheduling
Schedule meeting with all the team member easily using the bot. The organizer just have to tell bot about the meeting, the bot will private message to all the meeting member as a reminder before 30 minutes of meeting time.<br>
`neo discussion on <subject> at <time> <date>`
### Check Spam
Bot will detect all the spam users in any stream.<br>
`neo checkspam`<br>
### Smart Messages Summarization
Read all the unseen messages from stream and create a summary of messages.<br>

### Smart Text Summarization
Convert long paragraph to summarized short message using NLP.<br>

### To-Do
Add, remove, check current status for to-do's<br>
`neo todo add <name of task>`<br>
`neo todo done <index of task>`<br>
`neo todo remove/undone <index of task>`<br>
`neo todo remove all`<br>
### Currency Exchange
Show all the currency value related to particular currency value. <br>
`neo currency <currency type>`<br>
`neo currency <type 1> to <type 2>`<br>
### Geolocation
Display the longitude and latitude of a given place.<br>
`neo geolocation <place name>`
### Top News
Display top 10 current/trending news.<br>
`neo news`<br>
### Translate Languages
Translate words from one language to english language.<br>
`neo translate <word>`
### Weather Queries
Display all the weather information of any place.<br>
`neo weather <place>`

## License
This project is currently licensed under the **Apache License Version 2.0**. See the LICENSE file for more info.
