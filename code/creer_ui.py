#!/usr/bin/python
# -*- coding: utf-8 -*

from os import system

system("pyuic4 _sources_ui/FenetreBVN/fenetrebvn.ui > _ui/ui_fenetrebvn.py")
system("pyuic4 _sources_ui/Menu/menu.ui > _ui/ui_menu.py")
system("pyuic4 _sources_ui/Module/module.ui > _ui/ui_module.py")
system("pyuic4 _sources_ui/Score/score.ui > _ui/ui_score.py")
