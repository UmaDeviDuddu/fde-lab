raw = input("Enter Repo name: ")
clean = raw.strip()
slug = "-".join(clean.lower().split())
print(f"Orginal repo: '{raw}'")
print(f"Slug: '{slug}'")
print(f"Clean repo: '{clean}'")

print(f"Length:  {len(slug)} charachters")
