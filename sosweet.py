import re
import certifi
import os
import requests


def runServer():
    with open("doc/playlist1.m3u8", "w") as file:
        file.write("#EXTM3U\n")
    for i in range(len(lis)):
        print(f"{i+1}.{lis[i]}")
        server(i + 1, lis[i])


def server(i, name):
    print("Running Server")
    url = f"https://adult-tv-channels.com/tv/{name}.php"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://adult-tv-channels.com",
        "X-Requested-With": "XMLHttpRequest",
    }

    response = requests.get(url, headers=headers, verify=certifi.where())

    # Use regex to extract the source URL
    match = re.search(r'file:\s*"([^"]+playlist\.m3u8[^"]*)"', response.text)
    if match:
        stream_url = match.group(1)
        # print(stream_url)
        with open("docs/playlist1.m3u8", "a") as file:
            file.write(f"#EXTINF:-1,{name}\n")
            file.write(f"{stream_url}|Referer=https://adult-tv-channels.com/|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 ygx/69.1 Safari/537.36\n")

    else:
        print("No URL found.")


# For Server 1
print("Available Channels\nSome links might not works!!!")
lis = [
    "brazzerstv",
    "hustlerhd",
    "hustlertv",
    "penthouse",
    "redlight",
    "penthousepassion",
    "vivid",
    "dorcel",
    "superone",
    "oxax",
    "passie",
    "eroxxx",
    "playboy",
    "pinko",
    "extasy",
    "penthousereality",
    "kinoxxx",
    "pinkerotic",
    "pinkerotic7",
    "pinkerotic8",
    "evilangel",
    "private",
    "beate",
    "meiden",
    "centoxcento",
    "barelylegal",
    "venus",
    "freextv",
    "erox",
    "passion",
    "satisfaction",
    "jasmin",
    "fap",
    "olala",
    "miamitv",
]


runServer() #Runs the function to start the server!
