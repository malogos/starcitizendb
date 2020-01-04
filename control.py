# -*- coding: utf-8 -*-
''' control parsing process from single script '''

import sys

import fire

import lib_scdb
from directory_create import create_data_dirs
from extract_p4k import unp4k_and_unforge



def main():
  # create directory framework and extract p4k into XML
  # create_data_dirs()
  # unp4k_and_unforge()

  # convert xml data to yaml
  

#
if __name__ == '__main__':
  if len(sys.argv)>1:
    fire.Fire()
  else:
    print(__file__)
    main()
