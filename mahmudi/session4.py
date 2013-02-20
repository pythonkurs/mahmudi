import requests
import getpass
import sys, os
from dateutil import parser
from pandas import DataFrame,Series
import json
from collections import Counter

sys.stdout.write('Github User Name : ')
userName=sys.stdin.readline().strip()
password = getpass.getpass('Password : ')
organization = "pythonkurs" 

repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=(userName, password))
repositories = repos.json()

authors=[]
commit_msgs=[]
commit_times=[]
author_list=[]

for repository in repositories:
    authors.append(str(repository["name"]))

for author in authors:
    commit_messages= requests.get("https://api.github.com/repos/%s/%s/commits" % (organization, author))
    commits=commit_messages.json()
    for commit in commits:
        if not isinstance(commit,dict):  
            continue
        commit_msgs.append(commit["commit"]["message"])
        commit_times.append(parser.parse(commit["commit"]["author"]["date"]))
        author_list.append(commit["commit"]["author"]["name"])

days=[]
for time in commit_times:                                                                                              
    days.append(time.strftime("%A"))

hours=[]
for time in commit_times:                                                                                                                                
    hours.append(time.hour)

records=[]

d=DataFrame({'day' : days, 'hour' : hours},index=days)

mcDay = d.groupby('day')
mcHour = d.groupby('hour')

peakdaycount=0
peakday=''
peakhourcount=0
peakhour=''

for d in mcDay.groups.iterkeys():
    mcDayCount= mcDay.count()['day'][d]                                                                                                                           
    if peakdaycount < mcDayCount:  
        peakdaycount = mcDayCount                                                                                                                                     
        peakday = str(d)
for d in mcHour.groups.iterkeys():    
    mcHourCount= mcHour.count()['day'][d] 
    if peakhourcount < mcHourCount:  
        peakhourcount = mcHourCount                                                                                                                                     
        peakhour = str(d)

print "Most frequent day for submission is " + peakday + " with " + str(peakdaycount) + " commits "
print "Most frequent hour for submission is " + peakhour + " with " + str(peakhourcount) + " commits "
