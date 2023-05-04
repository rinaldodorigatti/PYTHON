#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 22 14:41:37 2023
@author: Gabriel Coutinho De Miranda
"""

import os
import shutil
import sys
import threading
import time

progressCOLOR = '\033[38;5;33;48;5;236m'
finalCOLOR =  '\033[38;5;33;48;5;33m'
BOLD    = '\033[1m'
UNDERLINE = '\033[4m'
CEND    = '\033[0m'

def getprecentprogress(source_path, destination_path):
    time.sleep(.24)
    if os.path.exists(destination_path):
        while os.path.getsize(source_path) != os.path.getsize(destination_path):
            sys.stdout.write('\r')
            percentagem = int((float(os.path.getsize(destination_path))/float(os.path.getsize(source_path))) * 100)
            steps = int(percentagem/5)
            copiado = int(os.path.getsize(destination_path)/1000000)
            sizzz = int(os.path.getsize(source_path)/1000000)
            sys.stdout.write(("         {:d} / {:d} Mb   ".format(copiado, sizzz)) +  (BOLD + progressCOLOR +
                                                                                       "{:20s}".format('|'*steps)
                                                                                       + CEND) + ("   {:d}% ".format(percentagem)))
            sys.stdout.flush()
            time.sleep(.01)

def cpprogress(source, destination):
    if os.path.isdir(destination):
        dst_file = os.path.join(destination, os.path.basename(source))
    else: dst_file = destination
    print(" ")
    print (BOLD + UNDERLINE + "FROM:" + CEND + "   ", source)
    print (BOLD + UNDERLINE + "TO:" + CEND + "     ", dst_file)
    print(" ")
    threading.Thread(name='progresso', target=getprecentprogress, args=(source, dst_file)).start()
    shutil.copy2(source, destination)
    time.sleep(.02)
    sys.stdout.write('\r')
    sys.stdout.write(("         {:d} / {:d} Mb   ".format((int(os.path.getsize(dst_file)/1000000)),
                                                          (int(os.path.getsize(source)/1000000)))) +
                     (BOLD + finalCOLOR + "{:20s}".format('|'*20) + CEND) + ("   {:d}% ".format(100)))
    sys.stdout.flush()
    print(" ")
    print(" ")


if __name__ == '__main__':
    src = 'FILES/spyder.sh'
    dst = 'FILES2/spyder.sh'
    cpprogress(src, dst)