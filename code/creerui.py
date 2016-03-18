#!/usr/bin/python
# -*- coding: utf-8 -*

from os import system

system("pyuic4 qt/FenetreBVN/fenetrebvn.ui > ui_fenetrebvn.py")
system("pyuic4 qt/Menu/menu.ui > ui_menu.py")
system("pyuic4 qt/Module/module.ui > ui_module.py")
