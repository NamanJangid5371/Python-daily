raw_names = ["alex","BOB","Charlie", "sam"]
usernames = [name.lower() if len(name)<4 else name.upper() for name in raw_names]
print("Genrated list",usernames)