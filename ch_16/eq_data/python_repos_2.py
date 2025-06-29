import requests
import plotly.express as px
#make an API call and check the responce

url = "https://api.github.com/search/repositories?q=language:python+sort:stars"
url +="?q=lamguage:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url,headers=headers)
print(f"Status code :{r.status_code}")
#prosses overall results
responce_dict = r.json()
print(f"total repositories:{responce_dict["total_count"]}")
print(f"complete results: {not responce_dict["incomplete_results"]}")

#explore information about repositories.
repo_dicts = responce_dict["items"]
repo_links,stars,hover_texts = [],[],[]
print(f"repositories returned:{len(repo_dicts)}")
#examine the first repositories
repo_dict = repo_dicts[0]
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict["stargazers_count"])
    #build hover texts
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

    
#make visualisations
title = "Most-starred python projects on github"
labels = {"x":"repository","y":"Stars"}
fig = px.bar(x=repo_links, y = stars, title = title, labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size = 28, xaxis_title_font_size = 20,yaxis_title_font_size=20)
fig.update_traces(marker_color="SteelBlue",marker_opacity =0.6)
fig.show()
