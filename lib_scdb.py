# -*- coding: utf-8 -*-
''' lib for shared sc data parsing functions and variables '''

import io
import yaml
from pathlib import Path


def global_vars():
  ''' return variables such as file paths that are needed by several scripts '''
  v = {}
  v['configs'] = yaml_read(Path.cwd() / 'config.yaml')

  abs_paths = ['dir_cig', 'dir_data_root']
  for ap in abs_paths:
    v['configs']['path'][ap] = Path(v['configs']['path'][ap])

  return v
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
def main():
  ''' oops '''
  print('this is a library...\n')
  print('config output:\n')
  v = global_vars()
  yaml_print(v['configs'])
#
if __name__ == '__main__':
  main()
