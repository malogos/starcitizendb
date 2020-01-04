# -*- coding: utf-8 -*-
''' control parsing process from single script '''

import sys

import fire

import lib_scdb
import directory_create


def main():
  directory_create.create_data_dirs()
#
if __name__ == '__main__':
  if len(sys.argv)>1:
    fire.Fire()
  else:
    print(__file__)
    main()
