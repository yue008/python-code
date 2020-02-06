# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: python_repos.py
@time: 2020/2/6 14:44
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print('Status code:',r.status_code)

#将API响应存储在一个变量中
response_dict=r.json()
print('Total repositories:',response_dict['total_count'])

#搜索有关仓库的信息
repo_dicts=response_dict['items']
print('Number of items:',len(repo_dicts))

names,plot_dicts=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict={'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url']}

    plot_dicts.append(plot_dict)

#可视化
my_style=LS('#333366',base_style=LCS)

# my_config=pygal.Config()
# my_config.x_labels_rotation=45
# my_config.show_legend=False
# my_config.title_font_size=24
# my_config.label_font_size=14
# my_config.major_label_font_size=18
# my_config.truncate_label=15
# my_config.show_y_guides=False
# my_config.width=100

chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title='Python Projects'
# chart.x_labels=['httpie','django','flask']
#
# plot_dicts=[ {'value':16101,'label':'Description of httpie.'},
#     {'value':15028,'label':'Description of django.'},
#     {'value':14798,'label':'Description of flask.'}]

chart.add('',plot_dicts)
chart.render_to_file('python_repos04.svg')

# #研究第一个仓库
# print('\nSelected information about each repository:')
# for repo_dict in repo_dicts:
#     print('Name:',repo_dict['name'])
#     print('Owner',repo_dict['owner']['login'])
#     print('Stars:',repo_dict['stargazers_count'])
#     print('Reposition:',repo_dict['html_url'])
#     print('Description:',repo_dict['description'])



