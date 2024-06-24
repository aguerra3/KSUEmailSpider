import json
import re
import unicodedata
from collections import Counter

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

import matplotlib.pyplot as plt

with open ('data.json', 'r', encoding="utf8") as f:
    json_object = json.loads(f.read())
tokenCount = 0
email_list = {}
pages_with_emails = 0
freq_counter = {}
tokens = []
line = 0
for entry in json_object:
    s1 = str(json_object[line]["body"])
    ss1 = s1.replace('\\n','')
    sss1 = ss1.replace('\\xa0','')
    ssss1 = sss1.replace("'',",'')
    sssss1 = ssss1.replace("',",'')
    ssssss1 = sssss1.replace("'",'')
    
    s2 = ssssss1.strip().split(' ')
    while '' in s2:
        s2.remove('')
    tokens = tokens + s2
    tokenCount+=len(s2)

    emails = entry.get('emails', [])
    if emails:
        pages_with_emails +=1
    for email in emails:
        if email in email_list:
            email_list[email] +=1
        else:
            email_list.update({email: 1})
    line +=1

# print(tokenCount)
# print(len(json_object))
print("Average length of webpages in tokens:-----------", tokenCount/len(json_object))
# print(email_list)
sorted_email_list = sorted(email_list.items(), key=lambda x:x[1], reverse= True)
print("Top ten most frequent email addresses found in the entire webpage collection:-----------", sorted_email_list[0:10])
print("Percentage of webpages that contain at least one email address:-----------", pages_with_emails/len(json_object)*100,"%")
freq_counter = Counter(tokens)
top_words = freq_counter.most_common(30)
print("Top 30 most common words:-----------",top_words)

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

no_stop_tokens = [w for w in tokens if not w.lower() in stop_words]

freq_counter2 = Counter(no_stop_tokens)

top_nonstop_words = freq_counter2.most_common(30)

print("Top 30 most common words with stop words removed:-----------",top_nonstop_words)


plot_list = []
plot_rank = []

all_top_words = freq_counter.most_common()

rank = 0
for words in all_top_words:
    plot_list.append(all_top_words[rank][1])
    rank += 1
    plot_rank.append(rank)


plt.plot(plot_rank,plot_list)
plt.ylabel('frequency')
plt.xlabel('rank')

plt.show()

plt.plot(plot_rank,plot_list)
plt.ylabel('frequency')
plt.xlabel('rank')
plt.semilogx()
plt.semilogy()

plt.show()


    