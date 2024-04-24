import os
import requests

# Ensure the access token is available
access_token = os.getenv("GITHUB_TOKEN")
if not access_token:
    raise EnvironmentError("GITHUB_TOKEN environment variable not set")

headers = {"Authorization": f"Bearer {access_token}"}

def get_closed_bug_issues(owner, repo):
    """Fetches closed issues labeled as 'bug' from a specified repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    params = {"state": "closed", "labels": "bug"}
    issues = []
    page = 1
    while True:
        params["page"] = page
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if not data:
                break
            issues.extend(data)
            page += 1
        else:
            print(f"Failed to fetch issues for {repo}: {response.status_code}, {response.text}")
            break
    return issues

def get_pull_request_commits(owner, repo, pull_number):
    """Fetches commits associated with a specific pull request."""
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/commits"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch pull request commits for {repo} PR#{pull_number}: {response.status_code}, {response.text}")
        return []

def print_commit_changes(owner, repo, commit_sha):
    """Fetches and prints changes for a specific commit."""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        commit_data = response.json()
        files = commit_data.get('files', [])
        for file in files:
            print(f"Changes in {file['filename']}:")
            print(f" - Additions: {file['additions']}")
            print(f" - Deletions: {file['deletions']}")
            print(f" - Patch: {file['patch']}")
    else:
        print(f"Failed to fetch commit details for {repo} commit {commit_sha}: {response.status_code}, {response.text}")

# List of repositories to process
repositories = [
    {"name": "senzing-api-server", "url": "https://github.com/Senzing/senzing-api-server.git"},
    # Add other repositories similarly
]

# Process each repository
for repo in repositories:
    owner, repo_name = repo["url"].split('/')[-2], repo["url"].split('/')[-1].replace('.git', '')
    issues = get_closed_bug_issues(owner, repo_name)
    print(f"Repo: {repo['name']}, Issues: {len(issues)}")
    for issue in issues:
        if "pull_request" in issue:
            pr_number = issue['pull_request']['url'].split('/')[-1]
            commits = get_pull_request_commits(owner, repo_name, pr_number)
            for commit in commits:
                print_commit_changes(owner, repo_name, commit['sha'])
