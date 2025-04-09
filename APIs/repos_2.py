## Making visualization of Python projects on Github
## Adding plot_dicts on each project, to describe each bar. Adding a clickable link to the graph.

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url'],
            }
    plot_dicts.append(plot_dict)

# Make visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('Python_repos_2.svg')



