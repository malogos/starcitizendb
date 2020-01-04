# -*- coding: utf-8 -*-
''' pak data in SC dir -> XMLs in sc game_data
    can include copying Data.p4k, but it's easier to just manually copy it
'''

import os
import shutil
import subprocess

import lib_scdb
from lib_scdb import global_vars

config = global_vars()
dir_p4k_tools = config['path']['dir_p4k_tools']

def copy_p4k(version=['LIVE', 'PTU']):
  ''' copy Data.p4k to tools dir, but easier to just do this manually '''
  path_data_pak = config['path']['dir_cig'] / f'StarCitizen/{version}/Data.p4k'

  print('copying', path_data_pak, 'to', dir_p4k_tools)
  shutil.copy(path_data_pak, dir_p4k_tools)
#

def unp4k_and_unforge():
  print('unp4k and unforge')
  # unp4k()  
  move_unpacked()
#
def unp4k():
  ''' unpak Data.p4k using unp4k.exe '''
  path_extracter = './unp4k.exe'
  path_p4k       = './Data.p4k'

  print(' extracting', path_p4k)
  print(f'  command: {path_extracter} {path_p4k} .ini')
  print('=======================-=-=-=-=-=-====================')
  os.chdir(dir_p4k_tools)
  subprocess.call(path_extracter + ' ' + path_p4k + ' .ini', stdin=None, stdout=None, stderr=None, shell=False)
  print(f'  command: {path_extracter} {path_p4k}')
  subprocess.call(path_extracter + ' ' + path_p4k + ' .xml', stdin=None, stdout=None, stderr=None, shell=False)
#
def move_unpacked():
  ''' move Data and Engine from tools dir to game data repo '''
  move_files = ['Data', 'Engine']
  move_paths = [str(dir_p4k_tools / f) for f in move_files]

  for mp in move_paths:
    print('moving', mp, 'to', config['path']['origin'])
    shutil.move(mp, config['path']['origin'])
#


if __name__ == '__main__':
  # copy_p4k()
  unp4k_and_unforge()
