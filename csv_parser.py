import csv
import json

# PAGE TYPES DICTONARY
page_types_dictonary = {
    'rv': 'rv_information',
    'reviews': 'regional_lander'
}

path_dicts = []
curr_id = 0
# update this line base on what file you're parsing
file_name = 'csv/11_18_2019_RV_500.csv'
with open(file_name, newline='') as csvfile:
    contents = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in contents:
        # the redirect url is the last csv in the row
        last_index = len(row) - 1
        curr_id += 1
        path = '/'.join(row[0].split('/')[3:])
        redirect_path = '/'.join(row[last_index].split('/')[3:])
        page_type = row[0].split('/')[3]
        path_dicts.append({'id': curr_id, 'path': path, 'redirect_path': redirect_path, 'type': page_type})

# print(path_dicts)

# create an object to place in JSON file

for dict in path_dicts:
    json_obj = {
        'title': dict['path'] + ' 301 to ' + dict['redirect_path'],
        'uid': dict['path'].split('/')[1],
        'redirect_to': '/' + dict['redirect_path'],
        'type': page_types_dictonary[dict['type']],
        'tags': [],
        'lang': 'en-us',
        'grouplang': 'XaC56BAAAB8AX53Z'
    }
    file_id = dict['id']
    language = "en-us"
    file_name = f'redirects/new_rv-info-{file_id}_en-us.json'
    with open(file_name, 'w') as f:
        f.write(json.dumps(json_obj))
    f.close
