import sys
import zulip
from summarizer import summarizeDoc
client = zulip.Client(config_file="~/.zuliprc")

def digest(stream_name,message_id,sender_email):
    # Get all users
    # all_users=client.get_members()
    # print(all_users)
    # all_users_emails=[]
    # for member in all_users["members"]:
    #     all_users_emails.append(member["email"])
    # print(all_users_emails)
    # print(sys.maxsize)
    # get all the messages in a particular stream by all the users 
    # for user_email in all_users_emails:
    # user_email="aswanth.koleri.anil@gmail.com"  
    # print("The user : ", user_email)
    request = {
        'use_first_unread_anchor': False,
        'anchor' : message_id,
        'num_before': 100,
        'num_after': 0,
        'narrow': [{'operator': 'sender', 'operand': sender_email, 'negated' : True },
                   {'operator': 'stream', 'operand': stream_name}],
        'client_gravatar': True,
        'apply_markdown': False
    }  # type: Dict[str, Any]
    result = client.get_messages(request)
    # print(result)
    # for i,message in enumerate(result["messages"]):
    #     print(i,message["content"])
    # print(result)
    # I have to find the messages with the most reactions
    # find all the messages along with the reaction
    messagesListWithReactions=[]
    print("#####################")
    print(sender_email)
    for message in result["messages"]:
        messagesListWithReactions.append((len(message["reactions"]),message["content"]))
    # for i in messagesListWithReactions:
    #     print(i)
    # first I have to take all top 10 messages
    messagesListWithReactions.sort(key=lambda x: x[0],reverse=True)
    sample=[(1,2),(2,3),(3,4)]
    sample.sort(key=lambda x: x[1],reverse=True)
    print(sample)
    message="**The top 10 messages are :**\n"
    document=""
    for i,item in enumerate(messagesListWithReactions):
        message+="\n"+str(i+1)+". "+item[1]+"["+str(item[0]) + " reacts]\n\n\n"
        
        if (i+1)==10:
            break
    for item in messagesListWithReactions:
        document+=item[1]+"."
    print(message)
    summary=summarizeDoc("LR",document,20)
    return (message,summary)
    

# digest()