import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#调用API，储存返回数据
url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)

#处理返回数据
dates = r.json()
print(dates.keys())
print('Total Repositories: ', dates['total_count'])

repo_dicts = dates['items']
names = []
repo_infos = []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    repo_info = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],#这里没有用str()，程序没有报错
        'xlink': repo_dict['html_url'],
    }
    repo_infos.append(repo_info)

#可视化
my_style = LS('#994433', base_style = LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 40
my_config.show_legend = False
my_config.show_y_guides = False
my_config.truncate_label = 13
my_config.title_font_size = 26
my_config.label_font_size = 15
my_config.major_label_font_size = 15
my_config.width = 1000

chart = pygal.Bar(my_config, style = my_style)
chart._title = 'Most_Starred Java Projects on Github'
chart.x_labels = names

chart.add('', repo_infos)
chart.render_to_file('java_github.svg')