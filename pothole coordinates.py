import json

   #parsing a large json file to python
with open('Potholes_512x512.json') as x: 
     data_list = json.load(x) 
   # Printing out all the pothole bounding box coordinates
for item in data_list:
    item_label = item['Label']

    # check if the item['Label'] is empty. If empty, continue to the next item.
    if bool(item_label)==False:
        continue
    # check if the item['Label']['objects'] is empty, if so, proceed to the next item.
    elif bool(item_label['objects']==False):
        continue
    # if all is well, execute the loop below for all the items.
    else:
        for dictionary in item_label['objects']:
            print(dictionary['bbox'])
