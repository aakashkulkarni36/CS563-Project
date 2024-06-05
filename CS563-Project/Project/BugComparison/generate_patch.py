import json
import os
import requests

## Github token
access_token = ""
if not access_token:
    raise EnvironmentError("GITHUB_TOKEN environment variable not set")

## Repositories
repositories = [
    {"name": "management-api-for-apache-cassandra", "url": "https://github.com/k8ssandra/management-api-for-apache-cassandra.git"},
    {"name": "catwatch", "url": "https://github.com/zalando-incubator/catwatch.git"},
    {"name": "cwa-verification-server", "url": "https://github.com/corona-warn-app/cwa-verification-server.git"},
    {"name": "digdag", "url": "https://github.com/treasure-data/digdag.git"},
    {"name": "enviroCar-server", "url": "https://github.com/enviroCar/enviroCar-server.git"},
    {"name": "features-service", "url": "https://github.com/JavierMF/features-service.git"},
    {"name": "gravitee-api-management", "url": "https://github.com/gravitee-io/gravitee-api-management.git"},
    {"name": "kafka-rest", "url": "https://github.com/confluentinc/kafka-rest.git"},
    {"name": "ocvn", "url": "https://github.com/devgateway/ocvn.git"},
    {"name": "ohsome-api", "url": "https://github.com/GIScience/ohsome-api.git"},
    {"name": "proxyprint-kitchen", "url": "https://github.com/ProxyPrint/proxyprint-kitchen.git"},
    {"name": "quartz-manager", "url": "https://github.com/fabioformosa/quartz-manager.git"},
    {"name": "restcountries", "url": "https://github.com/apilayer/restcountries.git"},
    {"name": "senzing-api-server", "url": "https://github.com/Senzing/senzing-api-server.git"},
    {"name": "Ur-Codebin-API", "url": "https://github.com/Mathew-Estafanous/Ur-Codebin-API.git"}
]

## Find link
def findRepo(name):
	for repo in repositories:
		if repo["name"] == name:
			owner, repo_name = repo["url"].split('/')[-2], repo["url"].split('/')[-1].replace('.git', '')
			return owner, repo_name
	return '',''

def generatePatch(owner,repo,folder,buggyCommit,fixedCommit):
    url = f"https://api.github.com/repos/{owner}/{repo}/compare/{buggyCommit}...{fixedCommit}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        diff_url = response.json()['diff_url']
        response = requests.get(diff_url, headers=headers)
        if response.status_code == 200:
            with open(os.path.join(folder,'diff.patch'),'wb') as f:
                f.write(response.content)
        else:
            print("Cannot access diff url")
    else:
        print(f'Failed to get patch for {owner}/{repo}!')
    
## Folder for patch
patch_directory = "./patch"
if not os.path.exists(patch_directory):
    os.mkdir(patch_directory)

## Read json file for bug list
json_filename = 'output.json'
with open(json_filename, 'r') as j:
    bug_list = json.load(j)

for bug in bug_list:
    _bug = bug_list[bug]
    buggy = _bug['buggyCommit']
    fixed = _bug['fixedCommit']
    if not os.path.exists(os.path.join(patch_directory,bug)):
        os.mkdir(os.path.join(patch_directory,bug))
    owner, repo = findRepo(_bug['service'])
    generatePatch(owner,repo,os.path.join(patch_directory,bug),buggy,fixed)
