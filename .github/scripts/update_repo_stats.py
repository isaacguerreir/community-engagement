import os
import gspread
import datetime
from github import Github

g = Github(os.environ["GH_TOKEN"])
credentials = {
	"client_email": os.environ["CLIENT_EMAIL"],
	"token_uri": os.environ["TOKEN_URI"],
	"private_key": os.environ["PRIVATE_KEY"],
}

print(credentials)

gc = gspread.service_account_from_dict(credentials)

repositories = [
	{ 
		"repo_name": "isaacguerreir/zet",
		"worksheet": "zet"
	},
	{ 
		"repo_name": "Lattice-Automation/isaac-prototype",
		"worksheet": "isaac-prototype"
	}
]

sh = gc.open("Community")

for repository in repositories:
	worksheet = sh.worksheet(repository["worksheet"])
	repo = g.get_repo(repository["repo_name"])

	open_issues = repo.get_issues(state="open")
	closed_issues = repo.get_issues(state="closed")
	open_issues = len(list(filter(lambda issue: issue.pull_request is None, open_issues)))
	closed_issues = len(list(filter(lambda issue: issue.pull_request is None, closed_issues)))
	prs = repo.get_pulls()

	date_now = datetime.datetime.now().strftime("%x") 
	new_row = [date_now, open_issues, closed_issues, prs.totalCount, repo.forks_count, repo.watchers_count, repo.stargazers_count]
	print(repo.name)
	print(new_row)
	
	worksheet.append_row(new_row)
