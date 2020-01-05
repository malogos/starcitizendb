# -*- coding: utf-8 -*-
''' convert the insane sc ini format into yaml '''

import lib_scdb
from lib_scdb import global_vars
from lib_scdb import read_file
from lib_scdb import yaml_write
# from lib_scdb import yaml_pprint

config = global_vars()

def convert_ini():
  ''' read global ini and write out localization dcts for items/ships and manufacturers '''
  print('Converting and writing localization data')
  # read in global ini
  path_ini = config['path']['localization_global']
  ini_lines = read_ini(path_ini)

  # convert to dcts
  ini_dcts = convert_ini_to_dcts(ini_lines)
  item_dcts = parse_descriptions(ini_dcts)
  manu_dcts = parse_manufacturer(ini_lines)
  # yaml_print(item_dcts)

  # write yamls
  yaml_write(config['path']['global'], item_dcts)
  yaml_write(config['path']['global_manu'], manu_dcts)
#
def read_ini(ini_path):
  ''' read in global.ini '''
  ini_raw_list = read_file(ini_path, split=True)
  ini_raw_list = [line.strip() for line in ini_raw_list]
  ini_raw_list = [line.encode("utf-8") for line in ini_raw_list]
  return ini_raw_list
#
def convert_ini_to_dcts(ini_lines):
  ''' return ini as list of dcts '''
  prefixes = ['vehicle_Name', 'vehicle_Desc', 'item_Name', 'item_Desc']
  prefixes = [prefix.encode("utf-8") for prefix in prefixes]

  item_list = []
  for line in ini_lines:
    # print(line.decode('cp1252', 'ignore'))
    # line = line.decode('utf-8').replace('_SCItem','').encode('utf-8')
    for prefix in prefixes:
      if line.startswith(prefix):
        prefix_key = prefix.decode('utf-8')
        split_line = line.decode('utf-8').replace(prefix.decode('utf-8'), '').split('=')
        if split_line[0].startswith('_'):
          split_line[0] = split_line[0][1:]
        if '_SCItem' in split_line[0]:
          split_line[0] = split_line[0].replace('_SCItem','')
        if split_line[0] not in [item.get('item') for item in item_list]:
          item_list.append({'item':split_line[0], prefix_key:split_line[1].encode("utf-8").decode('utf-8')})
        else:
          for item in item_list:
            if item['item'] == split_line[0]:
              item[prefix_key] = split_line[1]

  return item_list
#
def parse_descriptions(item_dcts):
  ''' parse out manufacturer and other data hidden in item_Desc and vehicle_Desc'''
  for item_dct in item_dcts:
    desc = item_dct.get('item_Desc', item_dct.get('vehicle_Desc',''))
    if 'Item Type:' in desc:
      # new descs
      ''' "item_Desc": "Item Type: Power Plant\\nSize: 1\\nGrade: B\\nClass: Competition\\n\\nPerformance: 125\\nSignals: 116\\nEfficiency: 95\\n\\nFour generations of racing knowledge and know-how are behind ACOM\u2019s StarHeart power plant. Known for its rapid power distribution, the StarHeart has become a favorite among speedsters.",'''
      desc_split = desc.split('\\n')
      desc_split = [s for s in desc_split if s]
      for ds in desc_split:
        item_split = ds.split(':')
        if len(item_split) > 2:
          print('YOU HAVE A PROBLEM WITH', item_dct)
        if len(item_split) == 2:
          item_dct[item_split[0]] = item_split[1].strip()
        if len(desc_split) > 1 and len(item_split) == 1:
          item_dct['item_Desc'] = ds
    elif 'Manufacturer' in desc:
      # ships
      if '\\nFocus:' in desc:
        desc_split = desc.split('\\nFocus:')
        item_dct['manufacturer'] = desc_split[0].split(':')[1].strip()#.replace('\\n', '')
        item_dct['focus'] = desc_split[1].split('\\n\\n')[0].strip()
        item_dct['vehicle_Desc'] = desc_split[1].split('\\n\\n')[1].strip()

  return item_dcts
#
def parse_manufacturer(ini_lines):
  ''' convert ini to manufacturer json '''
  ''' manufacturer_DescWETK=  Upstart company made by former employees of Ascension Astro. manufacturer_NameACAS=Ace Astrogation'''
  manufacturer_dcts = {}
  ini_lines = [line.decode('utf-8') for line in ini_lines]
  for line in ini_lines:
    if line.startswith('manufacturer_Name'):
      name_line = line.replace('manufacturer_Name','').split('=')
      manufacturer_dcts[name_line[0]] = {'name':name_line[1]}
  for line in ini_lines:
    if line.startswith('manufacturer_Desc'):
      desc_line = line.replace('manufacturer_Desc','').split('=')
      if desc_line[0] in manufacturer_dcts:
        manufacturer_dcts[desc_line[0]]['description'] = desc_line[1]

  return manufacturer_dcts

if __name__ == '__main__':
  main()
