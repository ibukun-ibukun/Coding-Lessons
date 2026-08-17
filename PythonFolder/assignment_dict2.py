songs = {
    "Rema": "Calm Down",
    "Taylor Swift": "Anti-Hero",
    "SZA": "Kill Bill",
    "Wizkid": "Essence"
}

songs["Bob Bob"] = "Bob"
songs["Wead"] = "Intinution"
songs["SZA"] = "Stars"
del songs["Wizkid"]

search = input("Search for a song: ").title().strip()

print(songs.get("search", "We did not find the song"))

for key, value in songs.items():
    print(f"{key:<12} {value}")

length = len(songs)
print(f"There are {length} songs in the library.")