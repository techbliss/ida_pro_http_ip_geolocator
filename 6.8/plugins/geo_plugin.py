# Created by: Storm Shadow http://www.techbliss.org

# WARNING! All changes made in this file will be lost!
import re
import idaapi
import idc
from idc import *
from idaapi import *
import sys
sys.path.insert(0 , idaapi.idadir("plugins\\geo\\icons"))
import ico
from ico import *
import subprocess
from subprocess import Popen
class ripeyess(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "This is a comment"

    help = "geo"
    wanted_name = "http ip locator"
    wanted_hotkey = "ALT-G"



    def init(self):
        idaapi.msg("http ip locator Is Found Use Alt+G to load to menu \n")
        return idaapi.PLUGIN_OK


    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")



    def AddMenuElements(self):
        idaapi.add_menu_item("File/", "Geo", "ALT-G", 0, self.popeye, ())
        idaapi.set_menu_item_icon("File/Geo", idaapi.load_custom_icon(":/ico/python.png"))




    def run(self, arg = 0):
        idaapi.msg("geo Loaded to menu use Alt+E once more")
        self.AddMenuElements()

    def popeye(self):
		idahome = idaapi.idadir("plugins\\geo")
		os.chdir(idahome)
		subprocess.Popen('python.exe geo.py')




def PLUGIN_ENTRY():
    return ripeyess()