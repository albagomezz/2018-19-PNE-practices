
import http.client
import json

user = input("Write the user to search: ")

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT1 = "/users/"
GITHUB_ID = user
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT1 + GITHUB_ID, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
u = json.loads(text_json)

# -- Get some data
name = u['name']
nrepos = u['public_repos']
repos = user['repos_url']

def all_repos(link):
    HOSTNAME = "api.github.com"
    ENDPOINT2 = link[22:]
    METHOD = "GET"

    # -- Here we can define special headers if needed
    headers = {'User-Agent': 'http-client'}

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection!
    # -- If we do not specify the port, the standar one
    # -- will be used
    conn = http.client.HTTPSConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT2, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Optionally you can print the
    # -- received json file for testing
    # print(text_json)

    # -- Generate the object from the json file
    info = json.loads(text_json)
    rep = []
    commits = len(info[0]['commits_url'])
    for i in info:
        rep.append(i['name'])
    add_to_list = ""
    for a in rep:
        add_to_list = add_to_list + a + ','
    return commits, add_to_list

information, comm = all_repos(repos)

print()
print("Real name:", name)
print("Names of all the repos: ", information)
print("Number of commits to the 2018-19-PNE-repo", comm)

