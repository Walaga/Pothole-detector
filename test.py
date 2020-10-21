import json
import csv

  #parsing a large json fail to python
with open('test.json') as x: 
     data_list = json.load(x) 
   
    # Generating the csv file with the different column headings listed.
f=csv.writer(open('test.csv', 'w'))
f.writerow(["Class", "fileName", "top","left","height","width","ymin","xmin","ymax","xmax"])


for item in data_list:
    item_label = item['Label']

    # check if the item['Label'] is empty. If empty, continue to the next item.
    # if bool(item_label)==False:
    if 'Label' not in item:
        continue
    # check if the item['Label']['objects'] is empty, if so, proceed to the next item.
    # elif bool(item_label['objects']==False):
    if 'objects' not in item_label:
        continue
    # if all is well, execute the loop below for all the items.
    else:
        for data in item_label['objects']:
            # print(dictionary['bbox'])
            f.writerow([data['title'], 
                        item['External ID'], 
                        data['bbox']['top'], 
                        data['bbox']['left'], 
                        data['bbox']['height'], 
                        data['bbox']['width'],
                        data['bbox']['top'] - data['bbox']['height'],       #ymin = top - height
                        data['bbox']['left'],                               #xmin = left
                        data['bbox']['top'],                                #ymax = "top"
                        data['bbox']['left'] + data['bbox']['width']       #xmax = "left + width"
                        ])

# the maths here doesn't make sense          (top, ymax) ________________
# ymin="top"                                            |                |
# xmin ="left"                      ==============>     |                |
# ymax ="top + width"                                   |                |
# ymin ="left + height"                                 |                |
#                                         (bottom, ymin)|________________|
#                                            (left, xmin)              (right, ymax)