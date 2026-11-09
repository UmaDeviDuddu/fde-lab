count = int(input("How many repos in this batch?"))
ready = 0
review = 0
blocked = 0

for i in range(count):
    print(f"\nRepo {i + 1} of {count}")
    name = input("Name of the repo:   ").strip()
    size_mb = int(input("   Size in MB:    ").strip())
    if size_mb > 1000:
        status = "Blocked"
        blocked += 1
    elif size_mb > 500:
        status = "NeedsReview"
        review += 1
    else:
        status = "Ready"
        ready += 1
    print(f"Repo {name}: {status}")

print(f"\nSummary: {ready} Ready, {review} NeedsReview, {blocked} Blocked")
