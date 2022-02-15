import json 
import requests
import subprocess

BASE_URL = "https://github.com/scalable-web-systems/"
f = open('config.json')
 
data = json.load(f)

exceptions = ['README.md']

def get_file_names():
    import os
    
    files = os.listdir('.')
    file_names = []

    for file in files:
        if '.md' in file and file not in exceptions:
            print(file)
            file_names.append(file)
    return file_names

for repo_name in data['repos']:
    print(repo_name)
    subprocess.run(["mkdir", repo_name])
    # subprocess.run(["cd", repo_name])
    subprocess.run(["git", "pull", BASE_URL+repo_name, "--allow-unrelated-histories"], cwd=repo_name)
    # res = requests.get(BASE_URL+repo_name)
    # if res.status_code != 200:
    #     print(repo_name, "does not exist or network error")
    #     continue
    # subprocess.run(["git", "pull", BASE_URL+repo_name, "--allow-unrelated-histories"])



    
