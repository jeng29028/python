#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      home
#
# Created:     28/12/2014
# Copyright:   (c) home 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
import tkFileDialog

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = tkFileDialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)