import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    # 1. Retrieve a list of "events" associated with the given user name
    response = requests.get(f"https://api.github.com/users/{username}/events")
    # 2. Print out the time stamp associated with the first event in that list.
    events = json.loads(response.content)

    print(events[0]['created_at'])
    


