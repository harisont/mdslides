#!/usr/bin/python

import sys
from os import system
from os.path import isfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('md_file', 
                    help="path to the markdown file to be converted")
parser.add_argument('-o', 
                    '--output', 
                    metavar='FILE', 
                    default="out.pdf",
                    help="path to the output pdf file") 
parser.add_argument('-c',
                    '--colors',
                    metavar='CVALS',
                    default="unipg themes",
                    help="personalized color scheme")
parser.add_argument('-l',
                    '--logo',
                    metavar='FILE',
                    help="path to the logo to be shown in the presentation")
args = parser.parse_args()

if not isfile(args.md_file):
  print(args.md_file + "is not a file.")
  exit()

                                         
'''
  if (len(sys.argv) > 3) and (sys.argv[3] == "-l"): # this if is all brutal and needs to be changed
    logofile = sys.argv[4]
    styfile = open("beamerthememhthm.sty",'r+')
    lines = styfile.readlines() 
    styfile.seek(0)
    styfile.write("\\logo{\\includegraphics[height=0.8cm]{" + logofile + "}\\vspace{239pt}} \n") 
    for line in lines:
      styfile.write(line)
    styfile.close()
  # TODO: use something more advanced than system for all the options; also use format
  system("pandoc " + in_file + " -t beamer -o" + out_file)
  '''