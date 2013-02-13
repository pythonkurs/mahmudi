import requests
import getpass
import sys, os
from dateutil import parser
from pandas import DataFrame

sys.stdout.write('Github User Name : ')
userName=sys.stdin.readline().strip()
password = getpass.getpass('Password : ')

users = requests.get("https://api.github.com/orgs/pythonkurs/members", auth=(userName, password))
repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=(userName, password))
repositories = repos.json()

print len(repositories)

organization = "pythonkurs" 


authors=[]
commit_msgs=[]

print "Starting: "

for repository in repositories:
    print "Reading repository name: " + repository["name"]
    
    commit_messages= requests.get("https://api.github.com/repos/%s/%s/commits" % (organization, repository["name"]))
    # for each commit
    commits=commit_messages.json()
    for commit in commits:
        if 'commit' not in commit:
            continue
    
        authors.append(commit["commit"]["author"]["name"])
        commit_msgs.append(commit["commit"]["message"])


print len(commit_msgs)
for msg in commit_msgs:
    print msg
