# -*- coding: utf-8 -*-
''' lib for shared sc data parsing functions and variables '''

import io
import sys
import oyaml as yaml
from pathlib import Path

import xmltodict


def global_vars():
  ''' return variables such as file paths that are needed by several scripts '''
  v = {}
  config = yaml_read(Path.cwd() / 'config.yaml')

  # todo: pull current live/ptu version from CIG

  abs_paths = ['dir_cig', 'dir_data_root_win', 'dir_data_root_lin', 'dir_p4k_tools']
  for ap in abs_paths:
    config['path'][ap] = Path(config['path'][ap])

  # set data root path based on OS being used
  platform = sys.platform
  if 'linux' in platform:
    dir_data_root = config['path']['dir_data_root_lin']
  elif 'win' in platform:
    dir_data_root = config['path']['dir_data_root_win']
  config['path']['dir_data_root'] = dir_data_root

  # path to current version
  dir_data_version_root = dir_data_root / config['version']['current']
  config['path']['dir_data_version_root'] = dir_data_version_root

  config['path']['origin'] = config['path']['dir_data_version_root'] / 'origin'
  config['path']['output'] = config['path']['dir_data_version_root'] / 'output'

  config['path']['output_subdirs'] = ['local']

  config['path']['foundry_origin'] = config['path']['origin'] / config['path']['foundry']
  config['path']['df_components'] = config['path']['foundry_origin'] / 'entities/scitem/ships'  # df components
  config['path']['df_spaceships'] = config['path']['foundry_origin'] / 'entities/spaceships'  # df ships

  config['path']['localization_global'] = config['path']['origin'] / config['path']['localization_global']

  config['path']['local'] = config['path']['output'] / 'local'
  config['path']['global'] = config['path']['local'] / 'global.yaml'
  config['path']['global_manu'] = config['path']['local'] / 'manufacturers.yaml'

  return config
#
def yaml_read(fp):
  ''' read in yaml file and return dct '''
  f = read_file(fp)
  return yaml.full_load(f)
#
def yaml_write(fp, content):
  ''' write content to fp '''
  with open(fp, 'w') as f:
    yaml.dump(content, f, default_flow_style=False)
#
def yaml_pprint(dct):
  print(yaml.dump(dct, default_flow_style=False))
#
def read_file(path, split=False):
  ''' read file '''
  with io.open(path, "r", encoding="utf-8") as f:
    if split:
      return f.read().splitlines()
    else:
       return f.read()
#
def get_paths_by_ext(dir_root_path, ext, recursive=True):
  ''' return list of all files that have a given extension '''
  if recursive:
    paths = [f for f in dir_root_path.rglob("*") if f.suffix==ext]
  else:
    paths = [f for f in dir_root_path.iterdir() if f.suffix==ext]
  paths.sort()
  return paths
#
def xml_to_dct(xml_path, ordered=True, verbose=False):
  ''' return xml as ordered dct '''
  with open(xml_path, 'rb') as xml_string:
    # try:
      if verbose:
        print(xml_path)
      ordered_dct = xmltodict.parse(xml_string)
      if not ordered:
        return yaml.dump(ordered_dct, default_flow_style=False)
        # return json.loads(json.dumps(ordered_dct, ensure_ascii=False))
      else:
        return ordered_dct
    # except:
      return {}
#
def main():
  ''' oops '''
  print('this is a library...\n')
  print('config output:\n')
  config = global_vars()
  yaml_pprint(config)
#
if __name__ == '__main__':
  main()
