name = input("Repo name :").strip()
size_mb = int(input("size in MB "))
has_lfs = input("Uses LFS? (y/n) ").strip().lower() == "y"

if size_mb > 1000:
    status = "Blocked"
    reason = "Over 1000 MB"
elif size_mb > 500 or has_lfs:
    status = "Needs Review"
    reason = "Over 500 MB or uses LFS"
else:
    status = "Ready to migrate"
    reason = "Small , no LFS"

print(f"{name} : {status} ({reason})")
