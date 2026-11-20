def repo_Status(repo):
    if repo["size"] > 1000:
        return "blocked"
    elif repo["size"] > 500 or repo["uses_lfs"]:
        return "Needs Review"
    else:
        return "Ready"


repos = [
    {"name": "repo1", "size": 1200, "uses_lfs": False},
    {"name": "repo2", "size": 600, "uses_lfs": True},
    {"name": "repo3", "size": 300, "uses_lfs": False},
    {"name": "repo4", "size": 800, "uses_lfs": False},
]

counts = {}
for r in repos:
    status = repo_Status(r)
    print(f"{r['name']:<15}  {status}")
    counts[status] = counts.get(status, 0) + 1

print(counts)
