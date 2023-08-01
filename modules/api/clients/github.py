from importlib.metadata import requires
import os
import requests

class GitHub:

    hdrs = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN', None)}"}

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(
                        "https://api.github.com/search/repositories",
                         params={"q": name})
        body = r.json()

        return body


    # Individual Tests for GitHub API
    def create_issue(self, owner, repo, data):
        r = requests.post(f"https://api.github.com/repos/{owner}/{repo}/issues",
                         headers=self.hdrs,
                         json = data)
        body = r.json()

        return body
    
    
    def list_of_issues(self, owner, repo, name):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/issues",
                         headers=self.hdrs,
                         params={"labels": name}
                         )
        body = r.json()

        return body
    
    def update_issues(self, owner, repo, issue_number, data):
        r = requests.patch(f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}",
                        headers=self.hdrs,
                        json = data)
        body = r.json()

        return body
    
    def get_issues(self, owner, repo, issue_number):
        r = requests.patch(f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}",
                           headers=self.hdrs)
        body = r.json()

        return body
    
    
    def list_of_commit(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits",
                         headers=self.hdrs,
                         params={"per_page": 1, "page" : 1}
                         )
        body = r.json()

        return body
    

    def create_comment(self, owner, repo, commit_sha, data):
        r = requests.post(f"https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}/comments",
                         headers=self.hdrs,
                         json = data)
        body = r.json()

        return body


    def delete_comment(self, owner, repo, comment_id):
        r = requests.delete(f"https://api.github.com/repos/{owner}/{repo}/comments/{comment_id}",
                         headers=self.hdrs)
        # body = r.json()

        return r