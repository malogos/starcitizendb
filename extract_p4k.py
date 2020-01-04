# -*- coding: utf-8 -*-
''' pak data in SC dir -> XMLs in sc game_data
    can include copying Data.p4k, but it's easier to just manually copy it
'''

import os
import shutil
import subprocess
from pathlib import Path

import lib_scdb
from lib_scdb import global_vars
from lib_scdb import get_paths_by_ext

config = global_vars()
dir_p4k_tools = config['path']['dir_p4k_tools']
dir_xmls = config['path']['foundry_origin']

path_unforge_exe = dir_p4k_tools / config['path']['unforge_exe']

path_game_dcb = config['path']['origin'] / 'Data/Game.dcb'
path_game_xml = config['path']['origin'] / 'Data/Game.xml'

def copy_p4k(version=['LIVE', 'PTU']):
  ''' copy Data.p4k to tools dir, but easier to just do this manually '''
  path_data_pak = config['path']['dir_cig'] / f'StarCitizen/{version}/Data.p4k'

  print('copying', path_data_pak, 'to', dir_p4k_tools)
  shutil.copy(path_data_pak, dir_p4k_tools)
#

def unp4k_and_unforge():
  print('unp4k and unforge')
  unp4k()
  move_unpacked()

  unforge_dcb(path_unforge_exe, path_game_dcb, path_game_xml)
  # unforge_xmls(dir_xmls)

#
def unp4k():
  ''' unpak Data.p4k using unp4k.exe '''
  path_extracter = './unp4k.exe'
  path_p4k       = './Data.p4k'

  print(f'  extracting {path_p4k}')
  print(f'   command: {path_extracter} {path_p4k} .ini')
  print('=======================-=-=-=-=-=-====================')
  os.chdir(dir_p4k_tools)
  subprocess.call(f'{path_extracter} {path_p4k} .ini', stdin=None, stdout=None, stderr=None, shell=False)
  print(f'   command: {path_extracter} {path_p4k}')
  subprocess.call(f'{path_extracter} {path_p4k} .xml', stdin=None, stdout=None, stderr=None, shell=False)
#
def move_unpacked():
  ''' move Data and Engine from tools dir to game data repo '''
  move_files = ['Data', 'Engine']
  move_paths = [str(dir_p4k_tools / f) for f in move_files]

  for mp in move_paths:
    print(f"  Moving {mp} to {config['path']['origin']}")
    shutil.move(mp, config['path']['origin'])
#
def unforge_dcb(path_unforge_exe, path_game_dcb, path_game_xml):
  ''' unforge the dcb file '''
  print('  unforge dcb')
  # if not os.path.exists(path_game_xml):
  print(f'  {path_unforge_exe} {path_game_dcb} {path_game_xml}')
  subprocess.call(f'{path_unforge_exe} {path_game_dcb}', stdin=None, stdout=None, stderr=None, shell=False)
  # shutil.move(os.path.join(gamedata_path, 'Game.xml'), path_game_xml)
#
def unforge_xmls(dir_xml):
  ''' convert XMLs from binary to readable '''
  print(f'  unforge XMLs in {dir_xml}')
  xml_paths = get_paths_by_ext(dir_xml, '.xml', True)

  for xml_path in xml_paths:
    print(f'    {xml_path}')
    subprocess.call(f'{path_unforge_exe} "{xml_path}"', stdin=None, stdout=None, stderr=None, shell=False)
    # try:
    raw = xml_path.replace('xml', 'raw')
    if Path(raw).is_file():
      shutil.move(raw, xml_path)
#


if __name__ == '__main__':
  # copy_p4k()
  unp4k_and_unforge()
