# -*- coding: utf-8 -*-
''' convert ship xml into yaml '''

import lib_scdb
from lib_scdb import global_vars
from lib_scdb import get_paths_by_ext
from lib_scdb import read_file
from lib_scdb import yaml_write
from lib_scdb import xml_to_dct
from lib_scdb import yaml_pprint


config = global_vars()

def convert_ship_xmls():
  ''' '''
  ship_xmls = get_paths_by_ext(config['path']['df_spaceships'], '.xml', True)[:1]
  for ship_xml in ship_xmls:
    ship_dct = xml_to_dct(ship_xml)

    # rename primary key
    for k,v in list(ship_dct.items()):
      if k.startswith('EntityClassDefinition.') and 'Components' in v:
        name = k.replace('EntityClassDefinition.','')
        ship_dct[name] = ship_dct.pop(k)


    # ship_dct[new_key] = mydict.pop(old_key)

    # ship_dct.pop(ship_dct.keys()[0], ship_dct.keys()[0].replace('EntityClassDefinition.', ''))

    # print(ship_dct.keys())
    # remove crap
    # flatten hardpoints (json_convert_ship_loads.py)

    yaml_pprint(ship_dct)
    '''for k,v in list(dcts_df.items()):
    if k.startswith('EntityClassDefinition.') and 'Components' in v:
      print(k)
      # print('', v['Components'])
      if isinstance(v['Components'], dict) and v['Components'].get('SCItem'):
        # if isinstance(v['Components'], dict) and v['Components'].get('SAttachableComponentParams'):
        v['@name'] = k.replace('EntityClassDefinition.','').replace('_SCItem', '')'''


if __name__ == '__main__':
  convert_ship_xmls()
