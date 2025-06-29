import requests

#make an API call and check the responce

url = f"https://api.github.com/search/repositories?q=language:Perl+sort:stars"
url1 = "https://api.github.com/search/repositories?q=language:C+sort:stars"
url2 = "https://api.github.com/search/repositories?q=language:Python+sort:stars"
url3 = "https://api.github.com/search/repositories?q=language:Java+sort:stars"
url4 = "https://api.github.com/search/repositories?q=language:Go+sort:stars"

url +="?q=language:Perl+sort:stars+stars:>10000"
url1 += "?q=language:C+sort:stars+stars:>10000"
url2 += "?q=language:Python+sort:stars+stars:>10000"
url3 +="?q=language:java+sort:stars+stars:>10000"
url4 +="?q=language:Go+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url,headers=headers)
r1 = requests.get(url1,headers=headers)
r2 = requests.get(url2,headers=headers)
r3 = requests.get(url3,headers=headers)
r4 =requests.get(url4,headers=headers)

print(f"Status code :{r.status_code}")
print(f"Status code :{r1.status_code}")
print(f"Status code :{r2.status_code}")
print(f"Status code :{r3.status_code}")
print(f"Status code :{r4.status_code}")

#convert the reponse object to a dictionary
responce_dict = r.json()
responce_dict1 = r1.json()
responce_dict2 = r2.json()
responce_dict3 = r3.json()
responce_dict4 = r4.json()


print(f"total repositories:{responce_dict["total_count"]}")
print(f"complete results: {not responce_dict["incomplete_results"]}")

print(f"total repositories:{responce_dict1["total_count"]}")
print(f"complete results: {not responce_dict1["incomplete_results"]}")

print(f"total repositories:{responce_dict2["total_count"]}")
print(f"complete results: {not responce_dict2["incomplete_results"]}")

print(f"total repositories:{responce_dict3["total_count"]}")
print(f"complete results: {not responce_dict3["incomplete_results"]}")

print(f"total repositories:{responce_dict4["total_count"]}")
print(f"complete results: {not responce_dict4["incomplete_results"]}")

#explore information about repositories.
repo_dicts = responce_dict["items"]
repo_dicts1 = responce_dict1["items"]
repo_dicts2 = responce_dict2["items"]
repo_dicts3 = responce_dict3["items"]
repo_dicts4 = responce_dict4["items"]

print(f"repositories returned:{len(repo_dicts)}")
print(f"repositories returned:{len(repo_dicts1)}")
print(f"repositories returned:{len(repo_dicts2)}")
print(f"repositories returned:{len(repo_dicts3)}")
print(f"repositories returned:{len(repo_dicts4)}")
#examine the first repositories
repo_dict = repo_dicts[0]

repo_dict1 = repo_dicts1[0]

repo_dict2 = repo_dicts2[0]

repo_dict3 = repo_dicts3[0]

repo_dict4 = repo_dicts4[0]

print("\nSelected information about first repository:")
#for repo_dict in repo_dicts:
#Perl
print(f"Name: {repo_dict["name"]}")
print(f"Owner:{repo_dict["owner"]["login"]}")
print(f"Stars: {repo_dict["stargazers_count"]}")
print(f"Repositories{repo_dict["html_url"]}")
print(f"Created{repo_dict["created_at"]}")
print(f"Updated{repo_dict["updated_at"]}")
print(f"Description{repo_dict["description"]}")
#C
print(f"Name: {repo_dict1["name"]}")
print(f"Owner:{repo_dict1["owner"]["login"]}")
print(f"Stars: {repo_dict1["stargazers_count"]}")
print(f"Repositories{repo_dict1["html_url"]}")
print(f"Created{repo_dict1["created_at"]}")
print(f"Updated{repo_dict1["updated_at"]}")
print(f"Description{repo_dict1["description"]}")
#Python
print(f"Name: {repo_dict2["name"]}")
print(f"Owner:{repo_dict2["owner"]["login"]}")
print(f"Stars: {repo_dict2["stargazers_count"]}")
print(f"Repositories{repo_dict2["html_url"]}")
print(f"Created{repo_dict2["created_at"]}")
print(f"Updated{repo_dict2["updated_at"]}")
print(f"Description{repo_dict2["description"]}")
#Java
print(f"Name: {repo_dict3["name"]}")
print(f"Owner:{repo_dict3["owner"]["login"]}")
print(f"Stars: {repo_dict3["stargazers_count"]}")
print(f"Repositories{repo_dict3["html_url"]}")
print(f"Created{repo_dict3["created_at"]}")
print(f"Updated{repo_dict3["updated_at"]}")
print(f"Description{repo_dict3["description"]}")
#Go
print(f"Name: {repo_dict4["name"]}")
print(f"Owner:{repo_dict4["owner"]["login"]}")
print(f"Stars: {repo_dict4["stargazers_count"]}")
print(f"Repositories{repo_dict4["html_url"]}")
print(f"Created{repo_dict4["created_at"]}")
print(f"Updated{repo_dict4["updated_at"]}")
print(f"Description{repo_dict4["description"]}")
"""print(f"\nKeys:{len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
#process results

print(responce_dict.keys())"""
