import json
from ghapi.all import GhApi, paged

api = GhApi()
repo_list = json.load(open('projects.json',))['repos']

data = [api.repos.get(owner=project["owner"], repo=project["repo"]) for project in repo_list]
