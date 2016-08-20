import json
import os
import re
from pandas import DataFrame
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__))


def normalise():
    cleaned_data = _read_clean_data1()
    cleaned_data += _read_clean_data2()
    cleaned_data += _read_clean_data3()

    # Group and save the data
    data_frame = DataFrame(cleaned_data).groupby(['cat', 'date']).sum()
    data_frame = data_frame.reset_index()

    # fill 0 where date is empty
    dates = data_frame.date.unique()
    for cat in data_frame.cat.unique():
        for date in dates:
            val = data_frame[data_frame['cat'] == cat][data_frame['date'] == date]
            if val.empty:
                new = DataFrame([[cat, date, 0]], columns=['cat', 'date', 'value'])
                data_frame = data_frame.append(new, ignore_index=True)
    data_frame = data_frame.sort_values(['cat', 'date'])

    file_cleaned = os.path.join(path, 'data/data_cleaned.json')
    with open(file_cleaned, 'w') as outfile:
        json.dump(data_frame.to_dict(orient='records'), outfile)
    print "DATA CLEANED AND SAVED"


def _read_clean_data1():
    file1 = os.path.join(path, 'data/data1.json')
    with open(file1) as data_file:
        data = json.load(data_file)
    for d in data:
        d['cat'] = d['cat'].upper()  # upper to category
        d['date'] = datetime.fromtimestamp(d['d']/1000.0).date().isoformat()  # datetime from milliseconds
        d.pop('d')
    return data


def _read_clean_data2():
    file2 = os.path.join(path, 'data/data2.json')
    with open(file2) as data_file:
        data = json.load(data_file)
    for d in data:
        d['date'] = datetime.strptime(d['myDate'], '%Y-%m-%d').date().isoformat()
        d['value'] = d['val']  # key name is value
        d['cat'] = d['categ'].upper()  # key name is cat
        d.pop('val')
        d.pop('myDate')
        d.pop('categ')
    return data


def _read_clean_data3():
    file3 = os.path.join(path, 'data/data3.json')
    with open(file3) as data_file:
        data = json.load(data_file)
    for d in data:
        match_date = re.search(r'(\d+-\d+-\d+)', d['raw'])
        d['date'] = datetime.strptime(match_date.group(0).strip(), '%Y-%m-%d').date().isoformat()

        match_cat = re.search(r'#(.*?)#', d['raw'])
        d['cat'] = match_cat.groups()[0].upper().strip()

        d['value'] = d['val']  # key name is value
        d.pop('val')
        d.pop('raw')
    return data


if __name__ == "__main__":
    normalise()
