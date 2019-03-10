# Created by: Storm Shadow http://www.techbliss.org
import os
import ida_idaapi, ida_kernwin
import idc
from idc import *
from idaapi import *
import sys
sys.path.insert(0 , idaapi.idadir("plugins\\geo\\icons")) #change path to the icon
sys.path.insert(0 , idaapi.idadir("plugins"))
sys.path.insert(0, idaapi.idadir("plugins\\geo\\"))
import ico
from ico import *
import subprocess

PLUGIN_VERSION = "1.4" #change Plugin Version
IDAVERISONS    = "IDA PRO 7.0+" #change Ida version
AUTHORS        = "Storm Shadow" #change author
DATE           = "2017" #change date
TWITTER        = "Twitter @zadow28" #change social media

def banner():
    banner_options = (PLUGIN_VERSION, AUTHORS, DATE, TWITTER, IDAVERISONS)
    banner_titles = "Geo Locator v%s - (c) %s - %s - %s - %s" % banner_options #change Python editor

# print plugin banner
    print("---[" + banner_titles + "]---\n")

banner()

# 1) Create the handler class
class MyEditorHandler(idaapi.action_handler_t): # the class name must be unique for each plugin nb same as line (53)
    def __init__(self):
        idaapi.action_handler_t.__init__(self)

    # Run editor when invoked.
    def activate(self, ctx):
		g = globals()
		idahome = idaapi.idadir("plugins\\geo") #change to set plguin path where the main plguin script is
		process = subprocess.Popen(['python', idahome + "\\geo.py"])
		#print os.getcwd()		#change for the main plugin script

    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS

class geoeye(idaapi.plugin_t): #change class to unique name for each plugin , also change line (103)
    flags = idaapi.PLUGIN_FIX #different flags this is for plugin visible at startup
    comment = "Run me" #help me text
    help = "Geo helper" #help text
    wanted_name = "Geo locate" #change the plugins name
    wanted_hotkey = "" #the tooltip goes away in menu when setting it here ,DONT DO it! and only is shown in File/Plugins menu


    def locate_menuaction(self): #change for something unique.also change line (90)
        action_desc = idaapi.action_desc_t(
            'my:locateaction',  # The action name. This acts like an ID and must be unique same as line (64), (68)
            'Geo locate!',  # The action text.
            MyEditorHandler(),  # The action handler must be unique , also change line (99)
            'Ctrl+G',  # Optional: the action shortcut DO IT  HERE!
            'Geo locate',  # Optional: the action tooltip (available in menus/toolbar)
            idaapi.load_custom_icon(":/ico/python.png")  # hackish load action icon , if no custom icon use number from 1-150 from internal ida
        )

        # 3) Register the action
        idaapi.register_action(action_desc)

        idaapi.attach_action_to_menu(
            'File/Editor...',  # The relative path of where to add the action
            'my:locateaction',  # The action ID (see line(51))
            idaapi.SETMENU_APP)  # We want to append the action after the 'Manual instruction...

        form = idaapi.get_current_tform()
        idaapi.attach_action_to_popup(form, None, "my:locateaction", None) # The action ID (see line(51)

    def init(self):
        """
        This is called by IDA when it is loading the plugin.
        """
        #self._icon_id_file = idaapi.BADADDR
        # attempt plugin initialization
        try:
            self._install_plugin()

        # failed to initialize or integrate the plugin, log and skip loading
        except Exception as e:
            form = idaapi.get_current_tform()
            pass

        return PLUGIN_KEEP

    def _install_plugin(self):
        """
        Initialize & integrate the plugin into IDA.
        """
        self.locate_menuaction() #same as line (49)
        self._init()

    def term(self):
        pass

    def run(self, arg = 0):
        #we need the calls again if we wanna load it via File/Plugins/editor
        idaapi.msg("Python Geo loacte Loaded to menu \n use Alt+G hot key to quick load ")
        hackish = MyEditorHandler() #must be the same as line (53) change also hackish =  must be unique also line (100)
        hackish.activate(self)  #hackish must the same as line hackish = (99)

def PLUGIN_ENTRY():
    return geoeye() #must be unique for each plugin and same as line 43