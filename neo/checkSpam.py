import zulip
import re, math
from collections import Counter
import time

WORD = re.compile(r'\w+')

class UserInfo():
    def __init__(self,email,similarityRank,timeRank):
        self.email = email
        self.similarityRank = similarityRank
        self.timeRank = timeRank

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def cosine_sim(str1,str2):

    vector1 = text_to_vector(str1)
    vector2 = text_to_vector(str2)

    cosine = get_cosine(vector1, vector2)

    if(cosine>0.75):
        return 1
    return 0

def rank_similarity(msgs):
    counter=0
    total=0
    for i in range(len(msgs)-3):
        total=total+1
        hitinCluster = 0
        for j in range(i-3,i+4):
            if(j>0 and j<len(msgs)):
                for k in range(j+1,i+4):
                    if(j!=k and k>0 and k<len(msgs)):
                        if(cosine_sim(msgs[j],msgs[k])):
                            counter = counter+1
                            hitinCluster = 1
                            break
            if(hitinCluster==1):
                break

    if(total==0):
        return 0
    print(counter," of ",total," clusters are similar")
    similarity_rank=(float(counter)/total)*10
    return similarity_rank

def findTimeDiff(timing,pos1,pos2):
    t1 = timing[pos1].split(" ")
    t2 = timing[pos2].split(" ")
    if((t1[4]==t2[4]) and (t1[1]==t2[1]) and (t1[2]==t2[2])):
        t1 = t1[3].split(":")
        t2 = t2[3].split(":")
		# print("time difference",int(t1[0])*3600+int(t1[1])*60+int(t1[2]))-(int(t2[0])*3600+int(t2[1])*60+int(t2[2]))
		#print("----")
        if(abs((int(t1[0])*3600+int(t1[1])*60+int(t1[2]))-(int(t2[0])*3600+int(t2[1])*60+int(t2[2]))) < 180):
            return 1
        else:
            return 0
    else:
        return 0
    
def rank_time(timings):
    cluster=0
    hits=0
    
    #7 tweets is taken as a cluster
    for i in range(0,len(timings)-6):
        for j in range(0,3):
            if(findTimeDiff(timings,i+j,i+j+4)):	#check time taken for 5 tweets,ie time difference of ith and i+4th tweet
                hits = hits+1
                break
    cluster=len(timings)-6
    print(hits," of ",cluster," clusters are tweeted in similar timings")
    rank = (float(hits)/cluster)*10
    return rank


def analyse(msgs,timings):
    similarityRank = rank_similarity(msgs)
    timeRank = rank_time(timings)
    return similarityRank,timeRank

def checkSpam(stream_name,message_id):
    client = zulip.Client(config_file="~/.zuliprc")
    users = client.get_members()
    emails = []
    for member in users["members"]:
        emails.append(member["email"])
    results = []
    for email in emails:
        request = {
            'use_first_unread_anchor': False,
            'anchor' : message_id,
            'num_before': 30,
            'num_after': 0,
            'narrow': [{'operator': 'sender', 'operand': email},
                {'operator': 'stream', 'operand': stream_name}],
            'client_gravatar': False,
            'apply_markdown': False
        }  # type: Dict[str, Any]
        userMsgs = client.get_messages(request)
        print(email)
        msgs = []
        timings = []
        for item in userMsgs["messages"]:
            msgs.append(item["content"])
            t = item["timestamp"]
            t = time.ctime(int(t))
            timings.append(t)
        if(len(msgs)>=7):
            [similarityRank,timeRank] = analyse(msgs,timings)
        else:
            similarityRank = 0
            timeRank = 0
        print(similarityRank)
        print(timeRank)
        print("-----")
        results.append(UserInfo(email,similarityRank,timeRank))
    return results


# if __name__ == "__main__":
#     checkSpam("announce")