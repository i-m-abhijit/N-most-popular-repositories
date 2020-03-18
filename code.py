import json
import requests
#sort the list of tuples in descending order
def Sort_Tuple(repo_fork):   
    repo_fork.sort(key = lambda x: x[1],reverse=True)  
    return repo_fork 
#inputs
orgname = input("Enter the Organisation name:")
number_of_repo = int(input("Enter number of popular repositories:"))
number_of_committees = int(input("Enter number of popular committees:"))
repo_fork=[]
for i in range(1,20):
    params = {'page': i, 'per_page':100}
    r = requests.get('https://api.github.com/orgs/'+orgname+'/repos', params=params)
    todos = json.loads(r.text)
    repo_fork.extend([(sub['full_name'],sub['forks_count']) for sub in todos])

Sort_Tuple(repo_fork)
k=1
for i in repo_fork[0:number_of_repo]:
    print("Repository number:",k,i[0]," ","Fork counts:",i[1])
    k+=1
    l = requests.get('https://api.github.com/repos/'+i[0]+'/contributors')
    temp = json.loads(l.text)
    contributors_commits = [(sub['login'],sub['contributions']) for sub in temp]
    Sort_Tuple(contributors_commits)
    m=1
    for j in contributors_commits[0:number_of_committees]:
        print("Github id:",m,j[0]," ","Commit counts:",j[1])
        m+=1
    print()
    print()
