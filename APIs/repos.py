import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code) # The response object has an attribute called status_code, tells whether the request is successful- code 200.

# Store API response in a variable.
response_dict = r.json() # Use json() method to convert the information to a Python dictionary.

# Process results.
print(response_dict.keys())

print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Examine the repositories.
print("\nSelected information on each repository:")
for repo_dict in repo_dicts:
    print('\nName: ', repo_dict['name'])
    print('Owner: ', repo_dict['owner']['login'])
    print('Stars: ', repo_dict['stargazers_count'])
    print('Created: ', repo_dict['created_at'])
    print('Description: ', repo_dict['description'])

