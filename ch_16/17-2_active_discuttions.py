from operator import itemgetter
import plotly.express as px
import requests
#make an api call and check the responce
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r= requests.get(url)
print(f'status code: {r.status_code}')

#prosses information aout each submission
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    #make a new api call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f'id:{submission_id}\tstatus:{r.status_code}')
    responde_dict = r.json()
    #build a dictionary for each article
    try:
        submission_dict = {"title":responde_dict["title"]
                        ,"hn_link":f"https://news.ycombinator.com/item?id={submission_id}",
                        "comments":responde_dict["descendants"],}
    except KeyError:
        print("missing descendants")

    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"),reverse=True)
"""print(submission_dicts)"""
comments,url_link, =[],[]
for submission_dict in submission_dicts:
    name1 = submission_dict["title"]
    link1= submission_dict["hn_link"]
    link2 =f"<a href='{link1}'>{name1}</a>"
    url_link.append(link2)
    comments.append(submission_dict["comments"])


title = "Most discussied topics on hacker news"
labels = {"x":"repositories","y":"Comments"}
fig = px.bar(x = url_link , y = comments  , title = title, labels=labels)

fig.update_layout(title_font_size = 28, xaxis_title_font_size = 20,yaxis_title_font_size=20)
fig.update_traces(marker_color="SteelBlue",marker_opacity =0.6)
fig.show()
