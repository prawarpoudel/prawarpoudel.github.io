from bs4 import BeautifulSoup

import os
import yaml
from os import path

rootdir = '.'
f_names = list()

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.split('.')[-1]=='html':
            f_name = os.path.join(subdir,file)
            f_names.append(f_name)

index_content = ''
with open('tableOfContents.yaml') as toc:
    index_content = yaml.safe_load(toc)

for each_file in f_names:
    with open(each_file,'r+') as edit_file:
        if 'about.html' in each_file:
            continue
        print(f"Working on file {each_file}")
        file_contents = edit_file.read()
        obj = BeautifulSoup(file_contents, 'html.parser')

        for this_div in obj.find_all('div'):
            if this_div['class'][0] == 'sidebar':

                new_div = obj.new_tag("div")
                new_div['class'] = "sidebar"
                
                for tp in index_content['table_contents']:
                    each_a = index_content['table_contents'][tp]
                    class_ = each_a['class']
                    string_ = each_a['string']
                    href_ = each_a['href']

                    if 'index.html' in each_file and string_ != "About" :
                        href_ = '/'.join(href_.split('/')[1:])

                    a_tag = obj.new_tag("a", href=href_)
                    a_tag.string = string_
                    a_tag['class'] = class_
                    new_div.append(a_tag)

                this_div.replaceWith(new_div)
                break
    

        edit_file.seek(0)
        edit_file.truncate()
        edit_file.write(str(obj.prettify()))