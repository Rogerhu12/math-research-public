#!/usr/bin/env python3
"""Actual nonlinear Frenet prefix with a new flat-acceleration physical metric.
Uses a finite linear tail port; no complete closed-surface claim.
"""
import importlib.util
from pathlib import Path
S=Path(__file__).resolve().parent
def mod(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
m=mod('db6f_adaptive',S/'950f-prefix-adaptive-chart-bvp-v2.py')
patch=mod('db6f_flat_patch',S/'db6f-prefix-flat-profile.py');patch.install(m)
if __name__=='__main__':m.main()
