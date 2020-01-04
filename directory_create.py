# -*- coding: utf-8 -*-
''' create directory structure for game files '''

import os
from pathlib import Path

import lib_scdb

def create_game_dirs():
  paths = [Path('C:/Users/mike/Dropbox/code/python3/sc/starcitizendb/test')]
  for path in paths:
    make_dir(path)
#
def make_dir(dir_path):
  ''' create directory if non existant'''
  if not dir_path.is_file():
    dir_path.mkdir(exist_ok=True, parents=True)
#
if __name__ == '__main__':
  create_game_dirs()
