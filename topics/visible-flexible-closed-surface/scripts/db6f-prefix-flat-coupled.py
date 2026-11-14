#!/usr/bin/env python3
"""Nonlinear prefix plus actual weighted tail with a flat-acceleration metric."""
import importlib.util
from pathlib import Path
S=Path(__file__).resolve().parent
def mod(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
m=mod('db6f_coupled',S/'db6f-prefix-coupled.py')
patch=mod('db6f_flat_patch',S/'db6f-prefix-flat-profile.py');patch.install(m.adaptive)
if __name__=='__main__':m.main()
