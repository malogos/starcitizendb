# -*- coding: utf-8 -*-
''' lib for shared sc data parsing functions and variables '''

import io
import sys
import yaml
from pathlib import Path


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

  config['path']['foundry_origin'] = config['path']['origin'] / config['path']['foundry']

  return config
#
def yaml_read(fp):
  ''' read in yaml file and return dct '''
  f = read_file(fp)
  return yaml.full_load(f)
#
def yaml_print(dct):
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
def main():
  ''' oops '''
  print('this is a library...\n')
  print('config output:\n')
  config = global_vars()
  yaml_print(config)
#
if __name__ == '__main__':
  main()
