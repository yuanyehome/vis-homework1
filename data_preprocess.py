# %%
import numpy as np
import pandas as pd
import json
detailed_data = pd.read_csv('./data/总表.csv')
corr_data = pd.read_csv('./data/隶属关系.csv')
prop_data = pd.read_csv('./data/单位性质.csv')
loc_data = pd.read_csv('./data/地区.csv').fillna(0)
col_keys = ['数理科学部', '化学科学部', '生命科学部', '地球科学部',
            '工程与材料科学部', '信息科学部', '管理科学部', '医学科学部']
detailed_data_json = {}
corr_data_json = {}
prop_data_json = {}
loc_data_json = {}
tmp_corr_keys = ['name'] + list(corr_data.keys()[1:])
tmp_prop_keys = ['name'] + list(prop_data.keys()[1:])
for key in col_keys:
    detailed_data_json[key] = {}
    corr_data_json[key] = {}
    prop_data_json[key] = {}
tmp_value = detailed_data.values
tmp_corr = corr_data.values
tmp_prop = prop_data.values
tmp_loc = loc_data.values
for i in range(len(tmp_value)):
    if i == 0:
        continue
    item = tmp_value[i]
    if item[0] in col_keys:
        now_key = item[0]
        continue
    detailed_data_json[now_key][item[0]] = {
        'name': item[0],
        '受理项数': item[1],
        '受理金额': item[2],
        '批准项数': item[3],
        '批准金额': item[4]
    }
for i in range(len(tmp_corr)):
    if i == 0:
        continue
    item = tmp_corr[i]
    for j in range(len(item)):
        corr_data_json[item[0]][tmp_corr_keys[j]] = item[j]
for i in range(len(tmp_prop)):
    if i == 0:
        continue
    item = tmp_prop[i]
    for j in range(len(item)):
        prop_data_json[item[0]][tmp_prop_keys[j]] = item[j]


# %%
loc_col_keys = list(loc_data['地区'])
loc_row_keys = list(loc_data.keys())
for key in loc_col_keys:
    if key == '合计':
        continue
    loc_data_json[key] = {}
for i in range(len(tmp_loc)):
    if i == 0:
        continue
    item = tmp_loc[i]
    for j in range(len(item)):
        loc_data_json[item[0]][loc_row_keys[j]] = item[j]
all_data = {
    'detailed_data': detailed_data_json,
    'corr_data': corr_data_json,
    'prop_data': prop_data_json,
    'loc_data': loc_data_json
}
with open('all_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False)
