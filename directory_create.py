# -*- coding: utf-8 -*-
''' create directory structure for game files '''

import os
from pathlib import Path

import lib_scdb
from lib_scdb import global_vars

config = global_vars()


def create_data_dirs():
  ''' create directories for storing game files for current game version '''
  print('creating directories for storing game files for current game version')
  paths = [config['path']['dir_data_version_root'],
           config['path']['origin'],
           config['path']['output'],
          ]

           # lib_sc.path_version_root,
           # lib_sc.path_raw,
           # lib_sc.path_raw_data,
           # lib_sc.path_out,
           # lib_sc.path_json['root'],
           # lib_sc.path_csv,
           # lib_sc.path_sim]

  for path in paths:
    print('', str(path))
    make_dir(path)

  output_subdirs = config['path']['output_subdirs']
  for subdir in output_subdirs:
    path_dir = config['path']['output'] / subdir
    print('', str(path_dir))
    make_dir(path_dir)

  ''' path_sets = [lib_sc.path_json]
  for path_set in path_sets:
    for _, _path in path_set.items():
      make_dir(_path)

  subdirs = [lib_sc.path_ship_subdirs, lib_sc.path_ammo_subdirs, lib_sc.path_sim_subdirs, lib_sc.path_fps_subdirs]
  for subdir in subdirs:
    for k, v in subdir.items():
      make_dir(v)'''
#
def make_dir(dir_path):
  ''' create directory if non existant'''
  if not dir_path.is_file():
    dir_path.mkdir(exist_ok=True, parents=True)
#
if __name__ == '__main__':
  create_data_dirs()
